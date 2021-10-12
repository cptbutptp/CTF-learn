#!/usr/bin/python
import hashlib
import sys
'''
for i in range(65,91):
	for j in range(65,91):
		for k in range(65,91):
			str="TASC" + chr(i) + "O3RJMV" +chr(j) + "WDJKX" + chr(k) +"ZM"
			enc_str=hashlib.md5()
			enc_str.update(str)
			#print enc_str.hexdigest()[0:4].upper()
			if(enc_str.hexdigest()[0:4].upper()=="E423"):
				print str,enc_str.hexdigest()
				#sys.exit()
print 'end'



'''
import hashlib
for i in range(65,91):
	for j in range(65,91):
		for k in range(65,91):
			string = "TASC" + chr(i) + "O3RJMV" +chr(j) + "WDJKX" + chr(k) +"ZM"
			enc_str = hashlib.md5()
			enc_str.update(string)
			enc_str = enc_str.hexdigest()
			if  enc_str[0:4].upper() == "E903":
				print "The string is :" + string
				print "The md5 of the string is :" + enc_str.upper()
