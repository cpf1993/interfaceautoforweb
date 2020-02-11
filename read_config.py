# coding=utf-8
import os
import configparser

base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = base_dir.replace("\\", "/")
web_config_path = base_dir + "/web_config.ini"
db_config_path = base_dir + "/db_config.ini"

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(web_config_path)
        self.db_cf = configparser.ConfigParser()
        self.db_cf.read(db_config_path)

    # 以下读取web_config.ini中相关配置文件
    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_envconf(self, name):
        value = self.cf.get("Envconf", name)
        return value

    def get_po(self, name):
        value = self.cf.get("PO", name)
        return value

    def get_supplier(self, name):
        value = self.cf.get("Supplier", name)
        return value

    def get_product(self, name):
        value = self.cf.get("Product", name)
        return value

    # 以下读取db_config.ini中相关数据库配置
    def get_db_dev_idoo(self, name):
        value = self.db_cf.get("mysqlconf", name)
        return value

    def get_db_dev_supplier(self, name):
        value = self.db_cf.get("Supplierconf", name)
        return value

    def get_db_citest_idoo(self, name):
        value = self.db_cf.get("citestmysqlconf", name)
        return value

    def get_db_citest_supplier(self, name):
        value = self.db_cf.get("citestSupplierconf", name)
        return value






