# coding: utf-8

import os
import sys
import unittest
import requests

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://dev.yuceyi.com:5678"
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ilx1NWYwMFx1NTNkMVx1ODAwNSIsImlzX2Nvb3BlcmF0aXZlX3N1cHBsaWVyIjp0cnVlLCJsb2dpbl9uYW1lIjoiZGV2ZWxvcGVyIiwiZXhwIjoxNTIyMTE3NTQ0LCJ1c2VyX2lkIjoxLCJ1c2VyX3V1aWQiOiJTVVA2NzQ3NTk4NTciLCJlbWFpbCI6IiJ9.SLaDwZClBJ_heCF-qWGXa-buGsjRr4ofjf-xKMBMWu0"
        }

    def tearDown(self):
        print(self.result)

    def test_stock_warehouse_out(self):
        ''' 出库核查 - 扫描出库单号 '''
        test_url = self.base_url + "/wms/stock_warehouse/out"
        payload = {"sp_name": "WO1045570-1"}
        r = requests.get(url=test_url, params=payload, headers=self._headers)
        self.result = r.json()
        self.assertEqual(self.result['status'], '全部出库')
        self.assertEqual(self.result['shipping_name'], '老三')

    def test_pda_operate_shelve(self):
        ''' 确认移入 - 扫描sku_id - 闲置 '''
        test_url = self.base_url + "/wms/pda/operate/shelve"
        body = {
             "box_name": "X13-01-12",
             "sku_id": 705776
        }
        r = requests.patch(url=test_url, json=body, headers=self._headers)
        self.result = r.json()
        self.assertEqual(self.result['sku_no'], 705776)

    def test_login(self):
        '''模拟登录'''
        test_url = "http://dev.yuceyi.com:8899/jwt_auth/login"
        login_header = {"Content-Type": "application/json"}
        body = {
            "username": "developer",
            "password": "123"
        }
        r = requests.post(url=test_url, json=body, headers=login_header)
        self.result = r.json()
        token = self.result['data']['token']



if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
