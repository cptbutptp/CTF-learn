# -*- coding: utf-8 -*-
# crc32Collision.py
import threading
import binascii
import time

def breakpassword():
	start=time.clock()
	crc_num=set([0x7C2DF918,0xA58A1926,0x4DAD5967])
	x = range(32,128)
	for i in x:
		for j in x:
			for k in x:
				for l in x:
					for m in x:
						for n in x:
							mutex.acquire() 
							string=chr(i)+chr(j)+chr(k)+chr(l)+chr(m)+chr(n)
							if binascii.crc32(string) in crc_num:
								print "crc32 of %s is-> %s" %(string,hex(binascii.crc32(string)))
								f=open("string.txt",'a')
								f.write(string)
								f.close()
							mutex.release()
	end=time.clock()
	print "Used time: %f s" % (end - start)

def main(thread_num):
	print "breaking,please wait!"
	global mutex 
	mutex=threading.Lock()
	threads=[]
	for x in xrange(0,thread_num): 
		threads.append(threading.Thread(target=breakpassword))
		for t in threads:
			t.start()

		for t in threads:
			t.join()

if __name__ == '__main__':
	main(10)