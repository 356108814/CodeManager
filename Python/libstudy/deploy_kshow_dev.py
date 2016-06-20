# encoding: utf-8
"""
部署kshow外网测试环境
@author Yuriseus
@create 2016-6-20 14:38
"""
import os
from auto_deploy import AutoDeploy


class DeployKShow(AutoDeploy):
    def __init__(self):
        super(DeployKShow, self).__init__()

    def init_config(self):
        self.src_dir = '/workspace/continuous/kshow_weixin_intranet/'
        self.dst_dir = '/workspace/continuous/kshow_weixin_internet_dev/'

    def modify_file(self):
        js_path = os.path.join(self.dst_dir, 'web_frontend/static/js/kshow_1.0.js')
        setting_path = os.path.join(self.dst_dir, 'kshow_server/settings/setting.py')
        # 修改kshow.js的apiUrl
        self.replace_in_file(js_path, ['http://172.16.2.102/kshow/api/'], ['http://dev.corp.weixin.meda.cc/api/'])
        # 修改setting.py的CONF
        self.replace_in_file(setting_path, ['DEBUG = True', 'settings/config_intranet.conf'],
                             ['DEBUG = False', 'settings/config_kshow.conf'])

    def restart_server(self):
        cd_path = '/usr/local/tengine-2.1.2/html/kshow_weixin'
        cmds = [
            'svn update',
            'supervisorctl restart kshow_weixin_server'
        ]
        self.shell.run_after_cd_path(cd_path, cmds)


if __name__ == '__main__':
    deploy_kshow = DeployKShow()
    deploy_kshow.deploy()
