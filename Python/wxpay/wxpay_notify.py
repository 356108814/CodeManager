# encoding: utf-8
"""
微信支付完成后，微信会把相关支付结果和用户信息发送给商户，商户需要接收处理，并返回应答
@author Yuriseus
@create 2016-5-31 20:03
"""


class WxPayNotify(object):

    def notify(self, element, callback_fun):
        """
        微信通知，业务处理
        @param element: xml转的对象
        @param callback_fun: 业务处理回调函数
        @return:
        """
        if callback_fun and hasattr(callback_fun, '__call__'):
            callback_fun()
