# /usr/bin/env python
# coding=utf-8

import unittest
import context

from pylinux.system_file.base_system_file import BaseSystemFile


class BaseSystemFileTestCase(unittest.TestCase):
    test_fp = None

    @classmethod
    def setUpClass(cls):
        BaseSystemFileTestCase.test_fp = context.get_test_abs_filepath("base_system_file.test")

    @classmethod
    def tearDownClass(cls):
        BaseSystemFileTestCase.test_fp = None

    def setUp(self):
        self.base_system_file = BaseSystemFile(BaseSystemFileTestCase.test_fp)

    def tearDown(self):
        self.base_system_file = None

    def test_no_comment(self):
        """
        验证一个配置项在没有注释情况下是否能成功
        :return:
        """
        name = "test_no_comment"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_error_comment(self):
        """
        验证一个配置项在错误注释情况下是否能成功
        应该是能成功的，注释被忽略
        :return:
        """
        name = "test_error_comment"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_correct_name(self):
        """
        验证happy path
        :return:
        """
        name = "test_correct_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_left_space_name(self):
        """
        验证一个配置项在 左侧有空白的情况下是否能成功
        :return:
        """
        name = "test_left_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_right_space_name(self):
        """
        验证一个配置项在 右侧有空白的情况下是否能成功
        :return:
        """
        name = "test_right_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_both_space_name(self):
        """
        验证一个配置项在 双侧有空白的情况下是否能成功
        :return:
        """
        name = "test_both_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)

    def test_connector_space_name(self):
        """
        验证一个配置项在 连接符附近有空白的情况下是否能成功
        :return:
        """
        name = "test_connector_space_name"
        expected = name + "_value"
        value = self.base_system_file.get_setting(name)
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main()
