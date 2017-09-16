# -*- coding: utf-8 -*-
from . import weshop
from flask import render_template, request, session
from .forms import QuickBuyForm
from weshop.utils import ezlogger
from weshop.wechat.views import wechat_oauth_decorator, wechat_pay
import json

logger = ezlogger.get_logger('quickbuy', use_stream=True, use_file=False)


@weshop.route('/quickbuy', methods=['GET', 'POST'])
@wechat_oauth_decorator
def quickbuy():

    form = QuickBuyForm()

    if request.method == 'GET':
        logger.debug('request method: %s' % request.method)
        if True:
            # 如果是老用户填充用户信息
            form = QuickBuyForm(goods_type='LSG',
                                order_num=1,
                                custom_addr='福清市城关小学后门7#803',
                                custom_name='游先生',
                                custom_phone='18503061799',
                                delivery_date=0,
                                delivery_time=11)
        return render_template('weshop/quickbuy.html', form=form)
    elif request.method == 'POST':
        logger.debug('request method: %s' % request.method)
        # 只有参数校验都通过时才提交
        if form.validate_on_submit():
            logger.debug('new order, name: %s, phone: %s, addr: %s' %
                         (form.custom_name.data, form.custom_phone.data, form.custom_addr.data))

            # 成功提交订单，弹出支付请求
            params = None
            try:
                result = wechat_pay.order.create('JSAPI', u'景田纯净水', 150, 'http://www.rockbot.top/weshop/jsapi_result/',
                                                 user_id="oZkEowZadq8ajEcu3w4IbH0AcSRY")
                params = wechat_pay.jsapi.get_jsapi_params(result['prepay_id'])
                logger.debug('result:%s' % str(result))
                logger.debug('params:%s' % str(params))
                return render_template('weshop/quickpay.html', params=json.dumps(params))
            except Exception as e:
                logger.debug('pay result ERROR: %s' % e)
                return '微信支付错误'  # TODO
        elif form.errors:
            logger.debug('error: %s' % form.errors)
            return '订单参数输入错误，红色文字标出错误项'  # TODO
        return render_template('weshop/quickbuy.html', form=form, to_str=str, form_errors=form.errors)


@weshop.route('/quickpay', methods=['GET', 'POST'])
def quickpay():
    return render_template('weshop/quickpay.html', params=json.dumps(params))

@weshop.route('/jsapi_pay_result/', methods=['GET', 'POST'])
def jsapi_result():
    logger.debug('get result, %s' % request.values)
    return 'get result'

