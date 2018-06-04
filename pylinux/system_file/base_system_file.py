# /usr/bin/env python
# coding=utf-8
from pylinux.common.file_config.file_config import FileConfig
from pylinux.common.modifier.base_modifier import BaseModifier
from pylinux.common.searcher.base_searcher import BaseSearcher


class BaseSystemFile(object):
    """
    系统文件的基类
    """

    def __init__(self, filepath, searcher=BaseSearcher, modifier=BaseModifier, file_config=FileConfig()):
        self.filepath = filepath
        self.lines = []
        self.load()

        self.searcher = searcher(self.lines, file_config=file_config)
        self.modifier = modifier(self.lines, file_config=file_config)

    def load(self):
        """
        载入文件
        """
        with open(self.filepath, "rb") as f:
            self.lines = f.readlines()

    def flush(self):
        with open(self.filepath, "wb") as f:
            f.writelines(self.lines)

    def get_setting(self, name):
        return self.searcher.get_setting(name)

    def setting_exists(self, name):
        return self.searcher.setting_exists(name)

    def set_setting(self, name, value):
        occurrence = self.searcher.get_setting_occurrence(name)
        if occurrence:
            self.modifier.add_setting(name, value)
        else:
            self.modifier.update_setting(name, value)
