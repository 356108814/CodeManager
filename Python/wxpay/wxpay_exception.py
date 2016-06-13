# encoding: utf-8
"""
微信支付异常
@author Yuriseus
@create 2016-5-31 17:27
"""


class WxPayError(Exception):
    def __init__(self, error_msg):
        print error_msg


class WxPayParamError(WxPayError):
    pass


class WxPayNetError(WxPayError):
    pass


class WxPayResultParseError(WxPayError):
    pass


class WxPayBusinessProcessError(WxPayError):
    pass
