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

#������'1000'~'3000'
year = [str(i) for i in range(1000,3000)]
#������'01'~'12'
month = [str(i) if i>9 else (str(0)+str(i)) for i in range(1,13) ]
#������'01'~'31'
day = [str(i) if i>9 else (str(0)+str(i)) for i in range(1,32) ]

#��Ŀ����
realDate = '4D1FAE0B'.lower()

#������ڼ���crc32ֵȻ������Ŀ����ֵ���бȶԣ�һ�������

#����itertools.protduct()���������յ��������
for item in itertools.product(year,month,day):
    date = ''.join(item)
    if crc32(date) == realDate:
        print date