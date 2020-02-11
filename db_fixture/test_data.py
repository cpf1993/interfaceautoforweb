# coding: utf-8
import sys
import time
import datetime as dt
import random
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB


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

# uuid = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+str(dt.datetime.now().microsecond)+str(random.randint(0,99))
# 更改插入po单的uuid使其与真实数据格式保持一致，
# '{:0>4d}'.format()与'{0:04d}'.format()     数字补零 (填充左边, 宽度为4)
def generate_po_uuid():
    return ''.join([
        dt.datetime.now().strftime("%y%m%d%H%M%S%f"),
        '{:0>4d}'.format(random.randint(0, 9999))
    ])

def generate_PB_uuid(delta_day=0):
    return ''.join([
        'PB',
        (dt.datetime.now() - dt.timedelta(delta_day)).strftime("%y%m%d%H%M%S%f"),
        '{0:04d}'.format(random.randint(0, 9999))
    ])


def prepare_data(table_name):
    uuid1 = generate_po_uuid()
    uuid2 = generate_po_uuid()
    uuid3 = generate_po_uuid()
    uuid4 = generate_po_uuid()

    bill_uuid_init = generate_PB_uuid()
    bill_uuid_undue = generate_PB_uuid()
    bill_uuid_applied = generate_PB_uuid()

    datas = {}

    if table_name == "purchase_order":
        datas = {
            'purchase_order': [
                {'uuid': uuid1, 'sku_id': '2952746', 'qty_system_demand': 1, 'qty_purchase_demand': 0, 'qty_purchased': 0,
                 'qty_received': 0, 'purchase_link_note': '颜色:深灰色/胸围(cm):98-102','short_uuid': uuid1[-12:],
                 'purchase_price': 100, 'target_warehouse_id': 1, 'create_time': '2018-10-14 03:34:48.184366', 'source_type': 0,
                 'has_backorder': 0, 'state': 0, 'create_user_id': 3168, 'create_user_name': '系统', 'sku_sale_price': 100,
                 'difficult_order': 0, 'complete_user_id':0, 'purchase_company_name': '金湖智盛服装店',
                 'logistics_status': 0, 'qty_signed': 0, 'has_bought': 0, 'is_exception': 0,'is_cooperative_supplier': 1, 'prev_state': 0,
                 'supplier_uuid': 'SUP674759857','sku_link_rel_id': 2538840, 'supplier_is_disposable': 0, 'quality_type': 'NORMAL',
                 'follow_user_id': 1,'follow_user_name':'开发者', "purchase_link":'http://detail.1688.com/offer/43932694010.html'},
                {'uuid': uuid2, 'sku_id': '2952746', 'qty_system_demand': 1, 'qty_purchase_demand': 0, 'qty_purchased': 0,
                 'qty_received': 0, 'purchase_link_note': '颜色:深灰色/胸围(cm):98-102','short_uuid': uuid2[-12:],
                 'purchase_price': 100, 'target_warehouse_id': 1, 'create_time': '2018-10-14 03:34:48.184366', 'source_type': 0,
                 'has_backorder': 0, 'state': 0, 'create_user_id': 3168, 'create_user_name': '系统', 'sku_sale_price': 100,
                 'difficult_order': 0, 'complete_user_id':0, 'purchase_company_name': '金湖智盛服装店',
                 'logistics_status': 0, 'qty_signed': 0, 'has_bought': 0, 'is_exception': 0,'is_cooperative_supplier': 1, 'prev_state': 0,
                 'supplier_uuid': 'SUP674759857','sku_link_rel_id': 2538840, 'supplier_is_disposable': 0, 'quality_type': 'NORMAL',
                 'follow_user_id': 1,'follow_user_name':'开发者', "purchase_link":'http://detail.1688.com/offer/43932694010.html'},
                {'uuid': uuid3, 'sku_id': '2952746', 'qty_system_demand': 1, 'qty_purchase_demand': 0, 'qty_purchased': 1,
                 'qty_received': 0, 'purchase_link_note': '颜色:深灰色/胸围(cm):98-102','short_uuid': uuid3[-12:],
                 'purchase_price': 100, 'target_warehouse_id': 1, 'create_time': '2018-10-14 03:34:48.184366', 'source_type': 0,
                 'has_backorder': 0, 'state': 1, 'create_user_id': 3168, 'create_user_name': '系统', 'sku_sale_price': 100,
                 'difficult_order': 0, 'complete_user_id':0,  'purchase_company_name': '金湖智盛服装店',
                 'logistics_status': 0, 'qty_signed': 0, 'has_bought': 0, 'is_exception': 0,'is_cooperative_supplier': 1, 'prev_state': 0,
                 'supplier_uuid': 'SUP674759857','sku_link_rel_id': 2538840, 'supplier_is_disposable': 0, 'quality_type': 'NORMAL',
                 'follow_user_id': 1,'follow_user_name':'开发者', "purchase_link":'http://detail.1688.com/offer/43932694010.html'},
                {'uuid': uuid4, 'sku_id': '2952746', 'qty_system_demand': 1, 'qty_purchase_demand': 0, 'qty_purchased': 1,
                 'qty_received': 0, 'purchase_link_note': '颜色:深灰色/胸围(cm):98-102','short_uuid': uuid4[-12:],
                 'purchase_price': 100, 'target_warehouse_id': 1, 'create_time': '2018-10-14 03:34:48.184366', 'source_type': 0,
                 'has_backorder': 0, 'state': 1, 'create_user_id': 3168, 'create_user_name': '系统', 'sku_sale_price': 100,
                 'difficult_order': 0, 'complete_user_id':0, 'purchase_company_name': '金湖智盛服装店',
                 'logistics_status': 0, 'qty_signed': 0, 'has_bought': 0, 'is_exception': 0,'is_cooperative_supplier': 1, 'prev_state': 0,
                 'supplier_uuid': 'SUP674759857','sku_link_rel_id': 2538840, 'supplier_is_disposable': 0, 'quality_type': 'NORMAL',
                 'follow_user_id': 1,'follow_user_name':'开发者', "purchase_link":'http://detail.1688.com/offer/43932694010.html'},
            ]
        }
    elif table_name == "purchase_order_ext":
        init_data('purchase_order')
        query_po_id_sql = "SELECT id FROM purchase_order ORDER BY id DESC LIMIT 4;"
        po_ids = query_id(query_po_id_sql, "id")
        datas = {
            'purchase_order_ext': [
                {'purchase_order_id': po_ids[0], 'sku_no': '0002952746', 'item_no': 'AMC000445565N',
                 'sku_attribute': '{"Color": "Dark Grey", "Size": "L"}', 'category_id_top': 607},
                {'purchase_order_id': po_ids[1], 'sku_no': '0002952746', 'item_no': 'AMC000445565N',
                 'sku_attribute': '{"Color": "Dark Grey", "Size": "L"}', 'category_id_top': 607},
                {'purchase_order_id': po_ids[2], 'sku_no': '0002952746', 'item_no': 'AMC000445565N',
                 'sku_attribute': '{"Color": "Dark Grey", "Size": "L"}', 'category_id_top': 607},
                {'purchase_order_id': po_ids[3], 'sku_no': '0002952746', 'item_no': 'AMC000445565N',
                 'sku_attribute': '{"Color": "Dark Grey", "Size": "L"}', 'category_id_top': 607},
            ]}

    elif table_name == "bill":
        datas = {
            'bill': [
                {'uuid': bill_uuid_init, 'supplier_uuid': 'SUP674759857', 'supplier_name': '金湖智盛服装店delete', 'qty': 1,
                 'purchase_rmb': 1,
                 'discount': 0.666, 'discount_rmb': 0.67, 'agree_pay_time': '2018-04-17 00:00:00.00000',
                 'real_pay_time': '0000-00-00 00:00:00.000000', 'supplier_note': '',
                 'create_time': '2018-04-16 23:05:00.325129',
                 'update_time': '2018-04-16 23:10:00.325129', 'freight_rmb': 10, 'total_rmb': 10.67,
                 'pr_status': 'INIT', 'qty_received': 1},
                {'uuid': bill_uuid_undue, 'supplier_uuid': 'SUP674759857', 'supplier_name': '金湖智盛服装店delete', 'qty': 1,
                 'purchase_rmb': 1,
                 'discount': 0.666, 'discount_rmb': 0.67, 'agree_pay_time': '2028-04-17 00:00:00.00000',
                 'real_pay_time': '0000-00-00 00:00:00.000000', 'supplier_note': '',
                 'create_time': '2018-04-16 23:05:00.325129',
                 'update_time': '2018-04-16 23:10:00.325129', 'freight_rmb': 10, 'total_rmb': 10.67,
                 'pr_status': 'INIT', 'qty_received': 1},
                {'uuid': bill_uuid_applied, 'supplier_uuid': 'SUP674759857', 'supplier_name': '金湖智盛服装店delete', 'qty': 1,
                 'purchase_rmb': 1,
                 'discount': 0.666, 'discount_rmb': 0.67, 'agree_pay_time': '2028-04-17 00:00:00.00000',
                 'real_pay_time': '0000-00-00 00:00:00.000000', 'supplier_note': '',
                 'create_time': '2018-04-16 23:05:00.325129',
                 'update_time': '2018-04-16 23:10:00.325129', 'freight_rmb': 10, 'total_rmb': 10.67,
                 'pr_status': 'APPLIED', 'qty_received': 1}
            ]
        }
    elif table_name == "goods_return":
        datas = {
            'goods_return': [
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0000', 'status': '0', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "开发者",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "开发者",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0010', 'status': '10', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0001', 'status': '1', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0002', 'status': '2', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0021', 'status': '21', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0022', 'status': '22', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0023', 'status': '23', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-07 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '0',
                 'application_id': 'RT0003', 'status': '3', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2017-09-04 00:00:00.000000", 'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': "4907",
                 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""},
                {'create_time': '2018-05-09 06:48:40.660261', 'apply_quantity': '1', 'return_quantity': '1',
                 'application_id': 'RT0006', 'status': '10', 'need_refund': '0',
                 'shipping_ticket_no': '', 'return_date': "2018-04-28 00:00:00.000000",'send_date': "2017-09-04 00:00:00.000000", 'applicant_id': "1",
                 'purchase_order_id': '554108', 'follow_user_id': 1, 'return_handler_id': 1, 'return_address': "",
                 'applicant_name': "开发者", 'follow_user_name': "开发者",
                 'return_handler_name': "", 'return_note': "", 'purchase_note': "", 'payer': "SUPPLIER",
                 'freight_rmb': 0.00, 'freight_total_rmb': 0.00,
                 'weight_kg': 0.00, 'payment_request_id': 1, 'return_province': "", 'return_consignee_name': "",
                 'return_consignee_phone': "", 'carrier_name': ""}
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
