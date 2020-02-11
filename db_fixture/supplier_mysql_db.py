# coding=utf8
import pymysql.cursors
import os
import configparser as cparser
import read_config as readconfig

# ======== Reading db_config.ini setting ===========
localReadConfig = readconfig.ReadConfig()
host = localReadConfig.get_db_dev_supplier("host")
port = localReadConfig.get_db_dev_supplier("port")
db = localReadConfig.get_db_dev_supplier("db_name")
user = localReadConfig.get_db_dev_supplier("user")
password = localReadConfig.get_db_dev_supplier("password")


# ======== MySql base operating ===================
class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    # def clear(self, table_name):
    #     # real_sql = "truncate table " + table_name + ";"
    #     real_sql = "delete from " + table_name + ";"
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
    #         cursor.execute(real_sql)
    #     self.connection.commit()

    # delete data by some condition
    def delete_data(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(sql)
            cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
        self.connection.commit()

    # update by sql
    def update(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"

        with self.connection.cursor() as cursor:
            result = cursor.execute(real_sql)
        self.connection.commit()

    # query id by sql
    def get_field_value(self, sql, field):
        result_array = []
        cur = self.connection.cursor()
        cur.execute(sql)
        num_rows = int(cur.rowcount)
        for i in range(num_rows):
            row = cur.fetchone()
            result_array.append(row[field])
        cur.close()
        return result_array

    # get num rows
    def get_num_rows(self,sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        num_rows = int(cur.rowcount)
        cur.close()
        return num_rows


    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    # table_name = "sign_event"
    # data = {'id':1,'name':'红米','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2016-08-20 00:25:42'}
    # table_name2 = "sign_guest"
    # data2 = {'realname':'alen','phone': 12312341234,'email':'alen@mail.com','sign':0,'event_id':1}
    # # db.clear(table_name)
    # db.insert(table_name, data)
    db.close()
