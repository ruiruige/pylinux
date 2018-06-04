# /usr/bin/env python
# coding=utf-8
from pylinux.common.file_config.file_config import FileConfig


class LineSettingModifier(object):

    def __init__(self, lines, file_config=FileConfig()):
        self.initial_lines = lines
        self.file_config = file_config

    def add_setting(self, name, value):
        pass

    def update_setting(self, name, value):
        pass