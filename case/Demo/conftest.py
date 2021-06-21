# coding=utf-8
import os

import pytest
import time
import logging
import sys
from lib import mysql
from lib import redis_helper
from lib import rd_platform


# 获取参数
@pytest.fixture(scope='module')
def cluster(request):
    if request.config.getoption('--cluster'):
        print('cluster mode')
    else:
        print('single mode')


# # 各个数据库的连接
# @pytest.fixture(scope="module")
# def warebusiness():
#     db = mysql.Mysql("warebusiness")
#     yield db
#     db.close()
#
#
# @pytest.fixture(scope="module")
# def warebase():
#     db = mysql.Mysql("warebase")
#     yield db
#     db.close()
#
#
# # redis连接
# @pytest.fixture()
# def redis():
#     redis_obj = redis_helper.Redis().get_redis()
#     return redis_obj


# 数据初始化，每次测试初始化一次，自动调用
@pytest.fixture(scope="session", autouse=True)
def init_global_data():
    print("init global data....done.")


# 数据初始化，每个module初始化一次
@pytest.fixture(scope="session")
def init_module_data():
    print("init module data...done")


@pytest.fixture(scope="module")
def init_module_data1():
    print("init module data1...done")


# 数据初始化，每个模块（每个py文件）初始化一次
@pytest.fixture(scope="module")
def init_data(warebase, common_data):
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data/testdata.txt") as f:
        for line in f:
            print(line)


# # 研发平台接口封装
# @pytest.fixture(scope='module')
# def rd_platform():
#     return rd_platform.RdPlatform()
#
#
# # 数据库清理
# @pytest.fixture(scope="module")
# def clear_data(warebase, common_data):
#     logging.debug("------------clear data--------------")
#     sql_list = [
#         'delete from warebase.container_stock where 1=1',
#         'delete from warebase.container_stock_freeze where 1=1',
#         'delete from warebase.region_stock where 1=1',
#         'delete from warebase.region_stock_freeze where 1=1',
#         'delete from warebase.house_stock where 1=1',
#         'delete from warebase.house_stock_freeze where 1=1',
#         "delete from warebase.container where container_type=24 and container_code='%s'" % common_data['containerID']
#     ]
#     for sql in sql_list:
#         logging.debug(f"delete sql: {sql}")
#         warebase.delete(sql)
#
#
# @pytest.fixture(scope='module')
# def restart_server_before_test(rd_platform):
#     # 重建mysql服务，相当于初始化
#     res = rd_platform.recreate_service('mysql')
#     if res != 'succ':
#         exit(1)
#     # 重启sim-device-common服务
#     res = rd_platform.restart_service('sim-device-common')
#     if res != 'succ':
#         exit(1)
#
#
# # 测试case都要用到的一些数据
# @pytest.fixture(scope='module')
# def common_data():
#     time_stamp = str(int(time.time()))
#     data = dict()
#     data['warehouseID'] = '248653306480558994'
#     data['regionID'] = '123456'
#     data['stationID'] = '249930691024846851'
#     data['outOrderID'] = 'TEST201900505' + time_stamp
#     data['containerID'] = "zx" + time_stamp
#     data['skuID'] = '249945655462592515'
#     data['skuName'] = '1001清风抽纸200抽*2层'
#     data['skuCode'] = '1001'
#     return data
