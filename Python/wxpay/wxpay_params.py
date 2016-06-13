# encoding: utf-8
"""
微信支付参数模型
@author Yuriseus
@create 2016-5-31 17:52
"""

import wxpay_config
from wxpay_util import WxPayUtil


class ParamBase(object):
    def __init__(self):
        self.appid = wxpay_config.APPID
        self.mch_id = wxpay_config.MCHID
        self.nonce_str = WxPayUtil.random_string(32)
        self.sign = ''

    def to_xml(self):
        # 生成xml之前签名
        self.init_sign()
        xml = '<xml>\n'
        fields = self.__dict__.keys()
        for index, field in enumerate(fields):
            value = getattr(self, field)
            if value:
                # one = '    <{field}><![CDATA[{value}]]></{field}>\n'.format(**{'field': field, 'value': value})
                one = '    <{field}>{value}</{field}>\n'.format(**{'field': field, 'value': value})
                xml += one
        xml += '</xml>'
        return xml

    def init_sign(self):
        self.sign = WxPayUtil.gen_sign(self)


class UnifiedOrderParam(ParamBase):
    def __init__(self):
        super(UnifiedOrderParam, self).__init__()
        self.device_info = 'WEB'
        self.fee_type = 'CNY'

        # 具体订单信息
        self.body = ''        # 商品描述

        self.out_trade_no = WxPayUtil.gen_order_no()      # 商品订单号
        self.total_fee = 0      # 总金额，接口中参数支付金额单位为【分】，参数值不能带小数
        self.spbill_create_ip = 0      # APP和网页支付提交用户端ip
        self.notify_url = wxpay_config.NOTIFY_URL
        self.trade_type = 'JSAPI'      # 交易类型
        self.openid = ''      # 用户标识，rade_type=JSAPI，此参数必传

        # 可选参数
        self.detail = ''      # 商品详情
        self.attach = ''
        self.time_start = ''
        self.time_expire = ''
        self.goods_tag = ''
        self.product_id = ''
        self.limit_pay = 'no_credit'    # no_credit--指定不能使用信用卡支付


class OrderQueryParam(ParamBase):
    def __init__(self):
        super(OrderQueryParam, self).__init__()
        self.transaction_id = ''    # 微信的订单号，优先使用
        self.out_trade_no = ''      # 商户订单号，与transaction_id二选一


class CloseOrderParam(ParamBase):
    def __init__(self):
        super(CloseOrderParam, self).__init__()
        self.out_trade_no = ''      # 商户订单号


class RefundParam(ParamBase):
    def __init__(self):
        super(RefundParam, self).__init__()
        self.device_info = 'WEB'
        self.transaction_id = ''    # 微信的订单号，优先使用
        self.out_trade_no = ''      # 商户订单号，与transaction_id二选一
        self.out_refund_no = ''      # 商户系统内部的退款单号
        self.total_fee = 0      # 总金额
        self.refund_fee = 0      # 退款金额
        self.op_user_id = wxpay_config.MCHID      # 操作员


class RefundQueryParam(ParamBase):
    def __init__(self):
        super(RefundQueryParam, self).__init__()
        self.device_info = 'WEB'
        self.transaction_id = ''    # 微信的订单号，优先使用
        self.out_trade_no = ''      # 商户订单号，与transaction_id二选一
        self.out_refund_no = ''      # 商户系统内部的退款单号
        self.refund_id = 0      # 微信生成的退款单号，在申请退款接口有返回


class DownloadbillParam(ParamBase):
    def __init__(self):
        super(DownloadbillParam, self).__init__()
        self.device_info = 'WEB'
        self.bill_date = ''    # 下载对账单的日期，格式：20140603
        self.bill_type = 'ALL'      # ALL，返回当日所有订单信息，默认值SUCCESS，返回当日成功支付的订单REFUND，返回当日退款订单


if __name__ == '__main__':
    m = UnifiedOrderParam()
    print m.to_xml()
