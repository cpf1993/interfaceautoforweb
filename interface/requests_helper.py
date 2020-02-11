# coding: utf-8

import os
import sys
import unittest
import requests
import configparser as cparser
import FuncGen

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

# ======== Reading web_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/web_config.ini"

cf = cparser.ConfigParser()
cf.read(file_path)


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.base_url = cf.get("Envconf", "WMSBaseUrl")
        self.content_type = cf.get("Envconf", "Content-Type")
        self.token = cf.get("Envconf", "token")
        self._headers = {
            "Content-Type": self.content_type,
            "Authorization": self.token
        }
        self._data = [{"sp_name": "WO1045570-1"}, {"sp_name": "WO1045570-2"}, {"sp_name": "WO1045570-3"}]
        self.my_list = ['test_a', 'test_b', 'test_c']
        self.dictf = {}
        self.result = []

    def tearDown(self):
        for _result in self.result:
            print(_result)
        # print (self.result)

    def test_test(self):
        for a in self.my_list:
            self.dictf.update({a: FuncGen.FuncGen(a)})

        for i, a in enumerate(self.my_list):
            self.dictf[a]("get", self.base_url+"/wms/stock_warehouse/out", self._data[i], self._headers)
            r = FuncGen.r
            self.result.append(r.json())
            # if i == 0:
            #     self.result = r.json()
            # else:
            #     self.result.update(r.json())
            self.assertEqual(r.status_code, requests.codes.ok)


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()

