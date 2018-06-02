# /usr/bin/env python
# coding=utf-8
from pylinux.system_file.base_system_file import BaseSystemFile
from pylinux.exception.name_not_valid_exception import NameNotValidException
from pylinux.exception.setting_not_valid_exception import SettingNotValidException


class RcLocal(BaseSystemFile):
    """
    rc.local的配置文件类
    """

    def __init__(self, filepath):
        super(RcLocal, self).__init__(filepath)

    def add_boot_item(self, cmd, name):
        """
        增加启动项
        :param name:
        :param cmd:
        """
        if not name:
            raise NameNotValidException("name not valid while adding boot item")

        if not cmd:
            raise SettingNotValidException("setting not valid while adding boot item")

    def add_multi_line_setting(self, name, value):
        pass
