FROM python:3.12-slim AS builder

WORKDIR /build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /build

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS final

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PATH="/opt/venv/bin:$PATH"

RUN useradd \
    --uid 10001 \
    --no-create-home \
    --shell /usr/sbin/nologin \
    --no-log-init \
    app

COPY --from=builder /opt/venv /opt/venv

COPY main.py /app

USER 10001

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]