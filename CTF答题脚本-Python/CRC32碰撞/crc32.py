import binascii
import time

start=time.clock()
crc_num=set([0x53A610F4,0x0F9C4BBD,0x0AAE6F9E])
for i in xrange(65,91):
	for j in xrange(65,91):
		for k in xrange(65,91):
			for l in xrange(65,91):
				for m in xrange(65,91):
					txt=chr(i)+chr(j)+chr(k)+chr(l)+chr(m)
					if binascii.crc32(txt) in crc_num:
						print "crc32 of %s is-> %s" %(txt,hex(binascii.crc32(txt))) 
end=time.clock()
print "Used time: %f s" % (end - start)