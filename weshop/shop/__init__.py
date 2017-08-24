# -*- coding: utf-8 -*-
from flask import Blueprint

weshop = Blueprint('weshop', __name__)

from . import views