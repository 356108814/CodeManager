# encoding: utf-8

from .msg_tpl import MsgTpl
from k_show_app.util import httpClient
from k_show_app.util.xml_util import XmlUtil
from k_show_app.util.log import Logger


SUBSCRIBE = 'subscribe'

# 取消订阅
UNSUBSCRIBE = 'unsubscribe'

# 扫描带参数二维码事件，用户已关注时的事件推送
SCAN = 'SCAN'

# 地理位置上报
LOCATION = 'LOCATION'

# 自定义菜单事件
CLICK = 'CLICK'

# 点击菜单跳转链接时的事件推送
VIEW = 'VIEW'


class EventHandler(object):
    """
    事件处理器
    """
    def __init__(self):
        self.xml = None
        self.xml_dict = None
        self.to_user = None
        self.msg_type = None
        self.event = None
        self.event_key = None

    def init_data(self, xml):
        """
        @param xml 微信推送过来的xml字符串
        初始化数据，在进行handler之前必须先初始化
        """
        self.xml = xml
        self.xml_dict = XmlUtil.get_dict_from_xml(self.xml)
        # 接受消息的用户openid
        self.to_user = self.xml_dict["FromUserName"]
        self.msg_type = self.xml_dict['MsgType']
        # 具体事件类型。如subscribe
        self.event = self.xml_dict['Event']
        # 事件KEY值
        self.event_key = None
        if self.xml_dict.has_key('EventKey'):
            self.event_key = self.xml_dict['EventKey']

    def handler(self):
        """
        事件处理入口
        @return 符合微信要求格式的字符串。xml格式
        """
        if self.event == SUBSCRIBE:
            return self.subscribe()
        elif self.event == SCAN:
            return self.scan()
        elif self.event == CLICK:
            return self.menu_click() 
        elif self.event == LOCATION:
            return self.report_location() 
        return 'success'

    def subscribe(self):
        """关注"""
        # if self.event_key is not None:
        #     # 未关注公共号就扫描
        #     content = u'欢迎关注公众号，检测到你扫艾美用户的二维码名片，请先绑定艾美账号再扫码，即可关注其他用户'
        # else:
        #     content = u'欢迎关注公众号，请点击“我的”按钮，按照提示绑定微信账户与艾美账户'
        #
        # return MsgTpl.get_text(self.to_user, content)

    def scan(self):
        """
        用户扫描了参数二维码。转发请求。
        """
        # scene_id = int(self.event_key)
        # url = "http://corp.weixin.meda.cc/follow/add/"
        # content = httpUtil.get_response_data(url, self.xml, 'POST', None, False)

        # return MsgTpl.get_text(self.to_user, content)

    def menu_click(self):
        """点击菜单处理"""
        # media_id = ''
        # kshow_qrcode_media_id = 'CunMEWDnbl4qvmJaXWDslCvSRzdNswOy7cAaExTYz08'
        # minik_qrcode_media_id = 'Og4KkuB2R4QVJzHl49JnvdXzMSslWEGnFQWn1msjPD0'
        # e5_qrcode_media_id = 'Og4KkuB2R4QVJzHl49Jnvf2zFCB3IyFVM5aDbh_CVmw'
        # # kf_qrcode_media_id = 'Og4KkuB2R4QVJzHl49JnvbpqOMTBZ3mW4Tky3DCo00s'
        # if self.event_key == 'menu_kshow_mp':
        #     media_id = kshow_qrcode_media_id
        # elif self.event_key == 'menu_minik_mp':
        #     media_id = minik_qrcode_media_id
        # elif self.event_key == 'menu_e5_mp':
        #     media_id = e5_qrcode_media_id
        # elif self.event_key == 'menu_kefu':
        #     content = u'客服：188 1887 3126\n销售：137 1134 0791\n官网：www.meda.cc'
        #     return MsgTpl.get_text(self.to_user, content)
        # return MsgTpl.get_image(self.to_user, media_id)

    def report_location(self):
        """上报地理位置"""
        openid = self.xml_dict['FromUserName']
        longitude = self.xml_dict['Longitude']    # 地理位置经度
        latitude = self.xml_dict['Latitude']      # 地理位置纬度
        precision = self.xml_dict['Precision']    # 地理位置精度
        location_dict = {'openid': openid}
        log = 'openid={openid}&longitude={longitude}&latitude={latitude}&country={country}&' \
              'province={province}&city={city}'.format(**location_dict)
        Logger.info(log)
        return 'success'


eventHandler = EventHandler()

if __name__ == '__main__':
    pass
