import json

import requests
import logging
from utils import cfg


class Simulator:
    def __init__(self):
        self.url_base = 'http://' + cfg.G_CONFIG_DICT['simulator.host'] + '/sim-device-common'
        # 集群环境本地运行
        # self.url_base = 'http://' + cfg.G_CONFIG_DICT['simulator.host']

        self.headers = {'Content-Type': 'application/json'}

    # 创建机器人
    def batch_create(self, data):
        url = self.url_base + '/sim/batchCreate'
        # print(url)
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f'simulator batch_create error, {res_data}')
            else:
                logging.error(f'simulator batch_create error, http response code is {r.status_code}')
        except Exception as e:
            logging.error(f'simulator batch_create error, {e}')
        return result

    # 下线机器人
    def offline(self, data):
        url = self.url_base + '/sim/offline'
        # print(url)
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f'simulator batch_create error, {res_data}')
            else:
                logging.error(f'simulator batch_create error, http response code is {r.status_code}')
        except Exception as e:
            logging.error(f'simulator batch_create error, {e}')
        return result

    # 上线机器人 （分为简单/复杂的上线，区别是是否带robotAttr信息）
    def online(self, data):
        url = self.url_base + '/sim/online'
        # print(url)
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f'simulator batch_create error, {res_data}')
            else:
                logging.error(f'simulator batch_create error, http response code is {r.status_code}')
        except Exception as e:
            logging.error(f'simulator batch_create error, {e}')
        return result

    # 设置状态异常（覆盖设置）
    def setErrorState(self, data):
        url = self.url_base + '/sim/setErrorState'
        # print(url)
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f'simulator batch_create error, {res_data}')
            else:
                logging.error(f'simulator batch_create error, http response code is {r.status_code}')
        except Exception as e:
            logging.error(f'simulator batch_create error, {e}')
        return result

    # 更新模拟器配置
    def update_config(self, data):
        url = self.url_base + '/config/update'
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f"simulator update config error, {res_data}")
            else:
                logging.error(f"simulator update config error, http response code is {r.status_code}")
        except Exception as e:
            logging.error(f"simulator update config error, {e}")
        return result

    # 添加机械臂设备
    def add_device(self, data):
        url = cfg.G_CONFIG_DICT['base.url_base'] + '/hub-center/device/add'
        result = 'fail'
        try:
            r = requests.post(url=url, data=data, headers=self.headers)
            if r.status_code == 200:
                res_data = r.json()
                if res_data['returnCode'] == 0:
                    result = 'succ'
                else:
                    logging.error(f"add device error, {res_data}")
            else:
                logging.error(f"add device error, http response code is {r.status_code}")
        except Exception as e:
            logging.error(f"add device error, {e}")
        return result



# if __name__ == "__main__":
#     import os
#
#     root_path = os.path.dirname(os.path.dirname(__file__))
#     cfg_path = os.path.join(root_path, './conf/config.ini')
#     cfg.load_cfg(cfg_path)
#
#     sim = Simulator()
#
#     data = {
#         "simList": [
#             {
#                 "deviceConfID": "0",
#                 "deviceSN": "850809707888978",
#                 "curX": 500,
#                 "curY": 2500,
#                 "mapID": 1,
#                 "ucPower": 100,
#                 "curDir": 0,
#                 "frameId": "65535",
#                 "liftState": 0
#             },
#             {
#                 "deviceConfID": "0",
#                 "deviceSN": "850809707888977",
#                 "curX": 500,
#                 "curY": 3500,
#                 "mapID": 1,
#                 "ucPower": 100,
#                 "curDir": 0,
#                 "frameId": "65535",
#                 "liftState": 0
#             }
#         ]
#     }
#     res = sim.batch_create(data=json.dumps(data))
#     print(res)
