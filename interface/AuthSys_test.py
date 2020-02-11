# coding: utf-8

import os
import sys
import unittest
import requests
import configparser as cparser

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

# ======== Reading web_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/web_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)


class AuthSysTest(unittest.TestCase):

    def setUp(self):
        self.base_url = cf.get("Envconf", "AuthBaseUrl")
        self.content_type = cf.get("Envconf", "Content-Type")
        self._headers = {
            "Content-Type": self.content_type
        }

    def tearDown(self):
        print(self.result)

    def test_a_login(self):
        '''模拟登录'''
        test_url = self.base_url + "/jwt_auth/login"
        body = {
            "username": "",
            "password": ""
        }
        r = requests.post(url=test_url, json=body, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(self.result['is_success'], True)
        cf.set("Envconf", "token", self.result['data']['token'])
        cf.write(open(file_path, "w"))

    def test_get_userlist_from_permission_name(self):
        '''权限 - 查询拥有某权限的用户列表'''
        test_url = self.base_url + "/jwt_auth/query"
        payload = {"perm_name": "purchase.batch_confirm_alloutstock_button"}
        r = requests.get(url=test_url, params=payload, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(self.result['is_success'], True)

    def test_check_token(self):
        '''权限 - 检查Token和权限'''
        test_url = self.base_url + "/api/token/check"
        body = {"token": cf.get("Envconf", "token")}
        r = requests.post(url=test_url, json=body, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(self.result['is_success'], True)

    def test_check_token_for_wh(self):
        '''权限 - 查询当前仓库下某一权限的用户列表'''
        test_url = self.base_url + "/jwt_auth/query"
        payload = {
            "perm_name": "warehouse_location.xiaoshan",
            "perm_name": "wms.idle_list_check"
            }
        r = requests.get(url=test_url, params=payload, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(self.result['is_success'], True)


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()