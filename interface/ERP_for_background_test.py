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


class ERPForBGTest(unittest.TestCase):

    def setUp(self):
        self.base_url = cf.get("Envconf", "WMSBaseUrl")
        self.content_type = cf.get("Envconf", "Content-Type")
        self.token = cf.get("Envconf", "token")
        self._headers = {
            "Content-Type": self.content_type,
            "Authorization": self.token
        }

    def tearDown(self):
        print(self.result)

    def test_peek_wms(self):
        ''' 仓库 - 查看 仓库活跃出库单sku需求量 和 仓库现有的sku存量'''
        test_url = self.base_url + "/wms/server/peek_wms"
        r = requests.get(url=test_url, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_all_shelved_sku(self):
        '''仓库 - 查看 仓库现有的sku存量: 闲置有库位'''
        test_url = self.base_url + "/wms/server/all_shelved_sku"
        payload = {"except_date": "2017-10-10"}
        r = requests.get(url=test_url, params=payload, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_occupy_stock_check(self):
        '''出库占用 - 查询最大库存，并标记'''
        test_url = self.base_url + "/wms/stock_warehouse/occupy_stock_check"
        body = {
            "id": "2263b8cce62811e78a7cc4b301d0283f",
            "warehouse": "yuhang",
            "data": {
                "743562": 2,
                "262146": 1,
                "9999999": 1,
                "6666666": 1
            }
        }
        r = requests.post(url=test_url, json=body, headers=self._headers)
        self.result = r.json()
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertEqual(self.result['743562'], 2)


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()