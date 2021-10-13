#!/usr/bin/env python
#encoding = utf-8
#author = tq001

import os
import sys
import socket

def restBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
    except:
        return
def checkVulns(banner,filename):
    f = open(filename,'r')
    for  lien in f.readlines():
        if line.strip('\n') in banner:
            print ' [+]  Server is vulnerable: '+\
                  banner.strip()
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print ' [-] ' + filename + 'does not exists!'
            exit(0)
        if not os.access(filename,os.R_OK):
            print ' [-] ' + filename + 'access denied!.'
            exit(0)
        print ' [+] Reading Vulnerabilities From: ' + filename 
    else:
        print ' [-] Usage: '+ str(sys.argv[0])  +\
        '<vuln.filename>'
        exit(0)
        portList = [21,22,23,25,80,110,443]
        for x in range(2,5):
            ip = '172.16.1.'+ str(x)
            for port in portList:
                banner = retBanner(ip,port)
                if banner:
                    print ' [+] '+ ip + ':'+ banner
                    checkVulns(banner, filename)
                    
if __name__ == '__main__':
    main()

            