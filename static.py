# coding = utf-8
from ip_to_city import ip_to_city

def static(records):
    '''static the same host in the packet and cacl the top 10 welcome hosts
       return a top_host list and a dict of host{"host":{'num':1,'visitor':[...]}[,]}
    '''
    hosts = {}
    for record in records:
        if record['host'] in hosts.keys():
            hosts[record['host']]['num'] += 1
            addr = ip_to_city(record['srcip'])
            hosts[record['host']]['visitors'].append((record['time'],record['srcip'],addr))
        else:
            hosts[record['host']] = {'num':1,'visitors':[(record['time'],record['srcip'])]}
            
    #cacl the top 10 welcome hosts
    top_hosts = sorted(hosts,reverse=True)      
    return top_hosts,hosts            


if __name__=="__main__":
    pass
