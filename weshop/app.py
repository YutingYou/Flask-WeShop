# -*- coding: utf-8 -*-

from flask import Flask, render_template
from configs.config import config
from .extensions import db, login_manager, bootstrap


# For import *
__all__ = ['create_app']


def create_app(config_name=None, app_name=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = 'Flask-Weshop'

    app = Flask(app_name)

    return app




