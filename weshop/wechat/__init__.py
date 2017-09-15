# -*- coding: utf-8 -*-
from flask import Blueprint

wechat = Blueprint('wechat', __name__)

from . import views
