# -*- coding: utf-8 -*-
from configs.config import config as app_config
from flask import Flask, render_template
from .extensions import db, login_manager, bootstrap


# For import *
__all__ = ['create_app']


def create_app(config_name=None):
    """Create a Flask app."""

    app = Flask(__name__, template_folder='templates')

    configure_app(app, config_name)
    configure_blueprints(app)
    configure_extensions(app)
    configure_error_handlers(app)

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


def configure_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('403.html'), 403






