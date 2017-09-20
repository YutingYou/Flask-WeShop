# -*- coding: utf-8 -*-
from weshop.extensions import db


# 用户
class User(db.Model):
    __table_name_ = 'weshop_user'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    openid = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), unique=True, index=True)
    headimgurl = db.Column(db.String(128))
    city = db.Column(db.String(32))
    sex = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# 商品
class Goods(db.Model):
    __tablename__ = 'weshop_goods'
    id = db.Column(db.Integer, primary_key=True)


# 订单
class Order(db.Model):
    __tablename__ = 'weshop_order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_base_info.id'))
    address = db.Column(db.Integer, db.ForeignKey('mall_user_addr.id'))
    datetime = db.Column(db.DateTime)


# 地址
class Address(db.Model):
    __tablename__ = 'mall_user_addr'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(128))
