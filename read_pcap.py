#! /usr/bin/env python
#-*- coding: utf-8 -*-
'''
读取pcap文件，分析是否为http请求。然后统计它的host，srcip，time，size 。
返回为[{host:"",srcip:"",time:"",size:""}[,{...}]]
格式的列表。
'''

import sys
import dpkt
import socket
import binascii
from struct import unpack

def addr2str(addrobj):
    '''parsing the ip
    '''
    if len(addrobj) != 4 :
        return "addr error!"
    else:
        return str(ord(addrobj[0]))+"."+str(ord(addrobj[1]))+"."+str(ord(addrobj[2]))+"."+str(ord(addrobj[3]))

            
def read_pcap(fpcap):
    '''parsing the http in pcap packets
    '''
    http_data = []
    meta = {}	
    pcap = dpkt.pcap.Reader(fpcap)
    for ts, pkt in pcap:
        ethernet=dpkt.ethernet.Ethernet(pkt)
        ip = ethernet.data   
        if ethernet.type == dpkt.ethernet.ETH_TYPE_IP:	
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                dport = tcp.dport
                data = tcp.data
                if dport == 80 and len(data) > 0: 
                    try:
                        http = dpkt.http.Request(data)
                        src = unpack('I',ip.src)
                        #print "host:",http.headers['host'],"packet_size:",ip.len,"srcip:",addr2str(ip.src),"time:",ts
                        meta["host"] = http.headers['host']
                        meta["packet_size"] = ip.len
                        meta["srcip"] = addr2str(ip.src)
                        meta["dstip"] = addr2str(ip.dst)
                        meta["time"] = ts
                        http_data.append(meta.copy())
                    except:
                        pass
    return http_data                        


if __name__ == "__main__":
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    pcapfile = config.get('file', 'pcapfile', 0)
    fpcap = file(pcapfile,"rb")
    http = read_pcap(fpcap)
    #http =[{'a':1,'b':2},{'a':2,'b':2}]
    i=0
    ftxt = open('result.txt','w')
    print http
    ftxt.close()    
