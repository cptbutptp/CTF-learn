#!/usr/bin/env python
#coding = utf-8

import zlib
import itertools

def crc32(st):
    crc = zlib.crc32(st)
    if crc > 0:
      return "%x" % (crc)
    else:
      return "%x" % (~crc ^ 0xffffffff)

#生成年'1000'~'3000'
year = [str(i) for i in range(1000,3000)]
#生成月'01'~'12'
month = [str(i) if i>9 else (str(0)+str(i)) for i in range(1,13) ]
#生成日'01'~'31'
day = [str(i) if i>9 else (str(0)+str(i)) for i in range(1,32) ]

#题目所给
realDate = '4D1FAE0B'.lower()

#穷举日期计算crc32值然后与题目给的值进行比对，一样则输出

#利用itertools.protduct()生成年月日的所有组合
for item in itertools.product(year,month,day):
    date = ''.join(item)
    if crc32(date) == realDate:
        print date