# encoding: utf-8
"""
微信支付配置
@author Yuriseus
@create 2016-5-31 17:26
"""

# APPID：绑定支付的APPID（必须配置，开户邮件中可查看）
# MCHID：商户号（必须配置，开户邮件中可查看）
# KEY：商户支付密钥，参考开户邮件设置（必须配置，登录商户平台自行设置）
# 设置地址：https://pay.weixin.qq.com/index.php/account/api_cert
# APPSECRET：公众帐号secert（仅JSAPI支付的时候需要配置， 登录公众平台，进入开发者中心可设置）
# 接收微信支付异步通知回调地址，通知url必须为直接可访问的url，不能携带参数。

APPID = 'wx3b91147491e66093'
MCHID = '1269456201'
KEY = 'e10adc3949ba59abbe56e057f20f883e'
APPSECRET = 'a4cc64686882ffc0b03b7b0adf547399'

NOTIFY_URL = ''
