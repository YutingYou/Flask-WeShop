# -*- coding: utf-8 -*-
from . import main


@main.route('/')
def index():
    return 'home page.'
