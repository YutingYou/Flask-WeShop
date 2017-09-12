# -*- coding: utf-8 -*-
import os

__all__ = ['config', 'ProductionConfig', 'DevelopmentConfig', 'TestingConfig']


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'rockyrocky'  #SECRET_KEY 用于token等加密

    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # 微信公众号配置
    WECHAT_APP_ID = ''
    WECHAT_TOKEN = ''
    WECHAT_AES_KEY = ''
    WECHAT_APP_SECRET = ''

    # 微信支付配置
    WEPAY_API_KEY = ''
    WEPAY_MCH_ID = ''
    WEPAY_MCH_CERT_PATH = ''
    WEPAY_MCH_KEY_PATH = ''

    @staticmethod
    def init_app(app):
        pass


basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


