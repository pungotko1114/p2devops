CREATE TABLE IF NOT EXISTS links (
    id         BIGSERIAL PRIMARY KEY,
    code       VARCHAR(16) NOT NULL UNIQUE,
    url        TEXT        NOT NULL,
    clicks     INTEGER     NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO links (code, url)
VALUES ('docker', 'https://docs.docker.com')
ON CONFLICT (code) DO NOTHING;