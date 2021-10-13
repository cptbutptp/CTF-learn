portList=[]
portList.append(21)
portList.append(80)
portList.append(25)
portList.append(443)

print portList

portList.sort()

pox = portList.index(80)

print portList

print pox

print "[+] There are "+str(pox) + " ports to scan before 80."

portList.remove(443)

print portList

cnt = len(portList)

print "[+] Scanning " + str(cnt)+" Total Ports."

print cnt 

services = {'ftp':21,'ssh':21,'http':80,'smtp':25}

print services.keys()

print services.items()

print services.has_key('http')

print services['http']

import socket

socket.setdefaulttimeout(4)

s = socket.socket()  # a socket variable
#print s

s.connect(("192.168.46.102",21))

banner = s.recv(1024)

#输出FTP服务器返回的banner信息
print banner 

#根据banner信息，判断这个版本的FTP是否有漏洞

if("Serv-U FTP Server v6.2" in banner):
    print "[+] 220 Serv-U FTP Server v6.2 is vulnerable."
elif("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print "[+] 3CDaemon FTP Server Version 2.0 in vulnerable"
elif("Sami FTP Server 2.0.2" in banner):
    print "Sami FTP Server 2.0.2 is vulnerable"
else:
    print "[-] FTP Server is not vulnerable"