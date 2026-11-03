import os
import secrets
import string
from pathlib import Path

import psycopg
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

ALPHABET = string.ascii_letters + string.digits


def db_password() -> str:
    # Step 9 uses a secret file; earlier steps use a plain variable.
    path = os.getenv("DB_PASSWORD_FILE")
    if path:
        return Path(path).read_text().strip()
    return os.getenv("DB_PASSWORD", "")


def connect():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "shortly"),
        user=os.getenv("DB_USER", "shortly"),
        password=db_password(),
        connect_timeout=3,
    )


app = FastAPI(title="Shortly")


class LinkIn(BaseModel):
    url: HttpUrl


@app.get("/api/health")
def health():
    try:
        with connect() as conn:
            conn.execute("SELECT 1")
    except Exception:
        raise HTTPException(status_code=503, detail="database unreachable")
    return {"status": "ok"}


@app.post("/api/links", status_code=201)
def create_link(link: LinkIn):
    code = "".join(secrets.choice(ALPHABET) for _ in range(6))
    with connect() as conn:
        conn.execute(
            "INSERT INTO links (code, url) VALUES (%s, %s)",
            (code, str(link.url)),
        )
    return {"code": code, "short_url": f"/s/{code}"}


@app.get("/api/links/{code}")
def link_stats(code: str):
    with connect() as conn:
        row = conn.execute(
            "SELECT url, clicks, created_at FROM links WHERE code = %s",
            (code,),
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="unknown code")
    return {"code": code, "url": row[0], "clicks": row[1], "created_at": row[2].isoformat()}


@app.get("/s/{code}")
def follow(code: str):
    with connect() as conn:
        row = conn.execute(
            "UPDATE links SET clicks = clicks + 1 WHERE code = %s RETURNING url",
            (code,),
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="unknown code")
    return RedirectResponse(row[0], status_code=307)