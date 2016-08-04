# coding:utf8

import datetime
import hashlib
import json
import time
import traceback

import httplib2

from k_show_app.common.cache_type import CacheType
from k_show_app.service.base import BaseService
from k_show_app.util import cf
from k_show_app.util import httpClient
from k_show_app.util.random_util import random_string
from k_show_app.util.redisclient import redisCache


class WechatService(BaseService):
    def __init__(self):
        super(WechatService, self).__init__()
        self.appid = cf.get('WECHAT', 'appid')    # 'wx3b91147491e66093'
        self.appsecret = cf.get('WECHAT', 'appSecret')    # 'a4cc64686882ffc0b03b7b0adf547399'
        self.host = 'api.weixin.qq.com'
        self.access_token_url = 'https://%s/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' \
                                % (self.host, self.appid, self.appsecret)

    def get_wechat_userinfo(self, code):
        oauth_token_url = 'https://%s/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code' % \
                    (self.host, self.appid, self.appsecret, code)
        oauth_token = httpClient.get_data(oauth_token_url)
        access_token = oauth_token['access_token']
        openid = oauth_token['openid']

        key = 'wechat_userinfo_%s' % openid
        userinfo = redisCache.get(key)
        if userinfo is None:
            userinfo_url = 'https://%s/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN' % \
                           (self.host, access_token, openid)
            userinfo = httpClient.get_data(userinfo_url)
            if userinfo:
                # 设置缓存
                redisCache.set(key, userinfo, CacheType.ONE_DAY)
        return userinfo

    def get_jssdk_config_dict(self, url):
        """
        获取调用微信jssdk需要的配置信息
        """
        key = 'jssdk_config_dict_' + url
        config_info = redisCache.get(key)
        if config_info is None:
            # 改为从公共服务器去获取
            jsapi_ticket = self.get_current_js_ticket()
            noncestr = random_string(10)
            timestamp = int(time.time())
            string1 = 'jsapi_ticket=' + jsapi_ticket + '&noncestr=' + noncestr + \
                      '&timestamp=' + str(timestamp) + '&url=' + url
            # 得到签名
            signature = hashlib.sha1(string1.encode()).hexdigest()
            config_info = {'appId': self.appid, 'timestamp': timestamp, 'nonceStr': noncestr, 'signature': signature}
            redisCache.set(key, config_info, CacheType.ONE_DAY)
        return config_info

    def get_current_access_token(self):
        # 从公共服务器去获取
        access_token = ''
        token_url = cf.get('WECHAT_TOKEN', 'token_url')
        token_host = cf.get('WECHAT_TOKEN', 'host')
        access_token_dict = httpClient.get_data(token_url, {'Host': token_host})
        if 'access_token' in access_token_dict:
            access_token = access_token_dict['access_token']
            self.logger.debug('get access_token:%s' % access_token)
        return access_token

    def get_current_js_ticket(self):
        # 从公共服务器去获取js ticket
        ticket = ''
        js_token_url = cf.get('WECHAT_TOKEN', 'js_token_url')
        token_host = cf.get('WECHAT_TOKEN', 'host')
        ticket_dict = httpClient.get_data(js_token_url, {'Host': token_host})
        if 'ticket' in ticket_dict:
            ticket = ticket_dict['ticket']
        return ticket

    def get_access_token(self):
        http = httplib2.Http()
        response, content = http.request(self.access_token_url, 'GET')
        response_time = response['date']
        access_token = None
        content_json = ''
        refresh_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            content_json = json.loads(content)
            access_token = content_json['access_token']
        except Exception as e:
            self.logger.error(traceback.format_exc() + str(content_json))
        return access_token, response_time, refresh_time

    def get_jsapi_ticket(self):
        jsapi_ticket = ''
        access_token = self.get_access_token()[0]
        jsapi_ticket_url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?' \
                           'access_token=%s&type=jsapi' % access_token

        ticket_dict = httpClient.get_data(jsapi_ticket_url)
        if ticket_dict and 'ticket' in ticket_dict:
            jsapi_ticket = ticket_dict['ticket']
        return jsapi_ticket

    def get_get_media_url(self, media_id):
        """
        得到获取媒体文件的url
        @param media_id
        """
        access_token = self.get_current_access_token()
        media_get_url = 'https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s' \
                        % (access_token, media_id)
        return media_get_url

    def get_qrcode_url(self, scene_id):
        """
        获取创建的二维码请求url
        @param scene_id int
        """
        access_token = self.get_current_access_token()
        get_ticket_url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s' % access_token
        body = "{'action_name': 'QR_LIMIT_SCENE', 'action_info': {'scene': {'scene_id': ' + str(scene_id) + '}}}"
        json_obj = httpClient.get_response_data(get_ticket_url, body, 'POST', None, True, False)
        ticket = json_obj['ticket']
        qrcode_url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s' % ticket
        return qrcode_url

    def batchget_material(self, m_type, offset=0, count=10):
        """
        根据类型获取素材列表
        @param m_type 素材类型.素材的类型，图片（image）、视频（video）、语音 （voice）、图文（news）
        @param offset 起始位置
        @param count 素材数量。1-20
        """
        access_token = self.get_current_access_token()
        url = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s' % access_token
        body = "{'type' : '%s', 'offset' : %s, 'count' : %s}" % (m_type, offset, count)
        json_obj = httpClient.get_response_data(url, body, 'POST', None, True, False)
        return json_obj
