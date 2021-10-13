#!/usr/bin/env python
#encoding=utf-8
#create a 4 num dict


f = open('dic.txt','w')
for i in range(19900101,19941232):
    dic = str(i)
    f.write(dic+'\n')

f.close()