# coding = utf-8

def static(records):
    '''static the same host in the packet and cacl the top 10 welcome hosts
    '''
    hosts = {}
    for record in records:
        if record['host'] in hosts.keys():
            hosts[record['host']]['num'] += 1
            hosts[record['host']]['visitors'].append((record['time'],record['srcip']))
        else:
            hosts[record['host']] = {'num':1,'visitors':[(record['time'],record['srcip'])]}
            
    #cacl the top 10 welcome hosts
    top_hosts = sorted(hosts,reverse=True)     
    return top_hosts            


if __name__=="__main__":
    pass
