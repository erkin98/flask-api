"""
Application extensions.

Keeping extension instances in a dedicated module avoids circular imports and
helps keep the application factory clean.
"""

from __future__ import annotations

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

