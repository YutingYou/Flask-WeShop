# -*- coding: utf-8 -*-
from weshop.extensions import db


# 商品
class Goods(db.Model):
    __tablename__ = 'weshop_goods'
    pass


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
