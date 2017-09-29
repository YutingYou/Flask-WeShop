# -*- coding: utf-8 -*-
from weshop.extensions import db


# 用户
class User(db.Model):
    __tablename__ = 'weshop_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    image_url = db.Column(db.String(128))
    category = db.Column(db.String(64), unique=True)


# 订单
class Order(db.Model):
    __tablename__ = 'weshop_order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paid = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('weshop_user.id'))
    goods_id = db.Column(db.Integer, db.ForeignKey('weshop_goods.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('weshop_user_address.id'))
    quantity = db.Column(db.Integer)
    delivery_date = db.Column(db.Integer)
    delivery_time = db.Column(db.Integer)


# 地址
class Address(db.Model):
    __tablename__ = 'weshop_user_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    phone = db.Column(db.String(16))
    address = db.Column(db.String(128))
