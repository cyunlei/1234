# -*- coding: utf-8 -*-
import time
import requests
import redis
import re
from urllib import parse


def get_cookie(uname, pwd):
    # 获取验证码url
    url = 'http://crmauth.dev.vsulv.com/auth/capcha/getCode'
    # 请求验证码地址并获取验证码uuid
    response = requests.post(url)
    key = response.json().get('data').get('uuid')
    # 链接redis,根据uuid获取code
    r = redis.Redis(host='r-uf6o5k7qx43r54cl7bpd.redis.rds.aliyuncs.com', port=6379, password='trnZq%9Hv79E', db='3')
    # 对获取的bytes类型进行解码
    co = r.get("captcha_codes:" + key).decode('utf-8')
    # 通过正则，匹配字符串中的数字
    co1 = re.findall('\d+', co)
    # 等待1秒
    time.sleep(1)
    # 构造post请求url及对data 进行urlencode加密，并进行登录请求
    url1 = 'http://crmauth.dev.vsulv.com/auth/login?uuid={}&code={}'.format(key, co1[0])
    data = {'username': uname, 'password': pwd}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36',
        'Referer': 'http://crmauth.dev.vsulv.com/staticPage/',
        'Origin': 'http://crmauth.dev.vsulv.com',
        'Host': 'crmauth.dev.vsulv.com',

    }
    response = requests.post(url1, data=parse.urlencode(data), headers=headers)
    # 判断返回结果是否正确
    if response.json().get('code') == 0:
        # 登录成功后获取登录成功后headers中的cookie
        set_cookie = response.headers.get('set-cookie')
        # 查找cookie分隔符位置，删除redis缓存，并将set-cookie进行切片，返回完整cookie
        num = set_cookie.find(';')
        r.delete("captcha_codes:" + key)
        return set_cookie[:num]


def get_strftime():
    """
    :return: 获取格式化后的时间戳
    """
    return time.strftime('%Y-%m-%d')
