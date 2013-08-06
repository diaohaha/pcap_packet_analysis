# coding = utf-8
from ip_to_city import ip_to_city
from read_pcap import read_pcap

def static(records):
    '''static the same host in the packet and cacl the top 10 welcome hosts
       return a top_host list and a dict of host{"host":{'num':1,'visitor':[...]}[,]}
    '''
    hosts = {}
    tmp_hosts = {}
    for record in records:
        if record['host'] in hosts.keys():
            tmp_hosts[record['host']] += 1
            hosts[record['host']]['num'] += 1
            hosts[record['host']]['flow'] += record['packet_size']
            hosts[record['host']]['end_time'] = float(record['time'])
            addr = ip_to_city(record['srcip'])['country_name']
            hosts[record['host']]['visitors'].append((record['time'],record['srcip'],ip_to_city(record['srcip'])['country_name'],record['dstip'],ip_to_city(record['dstip'])['country_name']))
        else:
            tmp_hosts[record['host']] = 1
            hosts[record['host']] = {'start_time':record['time'],'end_time':0,'flow':float(record['packet_size']),'num':1,'visitors':[(record['time'],record['srcip'],ip_to_city(record['srcip'])['country_name'],record['dstip'],ip_to_city(record['dstip'])['country_name'])]}
            
    #cacl the top 10 welcome hosts
    #for key in hosts.keys():
        
    top_hosts = sorted(tmp_hosts.iteritems(), key=lambda d:d[1],reverse=True)      
    return top_hosts,hosts            


if __name__=="__main__":
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    
    fpcap = file(pcapfile,"rb")
    http_datas = read_pcap(fpcap)
    top_hosts,hosts = static(http_datas)
    for i in top_hosts:
        print i
    for key in top_hosts:
        print hosts[key[0]]['flow']
