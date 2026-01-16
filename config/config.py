import os


def _normalize_database_url(url: str) -> str:
    # Heroku-style URLs historically used "postgres://", but SQLAlchemy expects "postgresql://".
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql://", 1)
    return url


class Config:
    # NOTE: Override in production via environment variable.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = _normalize_database_url(
        os.environ.get("DATABASE_URL", "sqlite:///app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
