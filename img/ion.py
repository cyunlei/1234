import time

import requests
from requests_toolbelt import MultipartEncoder
import pymysql
import hashlib
import datetime

# en = MultipartEncoder(
#     {
#         'files': ('blob', open('D:/Probject/SuLv-Locust/img/1.jpg', 'rb'), 'image/jpeg'),
#
#         # 'files':('D:/Probject/SuLv-Locust/img/1.jpg',open('D:/Probject/SuLv-Locust/img/1.jpg','rb'))
#     },
#     boundary='----WebKitFormBoundaryJszJCBBtkU0HxuFz'
# )
#
#
# fromdata =  MultipartEncoder(fields={
#     'ytType': '32',
#     'shopName': '唐思纾',
#     'timeStart': '00 : 00',
#     'timeEnd': '00 : 00',
#     'cost': '1',
#     'phone': '13511367608',
#     'shopType': 'Shop_Type',
#     'address': '110000,110100,110101',
#     'locate': '景山前街4号故宫博物院太和殿内',
#     'trueName': '胡信雪',
#     'userPhone': '15065736101',
#     'latitude': '39.91674',
#     'longitude': '116.396751',
#     'shopCompetes': '000001',
#     'shopCompetesReason': '',
#     'submitType': '2',
#     'inputId': '69913',
#     'shopSource': '',
#     'brand': '',
#     'files': ('una', 'D:/Probject/SuLv-Locust/img/1.jpg', 'image/jpeg')},
#     boundary='----WebKitFormBoundaryJszJCBBtkU0HxuFz'
# )
# headers = {
#     'cookie': 'JSESSIONID=be9a23fb-97e0-4f83-8610-7cb60a2262c1',
#     'Content-Type': fromdata.content_type
# }
#
# # 'files':'D:/Probject/SuLv-Locust/img/1.jpg'
# response = requests.post(url='http://crmauth.dev.vsulv.com/shop/createHighShop',data=fromdata, headers=headers, )
# print(response.text)
# # print(fromdata)
#


def installsql():
    conn = pymysql.connect(host='rm-uf6icr6da31d1802xjo.mysql.rds.aliyuncs.com', db='sulv', user='yanglulu',
                           password='q6y#Tu@9zw')
    cursor = conn.cursor()
    for i in range(600):
        num = str(41821 + (i + 1))
        str_md5 = hashlib.md5(num.encode(encoding='utf-8')).hexdigest()
        updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(updatetime)
        argid=[1169923,1169911,1169918,1169906,96893]
        if i<=100:
            argid=argid[0]
        elif i>100 and i>=200:
            argid=argid[1]
        elif i>200 and i>=300:
            argid=argid[2]
        elif i > 300 and i >= 400:
            argid = argid[3]

        mi = "INSERT INTO ycb_manager_present_audit_review " \
                 "(id, createdBy, createdDate, lastModifiedBy, lastModifiedDate, optlock, amount_of_cash," \
                 " area_name, balance, examine_status, examine_time, merchant_id, name, seller_id, seller_name," \
                 " send_status, send_time, submit_time, type, user_id, send_type, partner_trade_no, payment_no," \
                 " actual_money, date_section, fail_message, excute_status, priority, batch_no) VALUES " \
                 "({}, 'wpc', '2021-05-19 16:29:01', 'SYS:admin', '2021-05-19 16:29:01', 1, {}," \
                 " NULL, {}, 1, '2021-05-19 16:29:01', {}, '孙六', NULL, NULL, 0, '2021-09-15 12:21:24', " \
                 "'2021-09-15 13:46:09', 0, 69913, 0, 'rkkk-{}', NULL, 475.00, NULL, '', 0, NULL, NULL)".format(num,str(num),str(num),argid,
                                                                                                                str_md5)


        cursor.execute(mi)
        conn.commit()
        print('成功插入{}条数据！'.format(i+1))

    conn.close()


installsql()