#-*- coding: utf-8 -*-

#date:2013.08.03
#author gaoda
#descirbe:tell ip and get the address
'''
请求返回的数据格式如下：
{u'code': 0, u'data': {u'ip': u'201.1.0.1', u'city': u'', u'area_id': u'',
 u'region_id': u'', u'area': u'', u'city_id': u'', u'country': u'\u5df4\u897f', 
 u'region': u'', u'isp': u'', u'country_id': u'BR', u'county': u'', u'isp_id': u'', 
 u'county_id': u''}}
'''

import re
import urllib
import json
#from urllib import request


items = ("country", "area", "region", "city", "isp" )

apiUrl = 'http://ip.taobao.com/service/getIpInfo.php?ip='

def test_ip_format(ip):
    ipRex = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
    tmp = re.findall(re.compile(ipRex),ip)
    if not tmp:
        return False
    return True		
	
def search_ip_real_addr(ip):
    #opener = request.build_opener()
    data = urllib.urlopen(apiUrl+ip).read()
    data = data.decode('UTF-8')
    ddata = json.loads(data)
    return ddata
    
if __name__=="__main__" :
    ip = "202.108.22.5"
    if not test_ip_format(ip):
        msg = "the ip format error!"
        raise TypeError(msg)		
    data = search_ip_real_addr(ip)
    for item in items:
        print data['data'][item]
        print "\n"
