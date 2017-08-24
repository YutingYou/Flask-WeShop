# -*- coding: utf-8 -*-
from configs.config import config as app_config
from flask import Flask, render_template
from .extensions import db, login_manager, bootstrap


# For import *
__all__ = ['create_app']


def create_app(config_name=None, app_name=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = 'Flask-Weshop'

    app = Flask(app_name)
    configure_app(app, config_name)
    configure_blueprints(app)
    configure_extensions(app)

    return app


def configure_app(app, config_name=None):
    """Configure Flask app"""

    if config_name:
        app.config.from_object(app_config[config_name])


def configure_extensions(app):

    # flask-sqlalchemy
    db.init_app(app)


def configure_blueprints(app):
    """Configure blueprints in views."""

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .shop import weshop as weshop_blueprint
    app.register_blueprint(weshop_blueprint, url_prefix='/weshop')











