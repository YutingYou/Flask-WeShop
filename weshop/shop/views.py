# -*- coding: utf-8 -*-
from . import weshop
from flask import render_template, request
from .forms import QuickBuyForm
from weshop.utils import ezlogger

logger = ezlogger.get_logger('quickbuy', use_stream=True, use_file=False)


@weshop.route('/', methods=['GET', 'POST'])
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
            return '成功提交订单，进入支付流程'
        elif form.errors:
            logger.debug('error: %s' % form.errors)
            return '订单参数输入错误，红色文字标出错误项'
        return render_template('weshop/quickbuy.html', form=form, to_str=str, form_errors=form.errors)




