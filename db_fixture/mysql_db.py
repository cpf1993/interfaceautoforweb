# coding=utf8
import pymysql.cursors
import os
import configparser as cparser
from sshtunnel import SSHTunnelForwarder

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"
key_path = base_dir + "/Web-Test.pem"
cf = cparser.ConfigParser()
cf.read(file_path)

# DB_name = "citestmysqlconf"
DB_name = "mysqlconf"
host = cf.get(DB_name, "host")
port = cf.get(DB_name, "port")
db   = cf.get(DB_name, "db_name")
user = cf.get(DB_name, "user")
password = cf.get(DB_name, "password")


# ======== MySql base operating ===================
class DB:

    # def __init__(self):
    #     try:
    #         # Connect to the database
    #         server = SSHTunnelForwarder(
    #             ('ci-test.yuceyi.com', 22),
    #             ssh_username="root",
    #             ssh_pkey=key_path,
    #             # ssh_private_key_password="",
    #             remote_bind_address=('127.0.0.1', 3306)
    #         )
    #         server.start()
    #         self.connection = pymysql.connect(host='127.0.0.1',
    #                                           port=server.local_bind_port,
    #                                           user=user,
    #                                           passwd=password,
    #                                           db=db,
    #                                           charset='utf8mb4',
    #                                           cursorclass=pymysql.cursors.DictCursor)
    #     except pymysql.err.OperationalError as e:
    #         print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

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
        self.close()

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
        # self.close()
        return result_array


    # get num rows
    def get_num_rows(self,sql):
        cur = self.connection.cursor()
        cur.execute(sql)
        num_rows = int(cur.rowcount)
        self.close()
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
    db.close()

