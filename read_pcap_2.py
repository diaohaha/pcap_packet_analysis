#coding = utf-8
#author: gaoda

import sys
from read_pcap import read_pcap
from ip_address import search_ip_real_addr

def main():
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    
    fpcap = file(pcapfile,"rb")
    http_datas = read_pcap(fpcap)
    
    for http_data in http_datas:
        print search_ip_real_addr(http_data['srcip'])['data']['country'] 

if __name__ == "__main__":    
    main()    
