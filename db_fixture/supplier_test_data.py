# coding: utf-8
import sys
import time
import datetime as dt
import random
sys.path.append('../db_fixture')
try:
    from supplier_mysql_db import DB
except ImportError:
    from .supplier_mysql_db import DB


# create data
# datas = {
#     # 'zip_code_whitelist': [
#     #     {'id': 1, 'zip_code': 110001, '`delivery_way`': 'DTDC'},
#     #     {'id': 2, 'zip_code': 110002, '`delivery_way`': 'DTDC'},
#     # ],
#     # 'black_list': [
#     #     {'id': 1, 'object_type': 1, 'object_value': 'alexazavala12345@gmail.com', 'active': 1, 'create_time': '2017-10-10 03:08:07'},
#     # ],
# }


def prepare_data(table_name):
    uuid1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+str(dt.datetime.now().microsecond)+str(random.randint(0,99))
    bill_uuid_init = 'PB' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(dt.datetime.now().microsecond) + str(random.randint(0,99))
    datas = {}

    if table_name == "purchase_order":
        datas = {
            'purchase_order': [
                {'uuid': uuid1, 'qty_system_demand': 1, 'qty_purchase_demand': 1, 'qty_purchased': 1,
                 'qty_received': 0, 'target_warehouse_id': 1, 'create_time': '2018-03-14 03:34:48.184366', 'source_type': 0,
                 'has_backorder': 0, 'state': 0, 'create_user_id': 3168, 'stock_keep_unit_id': 157477, 'sku_sale_price': 1.00,
                 'difficult_order': 0, 'complete_user_id':0,'supply_order_id': 146450, 'purchase_company_name': '金湖智盛服装店',
                 'logistics_status': 0, 'qty_signed': 0, 'has_bought': 0, 'is_exception': 0,'is_cooperative_supplier': 1, 'prev_state': 0,
                 'supplier_uuid': 'SUP674759857','sku_link_rel_id': 40577146, 'supplier_is_disposable': 0, 'quality_type': 'NORMAL','purchase_price': 1.00}
            ]
        }
    elif table_name == "bill":
        datas = {
            'bill': [
                {'uuid': bill_uuid_init, 'supplier_uuid': 'SUP674759857', 'supplier_name': '金湖智盛服装店delete', 'qty': 1,
                 'purchase_rmb': 1,
                 'discount': 0.666, 'discount_rmb': 0.67, 'agree_pay_time': '2018-04-17 00:00:00.00000',
                 'real_pay_time': '0000-00-00 00:00:00.000000', 'supplier_note': '',
                 'create_time': '2018-04-16 23:05:00.325129',
                 'update_time': '2018-04-16 23:10:00.325129', 'freight_rmb': 10, 'total_rmb': 10.67,
                 'pr_status': 'INIT', 'qty_received': 1}
            ]
        }
    return datas


# Insert table data
def init_data(table_name):
    datas = prepare_data(table_name)
    DB().init_data(datas)


# query id
def query_id(sql, field):
    return DB().get_field_value(sql, field)

# delete table data
def delete_test_data(sql):
    DB().delete_data(sql)



if __name__ == '__main__':
    init_data()
