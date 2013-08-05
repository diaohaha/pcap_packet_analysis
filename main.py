#coding = utf-8
#author: gaoda

import sys
from read_pcap import read_pcap
from ip_to_city import ip_to_city
from static import static
from fpdf import FPDF
import time

def main():
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    
    fpcap = file(pcapfile,"rb")
    http_datas = read_pcap(fpcap)
    
    top_hosts,hosts = static(http_datas)
    #write result in pdf
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',24)
    pdf.cell(60,10,'PCAP Analysis results','C')
    pdf.ln(20)
    for i in range(1,2):
        pdf.set_font('Arial','B',16)
        pdf.cell(70,20,"top%d"%i)
        pdf.ln(10)
        pdf.set_font('Arial','B',12)
        pdf.cell(70,20,"host:"+str(top_hosts[i-1]))
        pdf.ln(10)
        pdf.cell(70,20,"num:"+str(hosts[top_hosts[i-1]]['num']))
        pdf.ln(10)
        pdf.cell(70,20,"start static time:"+str(hosts[top_hosts[i-1]]['start_time']))
        pdf.ln(10)
        pdf.cell(70,20,"end static time:"+str(hosts[top_hosts[i-1]]['start_time']))
        pdf.ln(10)
        pdf.cell(70,20,"flow:"+str(hosts[top_hosts[i-1]]['flow']))
        pdf.ln(10)
        pdf.cell(70,20,"visitors:")
        pdf.set_font('Arial','B',10)
        for visitor in hosts[top_hosts[i-1]]['visitors']:
            pdf.ln(7)
            pdf.cell(200,20,"     time: "+time.strftime('%Y-%m-%d',time.localtime(float(visitor[0])))+"     ip: "+str(visitor[1])+"     city: gd"+str(visitor[2]))
    pdf.output('results.pdf','F')
    

if __name__ == "__main__":    
    main()  
