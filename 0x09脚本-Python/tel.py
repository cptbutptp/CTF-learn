#!/usr/bin/env python
#encoding=utf-8
#生成一个以1391040开头的txt格式的字典

f = open('./dic.txt','w')
for  i in range(1000,9999):
    dic = '1391040'+str(i)+'\n'
    f.write(dic)
f.close
