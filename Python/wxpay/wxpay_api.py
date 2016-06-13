# encoding: utf-8
"""
微信支付接口封装
@author Yuriseus
@create 2016-5-31 17:35
"""
from wxpay_util import WxPayUtil


class WxPayApi(object):
    def __init__(self):
        pass

    def unified_order(self, order_param):
        """
        统一下单
        @param order_param: UnifiedOrderParam 对象
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
        # 参数验证
        return WxPayUtil.post_data(url, order_param.to_xml())

    def order_query(self, order_query_param):
        """
        订单查询
        @param order_query_param:OrderQueryParam
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/orderquery'
        # 参数验证
        return WxPayUtil.post_data(url, order_query_param.to_xml())

    def close_order(self, close_order_param):
        """
        关闭订单
        @param close_order_param:
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/closeorder'
        # 参数验证
        return WxPayUtil.post_data(url, close_order_param.to_xml())

    def refund(self, refund_param):
        """
        申请退款
        @param refund_param:
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/refund'
        # 参数验证
        return WxPayUtil.post_data(url, refund_param.to_xml())

    def refund_query(self, refund_query_param):
        """
        查询退款
        @param refund_query_param:
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/refundquery'
        # 参数验证
        return WxPayUtil.post_data(url, refund_query_param.to_xml())

    def downloadbill(self, downloadbill_param):
        """
        下载对账单
        @param downloadbill_param:
        @return:
        """
        url = 'https://api.mch.weixin.qq.com/pay/downloadbill'
        # 参数验证
        return WxPayUtil.post_data(url, downloadbill_param.to_xml())


