#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！
import sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/PyQYT/ExtentionPackages')
sys.path.append('/usr/lib/python3.4/site-packages/PyQYT/ExtentionPackages')
sys.path.append('../../ExtentionPackages')

import logging
import re
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)#清除报错
from scapy.all import *

def ftp_banner(ip, port):#定义三次TCP握手方法，传入目的IP和端口号
	source_port = random.randint(1024, 65535)#随机产生源端口
	init_sn = random.randint(1, 65535*63335)#随机产生初始化序列号
	try:#尝试进行连接
		#发送SYN包到目的地址与端口，并等待回应，随机产生源端口和初始化序列号
		result_raw_synack = sr(IP(dst=ip)/TCP(dport=port,sport=source_port,flags=2,seq=init_sn), verbose = False)
		#响应的数据包产生数组([0]为响应，[1]为未响应)
		result_synack_list = result_raw_synack[0].res
		#提取第一组[0],接收数据包[1],的TCP字段[1]并且产生字典
		tcpfields_synack = result_synack_list[0][1][1].fields
		#由于SYN算一个字节，所以客户到服务器序列号（sc_sn)需要增加1
		sc_sn = tcpfields_synack['seq'] + 1
		cs_sn = tcpfields_synack['ack']
		#发送ACK(flag = 16),完成三次握手！
		banner = sr(IP(dst=ip)/TCP(dport=port,sport=source_port,flags=16,seq=cs_sn,ack=sc_sn), verbose = False)
		banner_bit = banner[0].res[0][1][2]
		return banner_bit.fields['load'].decode().strip()
	except:#如果出现故障，跳过故障
		pass

if __name__ == '__main__':
	print(ftp_banner('192.168.220.129', 21))
