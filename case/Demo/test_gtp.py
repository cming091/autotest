# coding=utf-8
import pytest
import os
import sys
import allure
import logging
from utils import cfg
from case.base import TestBase

@allure.feature("整托入库流程")
@allure.link(url="https://pages/viewpage.action?pageId=84191585", name="测试用例")
@pytest.mark.usefixtures("clear_data")
class TestGTP10(TestBase):
    url_base = cfg.G_CONFIG_DICT['base.url_base']

    @allure.story("1.添加订单")
    def test_add_order(self, request, common_data, warebusiness, rd_platform):
        logging.debug(f"--------------------------------------------- begin {sys._getframe().f_code.co_name} ---------------------------------------------")

        with allure.step("请求接口"):
            url = self.url_base + '/warebusiness/api/businessflow/addBusinessFlow'
            containerBusinessFlowDetail = '[{"containerID":"%s","skuList":[{"skuID":"%s","num":20,"totalNum":2000,"expireTime":0}]}]' % (common_data['containerID'], common_data['skuID'])
            data = {
                "warehouseID": common_data['warehouseID'],
                "regionID": common_data['regionID'],
                "businessFlowType": 1,
                "businessFlowSubType": 3,
                "outOrderID": common_data['outOrderID'],
                "businessFlowFinishMode": 1,
                "containerBusinessFlowDetail": containerBusinessFlowDetail
            }
            r = self.post(url, data)
            logging.debug(f"url: {url}, data: {data}, status_code: {r.status_code}, res: {r.json()}")

            # 判断返回结果
            assert r.status_code == 200
            resp_data = r.json()
            assert resp_data['returnCode'] == 0
            assert resp_data['returnMsg'] == 'succ'
            assert resp_data['data'] is not None

        with allure.step("验证warebusiness库，business_flow应添加一条记录"):
            businessFlowID = resp_data['data']['businessFlowID']
            sql = 'select * from business_flow where business_flow_id={}'.format(businessFlowID)
            # print(sql)
            result = warebusiness.query(sql)
            logging.debug(f"sql: {sql}, num of result: {len(result)}")
            assert len(result) == 1

        # 重启wareplatform服务
        rd_platform.restart_service('wareplatform')

        # 停止wareplatform服务
        rd_platform.stop_service('wareplatform')

        # 启动wareplatform服务
        rd_platform.start_service('wareplatform')

        # 重建mysql服务
        rd_platform.recreate_service('mysql')

        with allure.step("验证warebusiness库中，container_business_flow_detail表中，是否添加了对应business_flow_id和container_id的记录"):
            sql = "select * from container_business_flow_detail where business_flow_id='{}' and container_id='{}'".format(businessFlowID, common_data['containerID'])
            result = warebusiness.query(sql)
            logging.debug(f"sql: {sql}, num of result: {len(result)}")
            assert len(result) == 1

        with allure.step("将businessFlowID存入缓存"):
            logging.debug(f"businessFlowID: {businessFlowID}")
            request.config.cache.set("gtp1.0.businessFlowID", businessFlowID)

    @allure.story("2.入库")
    def test_init_inbound(self, request, common_data, warebusiness):
        logging.debug(f"--------------------------------------------- begin {sys._getframe().f_code.co_name} ---------------------------------------------")
        url = self.url_base + "/warelogic/api/inboundWhole/initInbound"
        data = {
            "warehouseID": common_data['warehouseID'],
            "stationID": common_data['stationID'],
            "businessFlowID": request.config.cache.get("gtp1.0.businessFlowID", None)
        }

        r = self.post(url, data)
        logging.debug(f"url: {url}, data: {data}, status_code: {r.status_code}, res: {r.json()}")

        assert r.status_code == 200
        resp_data = r.json()
        print(resp_data)
        assert resp_data['returnCode'] == 0
        assert resp_data['data'] is not None

        workOrderID = resp_data['data']['workOrderID']
        sql = 'select * from business_work_order where work_order_id={}'.format(workOrderID)
        result = warebusiness.query(sql)
        assert len(result) == 1

    @allure.story("3.查询订单列表")
    def test_query_b_flow_list(self, common_data):
        logging.debug(f"--------------------------------------------- begin {sys._getframe().f_code.co_name} ---------------------------------------------")
        url = self.url_base + '/warelogic/api/inboundWhole/queryBFlowList'
        params = {
            'warehouseID': common_data['warehouseID'],
            "stationID": common_data['stationID']
        }

        r = self.get(url, params)
        logging.debug(f"url: {url}, data: {params}, status_code: {r.status_code}, res: {r.json()}")

        assert r.status_code == 200

    @allure.story("4.查询订单详细信息")
    def test_query_b_flow_detail(self, request, common_data):
        logging.debug(f"--------------------------------------------- begin {sys._getframe().f_code.co_name} ---------------------------------------------")
        url = self.url_base + '/warelogic/api/inboundWhole/queryBFlowDetail'
        params = {
            "warehouseID": common_data['warehouseID'],
            "stationID": common_data['stationID'],
            "businessFlowID": request.config.cache.get("gtp1.0.businessFlowID", None),
            "code": common_data['containerID']
        }

        r = self.get(url, params)
        logging.debug(f"url: {url}, data: {params}, status_code: {r.status_code}, res: {r.json()}")
        assert r.status_code == 200
        resp_data = r.json()
        # print(resp_data)
        assert resp_data['returnCode'] == 0
        assert resp_data['data'] is not None
        assert len(resp_data['data']['inboundDetail']) == 1
        assert resp_data['data']['inboundDetail'][0]['skuCode'] == common_data['skuCode']
        assert resp_data['data']['inboundDetail'][0]['skuName'] == common_data['skuName']

    @allure.story("5.入库确认")
    def test_confirm(self, request, common_data):
        logging.debug(f"--------------------------------------------- begin {sys._getframe().f_code.co_name} ---------------------------------------------")
        url = self.url_base + '/warelogic/api/inboundWhole/confirm'
        data = {
            "warehouseID": common_data['warehouseID'],
            "stationID": common_data['stationID'],
            "businessFlowID": request.config.cache.get("gtp1.0.businessFlowID", None),
            "code": common_data['containerID']
        }

        r = self.post(url, data)
        logging.debug(f"url: {url}, data: {data}, status_code: {r.status_code}, res: {r.json()}")

        assert r.status_code == 200
        resp_data = r.json()
        assert resp_data['returnCode'] == 0
        assert resp_data['data'] is not None
        assert resp_data['data']['isLastFrame'] == 1

