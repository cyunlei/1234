# -*- coding : utf-8-*-
# coding:unicode_escape
import logging
from locust import HttpUser, task, between
from common.param import Params
import time


class FeiGn(HttpUser):
    """
    feign�����ڲ��ӿ�
    """
    wait_time = between(1, 2)
    filetime = round(time.time())
    logging.basicConfig(filename='./log/{}.txt'.format(filetime), level=logging.INFO)
    param = Params()

    # �豸����-�ŵ��ѯ
    @task
    def find_divide_shop_by_id(self):
        response = self.client.get('/shop/feign/findDivideShopById/{}'.format(self.param.find_divide_shop_by_id()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_divide_shop_by_id  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                     response.json().get('msg')))

    # ��������-�ۼ��������
    @task
    def approval_ok(self):
        response = self.client.get('/shop/feign/approvalOK?'.format(self.param.approval_ok()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('approval_ok  error is code={} or msg={}'.format(response.json().get('code'),
                                                                          response.json().get('msg')))

    # ��������-�����Ѵ������
    @task
    def update_record_status_for_approve(self):
        response = self.client.get(
            '/shop/feign/updateRecordStatusForApprove?'.format(self.param.update_record_status_for_approve()),
            headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info(
                'update_record_status_for_approve  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                      response.json().get('msg')))

    # ��������-��ͬЭ��׷�ӽ�����
    @task
    def append_admission_status(self):
        response = self.client.get(
            '/shop/feign/appendAdmissionStatus?'.format(self.param.append_admission_status()),
            headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('append_admission_status  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                      response.json().get('msg')))

    # �豸����-����շѲ���
    @task
    def update_fee_strategy(self):
        response = self.client.get(
            '/shop/feign/updateFeeStrategy?'.format(self.param.update_fee_strategy()), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('update_fee_strategy  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                  response.json().get('msg')))

    # ��������-���������Ϣ��ѯ
    @task
    def query_admission_info(self):
        response = self.client.get(
            '/shop/feign/queryAdmissionInfo?'.format(self.param.query_admission_info()), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('query_admission_info  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                  response.json().get('msg')))
