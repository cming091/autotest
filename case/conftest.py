import json

import pytest
import logging
import requests

from utils import cfg


@pytest.fixture(scope="session", autouse=True)
def env():
    pass


class CollectTestCasePlugin(object):
    """
    pytest插件，收集测试用例信息，按照前端tree_transfer的属性结构，更新到数据库
    触发方式：python3 run.py --collectTestCase case
    每次git提交后，通过jenkins job同步到htp平台
    """
    case_dict = {
        'id': 'case',
        'pid': 0,
        'label': 'case',
        'children': []
    }

    def __init__(self, config):
        self.config = config

    def pytest_collection_finish(self, session):
        if self.config.option.collectTestCase:
            self._collect_test_case(session.items)

    def _append_case_tree(self, case_tree, path_list, class_name, method_name):
        if path_list[0] in case_tree.keys():
            if len(path_list) > 1:
                ret = self._append_case_tree(case_tree[path_list[0]], path_list[1:], class_name, method_name)
                case_tree[path_list[0]] = ret
            else:
                case_tree[path_list[0]][class_name].append(method_name)
                case_tree[path_list[0]]['case_num'] += 1
        else:
            case_tree[path_list[0]] = {}
            case_num = 0
            if len(path_list) > 1:
                ret = self._append_case_tree(case_tree[path_list[0]], path_list[1:], class_name, method_name)
                case_tree[path_list[0]] = ret
            else:
                case_num += 1
                case_tree[path_list[0]] = {class_name: [method_name], 'case_num': case_num}
        return case_tree

    def _get_case_tree(self, items):
        case_tree = {}
        for item in items:
            if not item.nodeid.startswith('Demo'):
                item_list = item.nodeid.split('::')
                case_path = item_list[0]
                path_list = case_path.split('/')
                class_name = item_list[1]
                method_name = item_list[2]
                case_tree = self._append_case_tree(case_tree, path_list, class_name, method_name)
        return case_tree

    def _make_case_dict(self, case_dict, case_tree, parent_id, parent_path, case_num):
        # print('entry, parent_id is ', parent_id, ' ,parent_path is ', parent_path)
        for item in case_tree.keys():
            # print('item: ', item, ', parent_id is ', parent_id, ' ,parent_path is ', parent_path)
            if item.endswith('.py'):
                node = {
                    'id': item,
                    'pid': parent_id,
                    'label': item,
                    'path': parent_path + '/' + item,
                    'children': []
                }
                case_num = case_num + case_tree[item]['case_num']
                case_dict['children'].append(node)
            else:
                node = {
                    'id': item,
                    'pid': parent_id,
                    'label': item,
                    # 'path': parent_path + '/' + item,
                    'case_num': 0,
                    'children': []
                }
                # print('before, item: ', item, 'parent_id is ', parent_id, ' ,parent_path is ', parent_path)
                old_parent_path = parent_path
                if parent_id != 'case':
                    parent_path = parent_path + '/' + item
                else:
                    parent_path = parent_id + '/' + item

                # print('after, item: ', item, 'parent_id is ', parent_id, ' ,parent_path is ', parent_path)
                ret, num = self._make_case_dict(node, case_tree[item], item, parent_path, 0)
                parent_path = old_parent_path
                ret['case_num'] += num
                case_num += ret['case_num']
                case_dict['children'].append(ret)
        return case_dict, case_num

    def _update_htp_test_case(self, case_dict, total_case_num_dict):
        url = 'http://' + cfg.G_CONFIG_DICT['htp.host'] + '/subsystem-test/testCaseCreate'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'test_case_name': 'API_Test_Case',
            'test_case_type': 1,
            'test_case_data': json.dumps(case_dict),
            'total_case_num': json.dumps(total_case_num_dict)
        }

        try:
            ret = requests.post(url=url, data=json.dumps(data), headers=headers)
            if ret.status_code != 200:
                logging.error('update test case to htp error, http status code is ', ret.status_code)
                exit(1)
            else:
                ret_dict = ret.json()
                if ret_dict['returnCode'] == 0:
                    logging.info('update test case to htp success!')
                else:
                    logging.error('update test case to htp error, returnCode is', ret_dict['ret_dict'], ', err msg is ', ret_dict['returnMsg'])
                    exit(1)
        except Exception as e:
            logging.error(f'upadte test case to htp error! {e}')
            exit(1)

    def _get_case_num(self):
        res = {}
        for key, value in cfg.G_CONFIG_DICT.items():
            if key.startswith('total_case_num'):
                res[key.split('.')[1]] = int(value)
        return res

    def _collect_test_case(self, items):
        # print('items:', items)
        # 将case整理成树形结构
        case_tree = self._get_case_tree(items)
        # print("case_list: ", json.dumps(case_tree))

        # 按照前端需要的数据结构，将case_tree拼装成一个case_dict
        case_dict, case_num = self._make_case_dict(self.case_dict, case_tree, 'case', 'case', 0)
        print('case_dict: ', json.dumps(case_dict))
        print('case_num: ', case_num)
        print('total_num: ', self._get_case_num())
        total_case_num_dict = self._get_case_num()

        # 调HTP接口，更新test_case表
        if case_num > 0:
            self._update_htp_test_case(case_dict, total_case_num_dict)

    def pytest_runtestloop(self, session):

        if session.config.option.collectTestCase:
            return True


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption(
        '--collectTestCase', action='store_true', dest="collectTestCase",
        help="collect test case")
    group.addoption(
        '--cluster', action='store_true', help='use cluster mode'
    )


def pytest_configure(config):
    print('in pytest configure')
    if config.option.collectTestCase:
        config.pluginmanager.register(CollectTestCasePlugin(config), "collectTestCase")
