# coding=utf-8
import logging

import pytest
import allure

from case.base import TestBase


@allure.feature('测试初始化全局数据')
@allure.link(url="https://pages/viewpage.action?pageId=84191585", name="测试用例")
@pytest.mark.usefixtures("init_module_data", "init_module_data1")
@pytest.mark.usefixtures("cluster")
class TestOther2(TestBase):
    """test other 2"""
    @allure.story("1.第一步")
    def test_step_one(self, request):
        logging.debug('this is a failed test')
        assert 1 == 2

