#coding = utf-8

from fpdf import FPDF
import time

def print_results(top_hosts,hosts):
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font('Arial','B',24)
    pdf.cell(60,10,'PCAP Analysis results','C')
    pdf.ln(20)
    for i in range(1,len(top_hosts)):
        pdf.set_font('Arial','B',16)
        pdf.ln(10)
        pdf.cell(70,20,"top%d"%i)
        pdf.ln(10)
        pdf.set_font('Arial','B',12)
        pdf.cell(70,20,"host:"+str(top_hosts[i-1][0]))
        pdf.ln(10)
        pdf.cell(70,20,"num:"+str(hosts[top_hosts[i-1][0]]['num']))
        pdf.ln(10)
        pdf.cell(70,20,"start static time:"+str(hosts[top_hosts[i-1][0]]['start_time']))
        pdf.ln(10)
        pdf.cell(70,20,"end static time:"+str(hosts[top_hosts[i-1][0]]['start_time']))
        pdf.ln(10)
        pdf.cell(70,20,"flow:"+str(float(hosts[top_hosts[i-1][0]]['flow'])/1024)+"kb")
        pdf.ln(10)
        pdf.cell(70,20,"visitors:")
        pdf.set_font('Arial','B',10)
        for visitor in hosts[top_hosts[i-1][0]]['visitors']:
            pdf.ln(7)
            pdf.cell(200,20,"     time: "+time.strftime('%Y-%m-%d',time.localtime(float(visitor[0])))+"     srcip: "+str(visitor[1])+"     country: "+str(visitor[2])+"     dstip: "+str(visitor[3])+"     country:"+str(visitor[4]))
    pdf.output('result.pdf','F')

