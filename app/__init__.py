from flask import Flask

from config import Config

from .extensions import db, migrate


def create_flask_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models for Flask-Migrate's autogeneration.
    # This must happen after db.init_app(app).
    from app import models  # noqa: F401
    from app.routes import admin_client, api
    app.register_blueprint(api.bp)
    app.register_blueprint(admin_client.bp)

    return app

create_app = create_flask_app
