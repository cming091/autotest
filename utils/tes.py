import json

import requests
import logging
from utils import cfg


def register(warehouse_name):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/api/warehouse/register'
    result = 'fail'
    warehouseID = ''
    try:
        data = {
            'userID': "111",
            'warehouseName': warehouse_name,
            'length': 1000,
            'width': 1000
                }
        r = requests.post(url=url, data=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'register success, {res_data}')
                warehouseID = res_data['data']['warehouseID']
            else:
                logging.error(f'register error, {res_data}')
        else:
            logging.error(f'register error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'register error, {e}')
    return result, warehouseID


def register_warebasic(warehouse_name,warehouseID,warehouseCode):
    url = cfg.G_CONFIG_DICT['base.url_base'] + ':8000/wes/warebasic/warehouse/registerWarehouse'
    result = 'fail'
    try:
        data = {
            'warehouseID': warehouseID,
            'warehouseName': warehouse_name,
            'warehouseCode': warehouseCode,
                }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'register success, {res_data}')
            else:
                logging.error(f'register_warebasic error, {res_data}')
        else:
            logging.error(f'register_warebasic error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'register_warebasic error, {e}')
    return result

def upload(file_path):
    url = cfg.G_CONFIG_DICT['base.url_base'] + ':81/upload'
    result = 'fail'
    file_url = ''
    md5 = ''
    try:
        data = {'file': open(file_path, 'rb')}
        r = requests.post(url=url, files=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'upload success, {res_data}')
                file_url = res_data['data']['url']
                md5 = res_data['data']['md5']
            else:
                logging.error(f'upload error,data: {data} res: {res_data}')
        else:
            logging.error(f'upload error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'upload error, {e}')
    return result, file_url, md5


def import_wareservice(md5,fileName,fileURL,warehouseID):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/api/warehouse/importByURL'
    result = 'fail'
    try:
        data = {
            'clearNodeTypeIndex': 1,
            'clearAllFrame': 1,
            'clearNodeTypeInsulate': 1,
            'md5': md5,
            'fileName': fileName,
            'fileURL': fileURL,
            'importType': 'COVER',
            'userName': 'admin',
            'warehouseID': warehouseID
                }
        r = requests.post(url=url, data=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'import wareservice success, {res_data}')
            else:
                logging.error(f'import wareservice error, {res_data}')
        else:
            logging.error(f'import wareservice error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'import wareservice error, {e}')
    return result


def import_wareservice_915(md5,fileName,fileURL,warehouseID,regionType,regionName):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/api/warehouse/importByURL'
    result = 'fail'
    try:
        data = {
            'regionType':regionType,
            'regionName':regionName,
            'clearNodeTypeIndex': 0,
            'clearAllFrame': 0,
            'clearNodeTypeInsulate': 0,
            'md5': md5,
            'fileName': fileName,
            'fileURL': fileURL,
            'importType': 'COVER',
            'userName': 'admin',
            'warehouseID': warehouseID
                }
        r = requests.post(url=url, data=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'import wareservice success, {res_data}')
            else:
                logging.error(f'import wareservice error, {res_data}')
        else:
            logging.error(f'import wareservice error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'import wareservice error, {e}')
    return result

def import_warebase(fileName,fileURL,warehouseID):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/warebase/api/warehouse/initWarehouseByUrl'
    result = 'fail'
    try:
        data = {
            'warehouseName': fileName,
            'fileURL': fileURL,
            'warehouseID': warehouseID
                }
        r = requests.post(url=url, data=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'import warebase success, {res_data}')
            else:
                logging.error(f'import warebase error, {res_data}')
        else:
            logging.error(f'import warebase error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'import warebase error, {e}')
    return result


def import_warebasic(warehouseCode,regionCode,regionName,regionType,fileURL):
    url = cfg.G_CONFIG_DICT['base.url_base'] + ':8000/wes/warebasic/warehouse/importMapByFileUrl'
    result = 'fail'
    try:
        data = {
            'warehouseCode': warehouseCode,
            'regionCode': regionCode,
            'regionName': regionName,
            'regionType': regionType,
            'fileUrl': fileURL
                }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=url, headers = headers, data=json.dumps(data))
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'import warebasic success, {res_data}')
            else:
                logging.error(f'import warebasic error, {res_data}')
        else:
            logging.error(f'import warebasic error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'import warebasic error, {e}')
    return result


def set_warehouse_sn(warehouse_id, sn_type, robot_id, sn):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/api/warehouse/setWarehouseSNInfo'
    print(f"---------------------------------{url}---------------------------------")
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = f'warehouseID={str(warehouse_id)}&snType={str(sn_type)}&robotID={str(robot_id)}&sn={str(sn)}'
    result = 'fail'
    try:
        r = requests.post(url=url, data=data, headers=headers)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'set warehouse sn success, {res_data}')
            else:
                logging.error(f'set warehouse sn error, {res_data}')
        else:
            logging.error(f'set warehouse sn error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'set warehouse sn error, {e}')
    return result


def multi_add_pod(warehouse_id, pod_info):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/apiv2/multiAddPod'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = f'warehouseID={warehouse_id}&podInfo={pod_info}'
    result = 'fail'
    try:
        r = requests.post(url=url, data=data, headers=headers)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
            else:
                logging.error(f'multi add pod error, {res_data}')
        else:
            logging.error(f'multi add pod error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'multi add pod error, {e}')
    return result


def multi_add_pod_815(warehouse_id, pod_info, request_id, client_code):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/apiv2/multiAddPod'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = f'warehouseID={warehouse_id}&podInfo={pod_info}&requestID={request_id}&clientCode={client_code}'
    result = 'fail'
    try:
        r = requests.post(url=url, data=data, headers=headers)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
            else:
                logging.error(f'multi add pod error, {res_data}')
        else:
            logging.error(f'multi add pod error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'multi add pod error, {e}')
    return result


def all_resume_robots(warehouse_id):
    url = cfg.G_CONFIG_DICT['base.url_base'] + '/tes/apiv2/resumeRobots'
    result = 'fail'
    try:
        data = {
            'warehouseID': warehouse_id,
            'all': 1
                }
        r = requests.post(url=url, data=data)
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'all_resume_robots success, {res_data}')
            else:
                logging.error(f'all_resume_robots error, {res_data}')
        else:
            logging.error(f'all_resume_robots, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'all_resume_robots, {e}')
    return result


# if __name__ == "__main__":
#     import os
#     root_path = os.path.dirname(os.path.dirname(__file__))
#     cfg_path = os.path.join(root_path, './conf/config.ini')
#     cfg.load_cfg(cfg_path)
#
#     file_path = '/Users/zhangjinqiang/Downloads/V1.4_big-118-hetu1.4.hetu'
#     res = import_map(file_path)
#     print('import map res = ', res)
#
#     warehouse_id = '268370858668458740'
#     sn_type = '0'
#     robot_id = '37463339938'
#     sn = '850809707888977'
#     res = set_warehouse_sn(warehouse_id, sn_type, robot_id, sn)
#     print('set_warehouse_sn, res =', res)
#
#     pod_info = [
#         {"podID": "201", "posID": "1568272772503", "posType": 2, "podFace": 3.14, "podType": 2},
#         {"podID": "202", "posID": "1568272772518", "posType": 2, "podFace": 3.14, "podType": 2}
#     ]
#     res = multi_add_pod(warehouse_id, json.dumps(pod_info))
#     print('multi_add_pod, res = ', res)

