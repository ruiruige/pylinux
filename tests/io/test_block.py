# /usr/bin/env python
# coding=utf-8
import unittest

# noinspection PyUnresolvedReferences
from .. import context
from pylinux.io.block import parse_lsblk_output


class TestBlock(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        必须使用@classmethod 装饰器,所有test运行前运行一次
        :return:
        """
        print('setUpClass')

    def setUp(self):
        """
        每个测试用例执行之前做操作
        :return:
        """
        print('setUp')

    def tearDown(self):
        """
        每个测试用例执行之后做操作
        :return:
        """
        self.config_file = None
        print('tearDown')

    def test_block(self):
        text = """
xvda             250G disk
xvda1 ext4     250G part /
xvdb    ext4    1000G disk /home/username/name/1.1.1.1
xvdc    ext4    1000G disk /home/username/name/1.1.1.1/folder_name
"""
        print parse_lsblk_output(text)


if __name__ == '__main__':
    unittest.main()
