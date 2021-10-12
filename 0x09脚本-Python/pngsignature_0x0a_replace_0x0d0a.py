from itertools import combinations
import binascii
import os


def find_all(source,aim):
     start=0
     while True:
          start=source.find(aim,start)
          if start==-1:
               return
          yield start
          start +=len(aim)

def repair(source,aim,filedes,num,crc):
     matchlist=list(find_all(source,'\x0a'))

     for subnet in combinations(matchlist,num):
          subnet=sorted(subnet)
          temp=''
          if(num==3):
               temp=source[:subnet[0]]+'\x0d\x0a'+source[subnet[0]+1:subnet[1]]+'\x0d\x0a'+source[subnet[1]+1:subnet[2]]+'\x0d\x0a'+source[subnet[2]+1:]
          if(num==2):
               temp=source[:subnet[0]]+'\x0d\x0a'+source[subnet[0]+1:subnet[1]]+'\x0d\x0a'+source[subnet[1]+1:]
          if(num==1):
               temp=source[:subnet[0]]+'\x0d\x0a'+source[subnet[0]+1:]
          if "%08x" % (binascii.crc32(temp)&0xFFFFFFFF)==crc:
               filedes.write(temp)
               filedes.write(binascii.a2b_hex(crc))
               filedes.flush()
               print "success"
               break;
     print "fail"

uncfile=open("image.png","rb")
cocfile=open("correct.png","wb")
#first write
correct=uncfile.read(0x6d)
cocfile.write(correct)
cocfile.flush()

correct=uncfile.read(0x4)#length
cocfile.write(correct)
cocfile.flush()

uncorrect=uncfile.read(0x20000-0x1+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,1,crc)#1
#second write
correct=uncfile.read(0x4)#length
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x3+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,3,crc)#2
#third write
correct=uncfile.read(0x4)#length
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x1+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,1,crc)#3
#fourth write
correct=uncfile.read(0x4+0x4+0x20000+0x4)
cocfile.write(correct)
cocfile.flush()
#fifth write
correct=uncfile.read(0x4)#length
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x3+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,3,crc)#4
#6th
correct=uncfile.read(0x4)#length
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x1+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,1,crc)#5
#7th
correct=uncfile.read(0x4)
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x2+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,2,crc)#6
#8th
correct=uncfile.read(0x4+0x4+0x20000+0x4)
cocfile.write(correct)
cocfile.flush()
#9th
correct=uncfile.read(0x4)
cocfile.write(correct)
cocfile.flush()
uncorrect=uncfile.read(0x20000-0x1+0x4)
crc=uncfile.read(0x4)
crc=binascii.hexlify(crc)
print crc
repair(uncorrect,'\x0a',cocfile,1,crc)#7
#10th
correct=uncfile.read(0x4+0x4+0x216f)
cocfile.write(correct)
cocfile.flush()

uncfile.close()
cocfile.close()