import json
import random
from common.config.Chinese import *
from common.util.GetTool import *


class Params:
    def __init__(self):
        self.UserAgent = 'Mozilla/5.0 (Linux; U; Android 11; zh-CN; Mi 10 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.0.36 Mobile Safari/537.36 AliApp(DingTalk/6.0.22) com.alibaba.android.rimet/15078563 Channel/700159 language/zh-CN UT4Aplus/0.2.25 colorScheme/light'
        self.cookie_aa07 = get_cookie(uname='aa07', pwd='Ycb@13')
        self.cookie_aa05 = get_cookie(uname='aa05', pwd='Ycb@13')
        self.status = 11
        self.city = '北京市'
        self.province = '北京市'
        self.area = '朝阳区'
        self.pageOffset = 0
        self.latitude = '39.91674'
        self.longitude = '116.396751'
        self.authUid = 'aa07'
        self.authType = 'SYS'
        self.sessionId = '0b1f04b8-6b64-4469-8dbc-44a25691330d'
        self.searchInput = None
        self.shopSource = None
        self.shopType = 'Shop_Type'
        self.shopId = 4339224
        self.unexpectedly = 0
        self.type = None
        self.locate = '北京市朝阳区褡裢坡001号'
        self.stime = '2001'
        self.etime = 2002
        self.cost = '100'
        self.phone = create_phone()
        self.accKey = '123456QAZ'
        self.ytType = 32,
        self.shopName = create_name(),
        self.timeStart = '00 : 00'
        self.timeEnd = '00 : 00'
        self.shopType1 = 1
        self.address = '110000,110100,110101'
        self.locate = '景山前街4号故宫博物院太和殿内'
        self.trueName = create_name()
        self.userPhone = create_phone()
        self.shopCompetes = "000001"
        self.submitType = 2
        self.inputId = 69913
        self.files = 'D:/Probject/SuLv-Locust/img/1.jpg'
        self.id = None
        self.my_shop_id = '5449707'  # 我已经认领的门店
        self.bdm_userid = '69911'
        self.bdm_shopId = '6083910'
        self.bdm_principal = '178'
        self.bdm_updateType = 0
        self.bdm_searchVal = '杭州市'
        self.bdm_authUid = '69913'
        self.shopIds = 4339224
        self.receive_shopid = '5447748'
        self.sid = 203000578  # sid为设备id
        self.vip_shopid = '5449707'

    def headers(self):
        headers = {
            'cookie': self.cookie_aa07,
            'User-Agent': self.UserAgent,
        }
        # headers.update(f)
        return headers

    def headers_aa05(self):
        headers = {
            'cookie': self.cookie_aa05,
            'User-Agent': self.UserAgent,
        }
        # headers.update(f)
        return headers

    def find_high_shop_info(self):
        data = {
            'status': self.status,
            'city': self.city,
            'province': self.province,
            'area': self.area,
            'pageOffset': self.pageOffset,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

        return data

    def find_shop_type(self):
        data = {
            'shopType': self.shopType
        }
        return data

    def edit_shop_actually(self):
        data = {
            'type': 4,
            'unexpectedly': self.unexpectedly,
            'id': self.shopId
        }

        return data

    def create_high_shop(self):
        data = {
            "ytType": 32,
            "shopName": self.shopName[0],
            "timeStart": self.timeStart[0],
            "timeEnd": self.timeEnd[0],
            "cost": self.cost,
            "phone": self.phone[0],
            "shopType": self.shopType,
            "address": self.address[0],
            "locate": self.locate[0],
            "trueName": self.trueName[0],
            "userPhone": self.userPhone[0],
            "latitude": self.latitude,
            "longitude": self.longitude,
            "shopCompetes": self.shopCompetes[0],
            "shopCompetesReason": "",
            "submitType": self.submitType,
            "inputId": self.inputId,
            "shopSource": "",
            "brand": "",
            'files': self.files[0]

        }
        return data

    def edit_shop(self):
        data = {
            'id': 4343643,
            'type': 58,
            'shopType': '',
            'locate': '西单堂子胡同9号新一代商城一层182号(进门口环岛红色招牌)',
            'latitude': '39.91111',
            'longitude': '116.37533',
            'stime': '10:00',
            'etime': '21:00',
            'cost': 459,
            'phone': '15110264111'
        }
        return data

    def claim_shop_userid_shop_id(self):
        return self.inputId, self.receive_shopid

    def change_stores_competition_percent(self):
        data = {
            'type': 4,
            'unexpectedly': 2,
            'id': 4343643
        }
        return data

    def stores_picture_edit(self):
        data = {
            'pictureImg': 'D:/Probject/SuLv-Locust/img/1.jpg'
        }
        return data

    def find_region_code(self):
        data = {
            "province": "北京市",
            "city": "北京市",
            "area": "朝阳区"
        }
        return data

    def find_collect_shops(self):
        data = {
            'search': '',
            'pageOffset': 0
        }
        return data

    def collect_shop(self):
        data = {
            'shopId': '1451240',
            'shopName': '四指遥高端进口超市（东方新天地店）',
            'province': '北京市',
            'city': '北京市',
            'district': '东城区',
            'address': '北京市东城区东方新天地第五区LG层BB82号',
            'closedTime': '00:00:00',
            'openTime': '00:00:00',
            'lat': '39.909485',
            'lng': '116.41461',
            'avgPrice': 0,
            'shopPic': 'null',
            'applet': '来电',
            'isCollect': 'false',
            'distances': '0.1'
        }
        return data

    def cancel_collect(self):
        return 'shopId=1451240'

    def find_competitor_collects(self):
        data = {
            'lat': '39.90965',
            'lng': '116.41406',
            'applet': '怪兽'
        }
        return data

    def find_shop_change_log(self):
        return 'shopId=2097128&page=1'

    def find_my_shops(self):
        data = {
            'userId': self.inputId,
            'searchInput': '',
            'signStatus': '13',
            'devStatus': '0',
            'otherScreen': '0',
            'pageOffSize': '0'
        }
        return data

    def get_shop_order(self):
        data = {
            'date': '',
            'shopId': self.my_shop_id
        }
        return data

    def update_shop_mag_fee(self):
        data = {
            'shopId': self.my_shop_id,
            'userId': self.inputId,
            'feeStrategyId': '5001'
        }
        return data

    def update_shop_bluetooth_mag_fee(self):
        data = {
            'shopId': self.my_shop_id,
            'userId': self.inputId,
            'bluetoothFeeStrategyId': '1691'
        }
        return data

    def shop_visit(self):
        data = {
            'page': '1',
            'shopId': self.my_shop_id
        }
        return data

    def shop_manager_task(self):
        data = {
            'page': '1',
            'shopId': self.my_shop_id
        }
        return data

    def find_sellers(self):
        return 'userId={}&type={}&newSeller='.format(self.bdm_userid, 0)

    def check_shop_seller(self):
        data = {
            'shopId': self.bdm_shopId,
            'userId': self.bdm_userid,
            'principal': self.bdm_principal,
            'updateType': self.bdm_updateType
        }
        return data

    def find_organizations(self):
        data = {
            'searchVal': self.bdm_searchVal,
            'authUid': self.bdm_authUid,
        }
        return data

    def audit_organization(self):
        data = {
            'shopId': '4335341',
            'maintenanceOrgid': '1113215',
            'merchantId': '1168923',
            'authType': 'SYS',
            'authUid': 'aa07',
            'sessionId': '0b1f04b8-6b64-4469-8dbc-44a25691330d'
        }
        return data

    def shop_info(self):
        return 'sessionId={}&authType={}&authUid={}&search='.format(self.sessionId, self.authType, self.authUid)

    def find_org_all_sellers(self):
        return 'authType={}&authUid={}'.format(self.authType, self.authUid)

    def add_authorize(self):
        data = {
            'userId': self.inputId,
            'authorizeId': '70081',
            'start': get_strftime(),
            'end': get_strftime(),
            'authType': self.authType,
            'authUid': self.authUid,
            'shopIds': self.shopIds
        }
        return data

    def cancel_association(self):
        data = {
            'shopId': '6083900',
            'userId': self.inputId,
            'merchantId': '1168920'
        }
        return data

    def apply_closure(self):
        data = {
            'shopId': '4339224',
            'shopCloseType': '1',
            'merchantId': '1168923',
            'authType': self.authType,
            'authUid': self.authUid,
        }
        return data

    def create_approve(self):
        data = {
            'userId': self.inputId,
            'shopId': '4337508',
            'shopCloseType': '0',
            'merchantId': '1168920',
            'remark': '',
            'openDate': get_strftime(),
            'authType': self.authType,
            'authUid': self.authUid
        }
        return data

    def to_sign_shop_id(self):
        return '5454204'

    def release_shop_shop_id(self):
        return self.receive_shopid

    def pre_install(self):
        return 'authType={}&authUid={}&sid={}&shopId={}'.format(self.authType, self.authUid, self.sid, 5454204)

    def rescission_shop(self):
        return 6083900

    def shop_manager(self):
        data = {
            'userId': self.bdm_userid,
            'pageSize': 10,
            'pageOffset': 0,
            'identification': 0,
            'province': '',
            'city': '',
            'area': '',
            'searchInput': '',
            'shopStatus': '',
            'shopType': '',
            'shopSource': ''
        }
        return data

    def shop_vip_index(self):
        return '{}?authType={}&authUid={}'.format(self.vip_shopid, self.authType, self.authUid)

    def un_open_vip_list(self):
        data = {
            'authUid': self.authUid,
            'authType': self.authType,
        }
        return data

    def open_vip_list(self):
        data = {
            'authUid': self.authUid,
            'authType': self.authType,
        }
        return data

    def open_vip(self):
        data = {
            'shopId': self.vip_shopid,
            'ids': '193',
            'authUid': self.authUid,
            'authType': self.authType
        }
        return data

    def reject_vip(self):
        data = {
            'shopId': self.vip_shopid,
            'ids': '194',
            'authUid': self.authUid,
            'authType': self.authType
        }
        return data

    def close_vip(self):
        data = {
            'shopId': self.vip_shopid,
            'ids': '193',
            'authUid': self.authUid,
            'authType': self.authType
        }
        return data

    def find_divide_shop_by_id(self):
        return '5449707'

    def approval_ok(self):
        return 'traceUntieId=5449707'

    def update_record_status_for_approve(self):
        return 'recordId=6&status=5&authUid=69913'

    def append_admission_status(self):
        return 'agreementNumber=SH116890720210820477798&appendEntryFee=10'

    def update_fee_strategy(self):
        return 'shopId=1&feeId=1&blueFeeId=1'

    def query_admission_info(self):
        return 'admissionNo=JC97015202010150141017'

    def search_by_condition(self):
        data = {
            "roleId": 10,
            "searchInput": "",
            "sellerId": 69913,
            "page": 1,
            "merchantType": 1
        }
        return data

    def merchant_total_info_detail(self):
        data = {
            "merchantId": 1168988,
            "merchantType": 1,
            "sellerId": 69913,
            "roleId": 10,
            "userId": 73393,
            "signStatus": "1"
        }
        return data

    def check_deliver_params(self):
        return 'sellerId=69913&merchantId=1168988&merchantType=1'

    def merchant_total_info_change_vip(self):
        boo = [True, False]
        return random.choice(boo)

    def query_merchant_present(self):
        return 'merchantId=1168988&page=1'


if __name__ == '__main__':
    h_k = 'Content-Type'
    h_v = "multipart/form-data; boundary=----WebKitFormBoundary5BrAXiHiKGZIltiN"
    f = {"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary5BrAXiHiKGZIltiN", }
    a = Params().create_high_shop()
    print(a)
