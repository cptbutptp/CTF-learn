#coding:gb2312
from __future__ import division
import urllib
import hashlib
import urllib2
import requests
import base64
import time

list1 = []
list2 = []
x = 0


def outputresult(list, count, temp):
    global x
    for i in range(0, len(list[count]), 1):
        if len(list) != count + 1:
            outputresult(list, count + 1, temp + list[count][i])
        else:
            print temp + list[count][i]
            x += 1


miwen = 'R2LMDEZVCKJHC2VJC0TLEQ'

#'AGV5IULSB3ZLVSE='

miwenlen = len(miwen) / 4
print "密文为" + miwen + ",总长度" + str(len(miwen)) + ",分为" + str(miwenlen) + "段开始穷举"
integer = 0
lastmingwen = ""
while integer <= miwenlen - 1:
    strdata = miwen[0 + integer * 4:4 + integer * 4]
    for i in range(1, 2 + 1):
        if i % 2 == 0:
            strdata2 = strdata[0:1].lower()
        else:
            strdata2 = strdata[0:1].upper()
        for j in range(1, 2 + 1):
            if j % 2 == 0:
                strdata3 = strdata2 + strdata[1:2].lower()
            else:
                strdata3 = strdata2 + strdata[1:2].upper()
            for k in range(1, 2 + 1):
                if k % 2 == 0:
                    strdata4 = strdata3 + strdata[2:3].lower()
                else:
                    strdata4 = strdata3 + strdata[2:3].upper()
                for l in range(1, 2 + 1):
                    if l % 2 == 0:
                        strdata5 = strdata4 + strdata[3:4].lower()
                    else:
                        strdata5 = strdata4 + strdata[3:4].upper()
                    mingwen = base64.decodestring(strdata5)
                    Base64Error = 0
                    for m in range(0, len(mingwen)):
                        if ord(mingwen[m:m + 1]) < 32 or ord(mingwen[m:m + 1]) > 126:
                            Base64Error = 1
                    if Base64Error != 1 and lastmingwen != mingwen:
                        # print "明文为"+mingwen+" 字符长度为:"+str(len(mingwen))+" 密文为"+strdata5
                        list1.append(mingwen)
                        lastmingwen = mingwen
    list2.append(list1)
    list1 = []
    integer += 1
print "穷举完毕正在进行拼接"
outputresult(list2, 0, "")

#print '爷搞完了，一共%s组，剩下的你自己看着办吧' % x

#str = "123451234512345123451234512345"
#print str[0::5]

#tempstr = open("d:\\4444.txt", "r")
#aaa = tempstr.read()
#bbb = aaa[2::3]
#count = {}
#tempint = 0.0000
#for i in range(65, 90):
    ##
    #print chr(i), bbb.count(chr(i))
    #count[i] = bbb.count(chr(i))
    #tempint = tempint + (count[i] / len(aaa)) ** 2
#print count[65]
#print tempint
