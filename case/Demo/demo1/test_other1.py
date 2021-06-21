# coding=utf-8
import pytest
import allure
from lib import mysql
from case.base import TestBase


@allure.feature('测试初始化全局数据')
@allure.link(url="https://pages/viewpage.action?pageId=84191585", name="测试用例")
@pytest.mark.usefixtures("init_module_data")
class TestOther1(TestBase):
    @allure.story("1.第一步")
    def test_step_one(self, request):
        print('test step one in TestOther1...done')
        l = ['34234', 'sfsdfsf', '98u909i']
        request.config.cache.set('just_key', l)
