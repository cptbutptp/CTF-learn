#!/usr/bin/env python
#encoding=utf-8
import hashlib
import string

key1 = 'BK'
key2 = '7J3'
key3 = '6U'
key4 = '5EAMH'
key5 = '2S'
#dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
dic = string.letters + string.digits
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                key = key1+a+key2+b+key3+c+key4+d+key5
                flag = hashlib.md5(key).hexdigest()
                if flag[0:4] =='3e14':
                    if flag[-2:0] =='b4':
                        print (key)
                        print (flag)