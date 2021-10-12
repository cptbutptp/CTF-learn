#!/usr/bin/env python
#encoding = utf-8

some_stenence = '''
I Love leraing python
because python is fun
and also easy to use
'''

#打开文件,开启写文件模式
f = open('text3.txt','w')

f.write(some_stenence)
f.close()

#读取文件内容,如果不写r模式，那么默认就是读取r模式
f = open('text3.txt','r')
while True:
    line = f.readline()
    if len(line)==0:
        break
    print(line)
    
f.close()
