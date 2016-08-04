# encoding: utf-8

import time


# 文本消息
TEXT = """
    <xml>
    <ToUserName><![CDATA[{toUser}]]></ToUserName>
    <FromUserName><![CDATA[{fromUser}]]></FromUserName>
    <CreateTime>{createTime}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{content}]]></Content>
    </xml>"""


# 图片消息
IMAGE = """
    <xml>
    <ToUserName><![CDATA[{toUser}]]></ToUserName>
    <FromUserName><![CDATA[{fromUser}]]></FromUserName>
    <CreateTime>{createTime}</CreateTime>
    <MsgType><![CDATA[image]]></MsgType>
    <Image>
    <MediaId><![CDATA[{media_id}]]></MediaId>
    </Image>
    </xml>"""


# 单条图文，必须放入NEWS中
ITEM = """
    <item>
    <Title><![CDATA[{title}]]></Title> 
    <Description><![CDATA[{description}]]></Description>
    <PicUrl><![CDATA[{picurl}]]></PicUrl>
    <Url><![CDATA[{url}]]></Url>
    </item>"""


# 图文消息
NEWS = """
    <xml>
    <ToUserName><![CDATA[{toUser}]]></ToUserName>
    <FromUserName><![CDATA[{fromUser}]]></FromUserName>
    <CreateTime>{createTime}</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>{counts}</ArticleCount>
    <Articles>
    {items}
    </Articles>
    </xml> """


class MsgTpl(object):
    """
    微信别动消息回复模板
    """
    fromUser = 'aamopen'

    @staticmethod
    def get_text(openid, content):
        """
        获取文本消息
        @param openid 接收人openid
        @param content 内容
        """
        data_dict = {'toUser': openid, 'fromUser': MsgTpl.fromUser, 'content': content, 'createTime': int(time.time())}
        return TEXT.format(**data_dict)

    @staticmethod
    def get_image(openid, media_id):
        """
        获取图片消息
        @param openid 接收人openid
        @param media_id
        """
        data_dict = {'toUser': openid, 'fromUser': MsgTpl.fromUser, 'media_id': media_id, 'createTime': int(time.time())}
        return IMAGE.format(**data_dict)


if __name__ == '__main__':
    print(MsgTpl.get_text('asjfjas', u'欢迎关注'))