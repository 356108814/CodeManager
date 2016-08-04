# encoding: utf-8

from k_show_app.util.xml_util import XmlUtil


class MsgHandler(object):
    """
    普通消息处理器
    """
    def __init__(self):
        self._xml = None
        self._xml_dict = None
        self._to_user = None
        self._msg_type = None

    def init_data(self, xml):
        """
        @param xml 微信推送过来的xml字符串
        初始化数据，在进行handler之前必须先初始化
        """
        self._xml = xml
        self._xml_dict = XmlUtil.get_dict_from_xml(self._xml)
        # 接受消息的用户openid
        self._to_user = self._xml_dict["FromUserName"]
        # 消息类型，如文本消息text
        self._msg_type = self._xml_dict['MsgType']

    def handler(self):
        """
        消息处理入口
        @return 符合微信要求格式的字符串。xml格式
        """
        return 'success'


msgHandler = MsgHandler()


if __name__ == '__main__':
    pass