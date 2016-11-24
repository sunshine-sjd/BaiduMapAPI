#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import hashlib
import requests


class LagouAPI(object):
    LAGOU_GATEWAY = 'http://www.lagou.com/jobs/positionAjax.json?'

    @classmethod
    def search_job(cls, kd, **kwargs):
        encodedstr = urllib.urlencode(kwargs)
        cls.url = cls.LAGOU_GATEWAY + encodedstr
        page = 1
        payload = {
            'first': False,
            'pn': page,
            'kd': kd
        }
        r = requests.post(cls.url, data=payload, proxies={'http': '10.144.1.10:8080'})
        json_result = r.json()
        for i in json_result['content']['positionResult']['result']:
            yield i


class BaiduMapAPI(object):
    BAIDU_GATEWAY = 'http://api.map.baidu.com'
    BAIDU_API_KEY = 'rHZYoqrQCylZupHuGUcGMtiWex57kHO7'
    BAIDU_API_SK = 'XMM2XfYZGbmbBumWA5r6enYDPhvDORBR'

    queryStr = '/place/v2/search?&q=北京市海淀区中关村南大街27号&region=杭州&output=json&ak=rHZYoqrQCylZupHuGUcGMtiWex57kHO7'
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + 'XMM2XfYZGbmbBumWA5r6enYDPhvDORBR'
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()

    @classmethod
    def search(cls):
        q = 'http://api.map.baidu.com/place/v2/search?&q=北京市海淀区中关村南大街27号&region=杭州&output=json&ak=%s&sn=%s' % (cls.BAIDU_API_KEY, cls.sn)
        print q
        r = requests.get(q, proxies={'http': '10.144.1.10:8080'})
        return r.json()

'''
a = BaiduMapAPI()
ret = a.search()
print ret['results']
print ret['results'][0]['location']
'''
'''
import requests
a = requests.get('http://www.lagou.com/jobs/2600411.html', proxies={'http': '10.144.1.10:80'})
print a.content
'''

