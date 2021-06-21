import json
import requests
import logging
from utils import cfg


def register_warehouse(warehouse_id, warehouse_code):
    url = cfg.G_CONFIG_DICT['base.url_base'] + ':8000/wes/warebasic/warehouse/registerWarehouse'
    result = 'fail'
    try:
        data = {
            "warehouseID": warehouse_id,
            "warehouseCode": warehouse_code,
            "warehouseName": warehouse_code
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'register success, request: {data}, response: {res_data}')
            else:
                logging.error(f'register error, {res_data}')
        else:
            logging.error(f'register error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'register error, {e}')
    return result

def import_map_by_file_url(warehouse_code, region_code, file_url, region_type):
    url = cfg.G_CONFIG_DICT['base.url_base'] + ':8000/wes/warebasic/warehouse/importMapByFileUrl'
    result = 'fail'
    try:
        data = {
            "warehouseCode": warehouse_code,
            "regionCode": region_code,
            "regionName": region_code,
            "fileUrl": file_url,
            "regionType": region_type
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        if r.status_code == 200:
            res_data = r.json()
            if res_data['returnCode'] == 0:
                result = 'succ'
                logging.info(f'import success, request: {data}, response: {res_data}')
            else:
                logging.error(f'import error,data: {data} res: {res_data}')
        else:
            logging.error(f'import error, http response code is {r.status_code}')
    except Exception as e:
        logging.error(f'import error, {e}')
    return result



