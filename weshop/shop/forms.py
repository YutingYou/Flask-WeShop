# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, NumberRange
from wtforms import ValidationError
from weshop.constants import GoodsId

mineral_water_choices = [(GoodsId.MINERAL_WATER_JINGTIAN, '景田'),
                         (GoodsId.MINERAL_WATER_YIBAO, '怡宝'),
                         (GoodsId.MINERAL_WATER_LINGSHIGU, '灵石谷')]
delivery_date_choices = [('0', '今天'), ('1', '明天')]
delivery_time_choices = [('9', '09:00 ~ 11:00'),
                         ('10', '10:00 ~ 12:00'),
                         ('11', '11:00 ~ 13:00'),
                         ('12', '12:00 ~ 14:00'),
                         ('13', '13:00 ~ 15:00'),
                         ('14', '14:00 ~ 16:00'),
                         ('15', '15:00 ~ 17:00')]


class QuickBuyForm(FlaskForm):
    goods_id = RadioField('矿泉水品牌', validators=[DataRequired()], choices=mineral_water_choices)
    address_id = IntegerField('地址ID')
    quantity = IntegerField('订购数量(1~50)', validators=[DataRequired(), NumberRange(min=1, max=50)])
    delivery_date = SelectField('配送日期', validators=[DataRequired()], choices=delivery_date_choices)
    delivery_time = SelectField('配送时间', validators=[DataRequired()], choices=delivery_time_choices)
    submit = SubmitField('提交订单')
