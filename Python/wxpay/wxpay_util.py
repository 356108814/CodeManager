# encoding: utf-8
"""
微信支付工具类
@author Yuriseus
@create 2016-5-31 19:12
"""
import datetime
import random
import string
import time
from urllib import urlencode
import xml.etree.ElementTree as ET

import httplib2
import hashlib

import wxpay_config


class WxPayUtil(object):

    @staticmethod
    def gen_order_time(validity=5):
        """
        获取订单生成时间、失效时间
        @param validity:有效期，单位分钟
        @return:
        """
        nowtime = time.time()
        fmt = '%Y%m%d%H%M%S'
        start_time_array = time.localtime(nowtime)
        expire_time_array = time.localtime(nowtime + validity*60)
        time_start = time.strftime(fmt, start_time_array)
        time_expire = time.strftime(fmt, expire_time_array)
        return time_start, time_expire

    @staticmethod
    def gen_order_no():
        fmt = '%Y%m%d%H%M%S'
        nowtime = time.time()
        microsecond = str(nowtime).split('.')[1].zfill(2)
        order_no = time.strftime(fmt, time.localtime(nowtime)) + microsecond + WxPayUtil.random_number(3)
        return order_no

    @staticmethod
    def random_string(num=10):
        """
        获取随机字符串
        @param num 长度
        """
        return ''.join(random.sample(string.digits + string.letters, num))

    @staticmethod
    def random_number(num=10):
        """
        获取随机数字字符串
        @param num 长度
        """
        return ''.join(random.sample(string.digits, num))

    @staticmethod
    def post_data(url, body=None, is_encode_body=False):
        """
        获取http返回数据
        @param url 请求的url
        @param body xml
        @param is_encode_body
        @return 对象
        """
        content = ''
        try:
            http = httplib2.Http()
            if is_encode_body:
                body = urlencode(body)
            else:
                if body is not None and not isinstance(body, str):
                    body = str(body)
            response, content = http.request(url, 'POST', body)
        except Exception as e:
            pass
            # Logger.error(traceback.format_exc())
        return ET.fromstring(content)

    @staticmethod
    def gen_sign(model_param, ignore_fields=None):
        sign = ''
        if not ignore_fields:
            ignore_fields = ['sign']
        if model_param:
            fields = model_param.__dict__.keys()
            field_list = []
            for index, field in enumerate(fields):
                field_list.append(field)
            field_list.sort()
            sign_field_list = []
            for _, field in enumerate(field_list):
                value = getattr(model_param, field)
                if value and field not in ignore_fields:    # 空串不参与签名
                    sign_field_list.append('%s=%s&' % (field, value))

            string_a = '&'.join(sign_field_list)
            string_sign_temp = string_a + '&key=' + wxpay_config.KEY
            md5 = hashlib.md5()
            md5.update(string_sign_temp)
            sign = md5.hexdigest()
        return sign

if __name__ == '__main__':
    print WxPayUtil.gen_order_time(30)
    # print time.time()
    print WxPayUtil.gen_order_no()
