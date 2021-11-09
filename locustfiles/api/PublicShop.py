import logging
from locust import HttpUser, task, between
from common.param import Params
import time


class PublicSeasShopInterface(HttpUser):
    """
    公海门店
    """
    # wait_time = between(3, 5)
    filetime = round(time.time())
    logging.basicConfig(filename='./log/{}.txt'.format(filetime), level=logging.INFO)
    param = Params()

    # 公海门店列表
    @task
    def find_high_shop_info(self):
        response = self.client.post('/shop/findHighShopInfo', data=self.param.find_high_shop_info(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_high_shop_info  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                  response.json().get('msg')))

    # 公海门店业态
    @task
    def find_shop_type(self):
        response = self.client.post('/shop/findShopType', data=self.param.find_shop_type(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_shop_type  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # 公海门店行政区域
    @task
    def query_cities_data(self):
        response = self.client.post('/shop/queryCitiesData', headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('query_cities_data  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                response.json().get('msg')))

    # 公海门店详情
    @task
    def shop_detail(self):
        response = self.client.post('/shop/shopDetail/{}'.format(self.param.shopId), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('shop_detail  error is code={} or msg={}'.format(response.json().get('code'),
                                                                          response.json().get('msg')))

    # 公海门店创建
    # @task
    # def create_high_shop(self):
    #     # 添加headers 将照片进行二进制方式上传
    #     h_k = 'Content-Type'
    #     h_v='multipart/form-data; boundary=----WebKitFormBoundary5BrAXiHiKGZIltiN'
    #     head = self.param.headers()
    #     head[h_k] = h_v
    #     # 添加headers 将照片进行二进制方式上传
    #     response = self.client.post('/shop/createHighShop', data=self.param.create_high_shop(),
    #                                 headers=head)
    #     print(self.param.create_high_shop())
    #     print(head)
    #     print(response.text)
    #     time.sleep(5)
    #     if response.json().get('code') != 0:
    #         raise Exception('shop_detail  error is code={}'.format(response.status_code))

    # 修改门店竟对
    @task
    def edit_shop_actually(self):
        response = self.client.post('/shop/editShopActually', data=self.param.edit_shop_actually(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('edit_shop_actually  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                 response.json().get('msg')))

    # 编辑门店信息
    @task
    def editor_stores_(self):
        response = self.client.post('/shop/editShop', data=self.param.edit_shop(), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('editor_stores_  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # 修改竟对门店转化
    @task
    def change_stores_competition_percent(self):
        response = self.client.post('/shop/editShopActually', data=self.param.change_stores_competition_percent(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info(
                'change_stores_competition_percent  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                       response.json().get('msg')))

    # 公海门店认领
    @task
    def stores_claim(self):
        response = self.client.post('/shop/claimShop/69913/{}'.format(self.param.shopId), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('stores_claim  error is code={} or msg={}'.format(response.json().get('code'),
                                                                           response.json().get('msg')))

    # 公海门店牌照变更
    @task
    def stores_picture_edit(self):
        response = self.client.post('/shop/shopPictureEdit/4341995', data=self.param.stores_picture_edit(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('stores_picture_edit  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                  response.json().get('msg')))

    # 获取区域code
    @task
    def find_region_code(self):
        response = self.client.post('/shop/findRegionCode', data=self.param.find_region_code(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_region_code  error is code={} or msg={}'.format(response.json().get('code'),
                                                                               response.json().get('msg')))

    # 用户收藏竞品列表
    @task
    def find_collect_shops(self):
        response = self.client.post('/shop/findCollectShops', data=self.param.find_collect_shops(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_collect_shops  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                 response.json().get('msg')))

    # 竞品收藏
    @task
    def collect_shop(self):
        response = self.client.post('/shop/collectShop', data=self.param.collect_shop(), headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('collect_shop  error is code={} or msg={}'.format(response.json().get('code'),
                                                                           response.json().get('msg')))

    # 取消收藏
    @task
    def cancel_collect(self):
        response = self.client.get('/shop/cancelCollect?', params=self.param.cancel_collect(),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('cancel_collect  error is code={} or msg={}'.format(response.json().get('code'),
                                                                             response.json().get('msg')))

    # 查询公海竞品地图
    @task
    def find_competitor_collects(self):
        response = self.client.post('/shop/findCompetitorCollects', data=self.param.find_competitor_collects(),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_competitor_collects  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                       response.json().get('msg')))

    # 公海门店优选展示tag页
    @task
    def show_tab_page(self):
        response = self.client.get('/shop/showTabPage', headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('show_tab_page  error is code={} or msg={}'.format(response.json().get('code'),
                                                                            response.json().get('msg')))

    # 创建门店，按名称搜索公海门店
    # @task
    # def search_high_shop(self):
    #     self.client.post('/shop/searchHighShop')

    # 门店变更记录
    @task
    def find_shop_change_log(self):
        response = self.client.get('/shop/findShopChangeLog?{}'.format(self.param.find_shop_change_log()),
                                   headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_shop_change_log  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                   response.json().get('msg')))

    # 门店认领
    @task
    def claim_shop_userid_shop_id(self):
        param = self.param.claim_shop_userid_shop_id()
        response = self.client.post('/shop/claimShop/{}/{}'.format(param[0], param[1]),
                                    headers=self.param.headers())
        if response.json().get('code') != 0:
            logging.info('find_shop_change_log  error is code={} or msg={}'.format(response.json().get('code'),
                                                                                   response.json().get('msg')))
