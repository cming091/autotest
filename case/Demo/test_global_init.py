# coding=utf-8
import pytest
import allure

from case.base import TestBase


@allure.feature('测试初始化全局数据')
@allure.link(url="https://pages/viewpage.action?pageId=84191585", name="测试用例")
@pytest.mark.usefixtures("init_module_data")
@pytest.mark.usefixtures("init_global_data")
class TestGlobalDataInit(TestBase):
    """test global data init"""
    @allure.story("1.第一步")
    def test_step_one(self, request):
        print('test step one...done')

    def test_step_two(self, request):
        print('test step two...done')
        assert 1 == 2

    def test_step_three(self, request):
        print('test step three... done')
