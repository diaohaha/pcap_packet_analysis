#coding = utf-8
#author: gaoda

import sys
from read_pcap import read_pcap
from ip_to_city import ip_to_city
from static import static
from output import print_results

def main():
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    
    fpcap = file(pcapfile,"rb")
    print "analysis the pcap...s"
    http_datas = read_pcap(fpcap)
    
    print "statics the results.."
    top_hosts,hosts = static(http_datas)
    #write result in pdf
    print "write the result in pdf.."
    print_results(top_hosts,hosts)
    
    

if __name__ == "__main__":    
    main()  
