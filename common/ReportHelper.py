# coding=utf-8
import os
from datetime import datetime
import threading

# ======== Reading web_config.ini setting ===========
base_dir = os.path.dirname(os.path.dirname(__file__))
base_dir = base_dir.replace("\\", "/")

class ReportHelper:
    def __init__(self):
        global result_Path, report_gen_Path, result_time
        result_Path = os.path.join(base_dir, "result")
        if not os.path.exists(result_Path):
            os.mkdir(result_Path)
        result_time = str(datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
        report_gen_Path = os.path.join(result_Path, result_time)
        if not os.path.exists(report_gen_Path):
            os.mkdir(report_gen_Path)


    def get_report_path(self):
        '''
        获得测试报告路径
        :return:
        '''
        report_path = os.path.join(report_gen_Path, (result_time + "_report.html"))
        return report_path

    def get_result_path(self):
        '''
        获得每次测试结果文件路径
        :return:
        '''
        return report_gen_Path


class MyRh:
    rh = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_Rh():

        if MyRh.rh is None:
            MyRh.mutex.acquire()
            MyRh.rh = ReportHelper()
            MyRh.mutex.release()

        return MyRh.rh


if __name__ == "__main__":
    rh = MyRh.get_Rh()