# -*- coding : utf-8-*-
# coding:unicode_escape
import logging
from locust import HttpUser, task, between
from common.param import Params
import time


class MyShops(HttpUser):
    """
    �ҵ��ŵ�
    """
    wait_time = between(1, 2)
    filetime = round(time.time())
    logging.basicConfig(filename='./log/{}.txt'.format(filetime), level=logging.INFO)
    param = Params()

    # �ҵ��ŵ��б�
    @task
    def find_my_shops(self):
        response = self.client.post('/shop/myShop/findMyShops', data=self.param.find_my_shops(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_my_shops  error is code={} or msg={}'.format(response.json().get('code'),
                                                                            response.json().get('msg')))

    # �ŵ�����-�ŵ���Ϣ
    @task
    def signing_shop(self):
        response = self.client.post('/shop/myShop/signingShop/{}'.format(self.param.my_shop_id),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('signing_shop  error is code={} or msg={}'.format(response.json().get('code'),
                                                                           response.json().get('msg')))

    # ����ϵͳ:�豸ά��:װ��:��γ�Ȳ�ѯ
    # @task
    # def find_shop_info_by_long_and_lat(self):
    #     response = self.client.post('/shop/feign/findShopInfoByLongAndLat', data=self.param.find_my_shops(),
    #                                 headers=self.param.headers())
    #     if response.json().get('code') != 0:
    #         logging.info('find_my_shops  error is code={} or msg={}'.format(response.json().get('code'),
    #                                                                         response.json().get('msg')))

    # �豸ά��װ���ŵ�����ѯ
    # @task
    # def find_shop_info_by_name(self):
    #     response = self.client.post('/shop/findShopInfoByName/{userId}/{name}', data=self.param.find_my_shops(),
    #                                 headers=self.param.headers())
    #     if response.json().get('code') != 0:
    #         logging.info('find_my_shops  error is code={} or msg={}'.format(response.json().get('code'),
    #                                                                         response.json().get('msg')))

    # ��������
    # @task
    # def reset_password(self):
    #     response = self.client.post('/shop/myShop/resetPassword', data=self.param.find_my_shops(),
    #                                 headers=self.param.headers())
    #     if response.json().get('code') != 0:
    #         logging.info('find_my_shops  error is code={} or msg={}'.format(response.json().get('code'),
    #                                                                         response.json().get('msg')))

    # �ŵ�����-�ŵ�ҵ��
    @task
    def get_shop_order(self):
        response = self.client.post('/shop/myShop/getShopOrder', data=self.param.get_shop_order(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('get_shop_order  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # �����籦�շѲ���
    @task
    def update_shop_mag_fee(self):
        response = self.client.post('/shop/myShop/updateShopMagFee', data=self.param.update_shop_mag_fee(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('update_shop_mag_fee  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                  response.json().get('msg')))

    # ��������շѲ���
    @task
    def update_shop_bluetooth_mag_fee(self):
        response = self.client.post('/shop/myShop/updateShopBluetoothMagFee',
                                    data=self.param.update_shop_bluetooth_mag_fee(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('update_shop_bluetooth_mag_fee  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                            response.json().get('msg')))

    # �ŵ�����-�ŵ�ݷ�
    @task
    def shop_visit(self):
        response = self.client.post('/shop/myShop/shopVisit', data=self.param.shop_visit(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('shop_visit  error is code={} or msg={}'.format(response.json().get('code'),
                                                                         response.json().get('msg')))

    # �ŵ�����-�ŵ깤��
    @task
    def shop_manager_task(self):
        response = self.client.post('/shop/myShop/shopManagerTask', data=self.param.shop_manager_task(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('shop_manager_task  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                response.json().get('msg')))

    # �ŵ����:�ҵ��ŵ�:��������˼�������ά����:����������
    # �˴���¼�û�Ϊaa05
    @task
    def find_sellers(self):
        response = self.client.get('/shop/myShop/findSellers?{}'.format(self.param.find_sellers()),
                                   headers=self.param.headers_aa05())
        if response.json().get('code') != 0:
            logging.info('find_sellers  error is code={} or msg={}'.format(response.json().get('code'),
                                                                           response.json().get('msg')))

    # �ŵ����:�ҵ��ŵ�:�޸ĸ����˼��޸����ά����
    @task
    def check_shop_seller(self):
        response = self.client.post('/shop/myShop/checkShopSeller', data=self.param.check_shop_seller(),
                                    headers=self.param.headers_aa05())
        if response.json().get('code') != 0:
            logging.info('check_shop_seller  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                response.json().get('msg')))

    # �������ά����-��ѯ��������
    @task
    def find_organizations(self):
        response = self.client.post('/shop/myShop/findOrganizations', data=self.param.find_organizations(),
                                    headers=self.param.headers_aa05())
        if response.json().get('code') != 0:
            logging.info('find_organizations  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                 response.json().get('msg')))

    # �ύ�������ά����
    @task
    def audit_organization(self):
        response = self.client.post('/shop/myShop/auditOrganization', data=self.param.audit_organization(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('audit_organization  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                 response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ȩά�����ܼ�����ŵ��ȷ����ӹ���
    # @task
    # def authorize(self):
    #     response = self.client.post('/shop/myShop/authorize', data=self.param.audit_organization(),
    #                                 headers=self.param.headers())
    #     if response.json().get('code') != 0:
    #         logging.info('shop_manager_task  error is code={} or msg={}'.format(response.json().get('code'),
    #                                                                             response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ȩά��-����ŵ�ӿ�
    @task
    def shop_info(self):
        response = self.client.get('/shop/myShop/shopInfo?{}'.format(self.param.shop_info()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('shop_info  error is code={} or msg={}'.format(response.json().get('code'),
                                                                        response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ȩά��->��ȡͬ���������б���Ȩ��
    @task
    def find_org_all_sellers(self):
        response = self.client.get('/shop/myShop/findOrgAllSellers?{}'.format(self.param.find_org_all_sellers()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_org_all_sellers  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                   response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ȩά��-�ύ
    @task
    def add_authorize(self):
        response = self.client.post('/shop/myShop/addAuthorize'.format(self.param.add_authorize()),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('add_authorize  error is code={} or msg={}'.format(response.json().get('code'),
                                                                            response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:ȡ����Ȩ
    @task
    def cancel_authorize(self):
        response = self.client.get('/shop/myShop/cancelAuthorize/{}'.format(self.param.shopIds),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('cancel_authorize  error is code={} or msg={}'.format(response.json().get('code'),
                                                                               response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:�ŵ���
    @task
    def cancel_association(self):
        response = self.client.post('/shop/myShop/cancelAssociation', data=self.param.cancel_association(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('cancel_association  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                 response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:����Ъҵ���ӳ�Ъҵ-�����ύ
    @task
    def create_approve(self):
        response = self.client.post('/shop/myShop/createApprove', data=self.param.create_approve(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('create_approve  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # # ������ Ъҵ��������
    # @task
    # def operate_approve(self):
    #     response = self.client.post('/work/approve/operateApprove?authUid=aa05', data=self.param.create_approve(),
    #                                 headers=self.param.headers())
    #     if response.json().get('code') != 0:
    #         logging.info('create_approve  error is code={} or msg={}'.format(response.json().get('code'),
    #                                                                          response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:����Ъҵ���ӳ�Ъҵ
    @task
    def apply_closure(self):
        response = self.client.post('/shop/myShop/applyClosure', data=self.param.apply_closure(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('apply_closure  error is code={} or msg={}'.format(response.json().get('code'),
                                                                            response.json().get('msg')))

    # �ҵ��ŵ�:���� :�ŵ�����
    @task
    def to_sign_shop_id(self):
        response = self.client.get('/shop/myShop/toSign/{}'.format(self.param.to_sign_shop_id()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('to_sign_shop_id  error is code={} or msg={}'.format(response.json().get('code'),
                                                                              response.json().get('msg')))

    # �ҵ��ŵ�:����:�ŵ�����-�ͷ��ŵ�
    # �빫�������ŵ����Ⱥ��ϵ
    @task
    def release_shop_shop_id(self):
        response = self.client.get('/shop/myShop/releaseShop/{}'.format(self.param.release_shop_shop_id()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('release_shop_shop_id  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                   response.json().get('msg')))

    # �ҵ��ŵ�:����:�ŵ�����:Ԥװ��
    @task
    def pre_install(self):
        response = self.client.get('/shop/myShop/preInstall?authType={}&'.format(self.param.pre_install()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('pre_install  error is code={} or msg={}'.format(response.json().get('code'),
                                                                          response.json().get('msg')))

    # �ҵ��ŵ�:�ѽ�Լ:�ŵ�����
    @task
    def rescission_shop(self):
        response = self.client.get('/shop/myShop/rescissionShop/{}'.format(self.param.rescission_shop()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('rescission_shop  error is code={} or msg={}'.format(response.json().get('code'),
                                                                              response.json().get('msg')))

    # �ŵ����
    @task
    def shop_manager(self):
        response = self.client.post('/shop/myShop/shopManager', data=self.param.shop_manager(),
                                    headers=self.param.headers_aa05())
        if response.json().get('code') != 0:
            logging.info('shop_manager  error is code={} or msg={}'.format(response.json().get('code'),
                                                                           response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����
    @task
    def shop_vip_index(self):
        response = self.client.get('/shop/shopVip/index/{}'.format(self.param.shop_vip_index()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('shop_vip_index  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����:����ͨ��Ա�б�
    @task
    def un_open_vip_list(self):
        response = self.client.post('/shop/shopVip/unOpenVipList/{}'.format(self.param.vip_shopid),
                                    data=self.param.un_open_vip_list(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('un_open_vip_list  error is code={} or msg={}'.format(response.json().get('code'),
                                                                               response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����:�ѿ�ͨ��Ա�б�
    @task
    def open_vip_list(self):
        response = self.client.post('/shop/shopVip/openVipList/{}'.format(self.param.vip_shopid),
                                    data=self.param.open_vip_list(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('open_vip_list  error is code={} or msg={}'.format(response.json().get('code'),
                                                                            response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����:�ܾ���Ա
    @task
    def reject_vip(self):
        response = self.client.post('/shop/shopVip/rejectVip', data=self.param.reject_vip(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('open_vip  error is code={} or msg={}'.format(response.json().get('code'),
                                                                       response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����:��ͨ��Ա
    @task
    def open_vip(self):
        response = self.client.post('/shop/shopVip/openVip', data=self.param.open_vip(), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('open_vip  error is code={} or msg={}'.format(response.json().get('code'),
                                                                       response.json().get('msg')))

    # �ҵ��ŵ�:�ŵ�����:��Ա����:�رջ�Ա
    @task
    def close_vip(self):
        response = self.client.post('/shop/shopVip/closeVip', data=self.param.reject_vip(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('open_vip  error is code={} or msg={}'.format(response.json().get('code'),
                                                                       response.json().get('msg')))
