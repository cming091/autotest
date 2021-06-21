# -*- coding: utf-8 -*-
import json
import requests


class TestBase:

    def post(self, url, data, content_type='form'):
        headers = ""
        if content_type == 'json':
            headers = {'Content-Type': 'application/json'}
            r = requests.post(url=url, headers=headers, data=json.dumps(data))
        else:
            r = requests.post(url=url, headers=headers, data=data)
        return r

    def get(self, url, params):
        return requests.get(url=url, params=params)

    def assert_succ(self, r):
        assert r.status_code == 200
        assert r.json()['returnCode'] == 0
        assert r.json()['returnMsg'] == 'succ'
        assert r.json()['returnUserMsg'] == '成功'
