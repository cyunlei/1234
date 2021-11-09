# -*- coding : utf-8-*-
# coding:unicode_escape
import logging
from locust import task, between
from common.param import Params
import time, json
from common.auth.on_auth import TaskStart


class BM(TaskStart):
    """
    �̻�����
    """
    wait_time = between(1, 2)
    filetime = round(time.time())
    logging.basicConfig(filename='./log/{}.txt'.format(filetime), level=logging.INFO)

    param = Params()
    param_add_headers = param.headers()['Content-Type'] = 'application/json;charset=UTF-8'
    merchant_total_info_search_by_condition = param.search_by_condition()
    merchant_total_info_search_by_condition['searchInput'] = '1168988'
    lists_search_by_condition = [param.search_by_condition(), merchant_total_info_search_by_condition]

    # �̻������б�ӿ� / �̻����� - ������������ѯ�ӿ�
    @task
    def search_by_condition(self):
        """
        :�����ӿ�ʹ�ò�ͬ��body����,ͨ��ѭ��ȡ����ͬ��body �ֱ�����ִ��
        """
        for params_data in self.lists_search_by_condition:
            response = self.client.post('/shop/merchantTotalInfo/searchByCondition',
                                        data=json.dumps(params_data), headers=self.param_add_headers)
            if response.json().get('code') != 0:
                logging.info('search_by_condition  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                      response.json().get('msg')))

    # �̻�����
    @task
    def merchant_total_info_detail(self):
        response = self.client.post('/shop/merchantTotalInfo/detail',
                                    data=json.dumps(self.param.merchant_total_info_detail()),
                                    headers=self.param_add_headers)
        if response.json().get('code') != 0:
            logging.info('merchant_total_info_detail  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                         response.json().get('msg')))

    # ��ѯ�Ƿ���Ե���̻����䰴ť
    @task
    def check_deliver_params(self):
        response = self.client.get(
            '/shop/merchantTotalInfo/checkDeliverParams?{}'.format(self.param.check_deliver_params()),
            headers=self.param_add_headers)
        if response.json().get('code') != 0:
            logging.info('merchant_total_info_detail  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                         response.json().get('msg')))

    # ��ͨ��ȡ����Ա
    @task
    def merchant_total_info_change_vip(self):
        response = self.client.post(
            '/shop/merchantTotalInfo/changeVip/73393/{}'.format(self.param.merchant_total_info_change_vip()),
            headers=self.param_add_headers)
        if response.json().get('code') != 0:
            logging.info(
                'merchant_total_info_change_vip  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                    response.json().get('msg')))

    # �̻����ּ�¼��ѯ
    @task
    def query_merchant_present(self):
        response = self.client.get(
            '/shop/merchantTotalInfo/queryMerchantPresent?'.format(self.param.query_merchant_present()),
            headers=self.param_add_headers)
        if response.json().get('code') != 0:
            logging.info(
                'merchant_total_info_change_vip  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                    response.json().get('msg')))
