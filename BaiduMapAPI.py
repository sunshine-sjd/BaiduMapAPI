# 百度地图 Place API

class BaiduMapAPI(object):
    BAIDU_GATEWAY = 'http://api.map.baidu.com'
    BAIDU_API_KEY = 'rHZYoqrQCylZupHuGUcGMtiWex57kHO7'
    BAIDU_API_SK = 'XMM2XfYZGbmbBumWA5r6enYDPhvDORBR'

    queryStr = '/place/v2/search?&q=北京市海淀区中关村南大街27号&region=杭州&output=json&ak=rHZYoqrQCylZupHuGUcGMtiWex57kHO7'
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + 'XMM2XfYZGbmbBumWA5r6enYDPhvDORBR'
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    print sn

    @classmethod
    def search(cls):
        q = 'http://api.map.baidu.com/place/v2/search?&q=北京市海淀区中关村南大街27号&region=杭州&output=json&ak=%s&sn=%s' % (cls.BAIDU_API_KEY, cls.sn)
        print q
        r = requests.get(q, proxies={'http': '10.144.1.10:8080'})
        return r.json()

a = BaiduMapAPI()
ret = a.search()
print ret['results']
print ret['results'][0]['location']

'''
output:

4c5967fdd87caed4f734974109f83f9b
http://api.map.baidu.com/place/v2/search?&q=北京市海淀区中关村南大街27号&region=杭州&output=json&ak=rHZYoqrQCylZupHuGUcGMtiWex57kHO7&sn=4c5967fdd87caed4f734974109f83f9b
[{u'address': u'\u6d77\u6dc0\u533a', u'name': u'\u4e2d\u5173\u6751\u5357\u5927\u885727\u53f7', u'location': {u'lat': 39.955313, u'lng': 116.3306}}]
{u'lat': 39.955313, u'lng': 116.3306}
'''
