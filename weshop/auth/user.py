# -*- coding: utf-8 -*-
from ..extensions import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    openid = db.Column(db.String(128), unique=True, index=True)
    avatar_url = db.Column(db.String(256))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)







