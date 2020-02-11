# -*- coding: utf-8 -*-

import time, sys
import os
import xlrd
import unittest
import configparser as cparser
from HTMLTestRunner import HTMLTestRunner


sys.path.append('./interface')
sys.path.append('./db_fixture')
import read_config as readconfig
from common.ReportHelper import MyRh
from common.config_email import MyEmail
from db_fixture import test_data

# ======== Reading web_config.ini setting ===========
localReadConfig = readconfig.ReadConfig()

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Supplier_home_*_test.py')


class RunTest:
    def __init__(self):
        global reportPath_html, on_off
        result_help = MyRh.get_Rh()
        reportPath_html = result_help.get_report_path()
        on_off = localReadConfig.get_email("on_off")
        self.email = MyEmail.get_email()


    def find_pyfile_and_import(self, root_dir):
        '遍历rootDir下所有目录，import所有*_test.py'
        # 判断传入的路径下是否有"__init__.py"文件，如没有，则认为没有这个moudle
        if os.path.exists(root_dir):
            arr = root_dir.split("/")
            path_dir = ""
            for path in arr:
                path_dir = path_dir + path + "/"
                if not os.path.exists(path_dir + "/__init__.py"):
                    f = open(path_dir + "/__init__.py", 'w')
                    f.close()
        # 遍历文件夹找出_test结尾的py文件
        list_dirs = os.walk(root_dir)
        for dirName, subdirList, fileList in list_dirs:
            for f in fileList:
                file_name = f
                if file_name[-8:] == "_test.py":
                    if dirName[-1:] != "/":
                        imp_path = dirName.replace("/", ".")[2:].replace("\\", ".")
                    else:
                        imp_path = dirName.replace("/", ".")[2:-1]
                    if imp_path != "":
                        exe_str = "from " + imp_path + " import " + file_name[0:-3]
                    else:
                        exe_str = "import" + file_name[0:-3]
                    exec (exe_str, globals())


    def get_xls_case_by_index(self, xls_path, sheet_name):
        """
        获取excel表里指定sheet数据，保存到列表中返回
        :param xls_path: excel路径
        :param sheet_name: sheet表名
        :return:
        """
        my_file = xlrd.open_workbook(xls_path)
        sheet = my_file.sheet_by_name(sheet_name)
        my_ncols = sheet.ncols
        for j in range(my_ncols):
            cell_value = sheet.cell_value(0, j)
            if cell_value == "fileName":
                col1 = j
            elif cell_value == "ClassName":
                col2 = j
            elif cell_value == "caseName":
                col3 = j
        my_rows = sheet.nrows
        case_list = []
        for i in range(1, my_rows):
            if sheet.row_values(i)[0].lower().strip() == 'ready':
                file_name = sheet.cell_value(i, col1)
                class_name = sheet.cell_value(i, col2)
                case_name = sheet.cell_value(i, col3)

                case = '%s.%s("%s")' % (file_name.strip(), class_name.strip(), case_name.strip())
                case_list.append(case)
        return case_list


    def gen_test_suite(self, _test_dir):
        test_unit = unittest.TestSuite()
        self.find_pyfile_and_import(_test_dir)
        test_case_list = self.get_xls_case_by_index(xls_path='./CaseList.xlsx', sheet_name='Sheet1')
        for test_case in test_case_list:
            test_unit.addTest(eval(test_case))
        return test_unit

    def run(self):
        '''
        run interface test
        :return:
        '''
        try:
            fp = open(reportPath_html, 'wb')
            runner = HTMLTestRunner(stream=fp,
                                    title='Interface Test Report',
                                    description='Implementation Example with: ')
            runner.run(discover)
            # runner.run(self.gen_test_suite(test_dir))
        except Exception as ex:
            print ex
        finally:
            fp.close()
            # send test report by email
            if on_off == 'on':
                self.email.send_email()
                print "\nReport email has been sent."
            elif on_off == 'off':
                print "\nDoesn't send report email to developer."
            else:
                print "Unknow state."


if __name__ == "__main__":
    # # test_data.init_data() # 初始化接口测试数据
    obj = RunTest()
    obj.run()
