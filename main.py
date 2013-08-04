#coding = utf-8
#author: gaoda

import sys
from read_pcap import read_pcap
from ip_to_city import ip_to_city
from static import static
from fpdf import FPDF

def main():
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    
    fpcap = file(pcapfile,"rb")
    http_datas = read_pcap(fpcap)
    
    hosts = static(http_datas)
    print hosts
    
    #write result in pdf
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',16)
    i = 0
    for host in hosts:
        pdf.cell(70,30+i,host)
        i = i + 30
    pdf.output('results.pdf','F')
    
    #for http_data in http_datas:
     #   print http_data['srcip']
      #  print ip_to_city(http_data['srcip'])

if __name__ == "__main__":    
    main()    
