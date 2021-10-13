#!/usr/bin/env python
#encoding=utf-8
#生成一个以nsfocus开头的txt格式的字典

f = open('./dic.txt','w')
for  i in range(10000,99999):
    dic = 'nsfocus'+str(i)+'\n'
    f.write(dic)
f.close
