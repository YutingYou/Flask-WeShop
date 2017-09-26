# -*- coding: utf-8 -*-
from . import weshop
from flask import render_template, request, session, redirect, url_for
from .forms import QuickBuyForm
from .models import User, Order, Address, Goods
from weshop.utils import ezlogger
from weshop.wechat.views import wechat_oauth_decorator, wechat_pay
from weshop.extensions import db
from weshop.constants import Role
import json

logger = ezlogger.get_logger('quickbuy', use_stream=True, use_file=False)


@weshop.route('/quickbuy', methods=['GET', 'POST'])
@wechat_oauth_decorator
def quickbuy():

    form = QuickBuyForm()

    # 查询用户是否注册，未注册则注册
    user = User.query.filter_by(openid=session['user_info']['openid']).first()

    if request.method == 'GET':
        logger.debug('request method: %s' % request.method)
        logger.debug('user: %r' % session['user_info'])

        if user is None:
            user = User(role=Role.USER,
                        openid=session['user_info']['openid'],
                        username=session['user_info']['nickname'],
                        headimgurl=session['user_info']['headimgurl'],
                        city=session['user_info']['city'],
                        sex=session['user_info']['sex'],
                        )
            db.session.add(user)
            db.session.commit()
            logger.debug('db, add new user.')
        else:
            # 如果是老用户则查询最近订单快速填写订单
            last_order = Order.query.filter_by(user_id=user.id).order_by(Order.id.desc()).first()
            if last_order:
                goods = Goods.query.filter_by(goods_id=last_order.goods_id).first()
                address = Address.query.filter_by(address_id=last_order.address_id).first()
                form = QuickBuyForm(goods_name=goods.name,
                                    quantity=last_order.quantity,
                                    custom_address=address.address,
                                    custom_name=address.name,
                                    custom_phone=address.phone,
                                    delivery_date=last_order.delivery_date,
                                    delivery_time=last_order.delivery_time)
                logger.debug('old user, auto fill info.')
        return render_template('weshop/quickbuy.html', form=form)
    elif request.method == 'POST':
        logger.debug('request method: %s' % request.method)
        # 只有参数校验都通过时才提交
        if form.validate_on_submit():
            logger.debug('new order, name: %s, phone: %s, addr: %s' %
                         (form.custom_name.data, form.custom_phone.data, form.custom_address.data))
            order = Order()


            # 成功提交订单，弹出支付请求
            return redirect(url_for('.quickpay'))
        elif form.errors:
            logger.debug('error: %s' % form.errors)
            return '订单参数输入错误，红色文字标出错误项'  # TODO
        return render_template('weshop/quickbuy.html', form=form, to_str=str, form_errors=form.errors)


@weshop.route('/pay/', methods=['GET', 'POST'])
def quickpay():
    logger.debug('pay page, user: %r' % session['user_info'])
    params = None
    try:
        result = wechat_pay.order.create('JSAPI', u'景田纯净水', 1, 'http://www.rockbot.top/weshop/jsapi_pay_result/',
                                         user_id=session['user_info']['openid'])
        params = wechat_pay.jsapi.get_jsapi_params(result['prepay_id'])
        logger.debug('result:%s' % str(result))
        logger.debug('params:%s' % str(params))
        return render_template('weshop/quickpay.html', params=json.dumps(params))
    except Exception as e:
        logger.debug('pay result ERROR: %s' % e)
        return '微信支付错误'  # TODO


@weshop.route('/jsapi_pay_result/', methods=['GET', 'POST'])
def jsapi_result():
    xml = request.data
    result = wechat_pay.parse_payment_result(xml)
    logger.debug('%s, pay result, %s' % (request.method, result))

    # 支付成功返回'SUCCESS', 失败则返回'FAIL'，微信收到这两个字符串后不再重试访问支付结果链接
    # TODO
    if True:
        return 'SUCCESS'
    else:
        return 'FAIL'

