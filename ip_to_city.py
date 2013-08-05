# coding: utf-8
import pygeoip
import re
'''
返回的数据格式如下：
{'city': 'Falls Church', 'region_name': 'VA', 'area_code': 703, 'time_zone': 'America/New_York', 
'dma_code': 511, 'metro_code': 'Washington, DC', 'country_code3': 'USA', 
'latitude': 38.864000000000004, 'postal_code': '22042', 'longitude': -77.1922, 
'country_code': 'US', 'country_name': 'United States', 'continent': 'NA'}
'''

def test_ip_format(ip):
    '''test the ip format
    '''
    ipRex = '^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$'
    tmp = re.findall(re.compile(ipRex),ip)
    if not tmp:
        return False  
    return True	
    
    
def ip_to_city(ip):
    '''get the real addr use ip, if failed return None
    '''
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    ipfile = config.get('file', 'ipfile', 0)
    
    gi = pygeoip.GeoIP(ipfile, pygeoip.MEMORY_CACHE)
    record = gi.record_by_addr(ip)
    if record == None:
		return {'country_name':None}
    return record

if __name__=="__main__" :
    ip = '113.111.60.3'
    if test_ip_format(ip):
        print ip_to_city(ip)
    else:
		print "format error of ip"    	
