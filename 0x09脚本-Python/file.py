#!/usr/bin/env python
#encoding = utf-8

some_stenence = '''
I Love leraing python
because python is fun
and also easy to use
'''

#���ļ�,����д�ļ�ģʽ
f = open('text3.txt','w')

f.write(some_stenence)
f.close()

#��ȡ�ļ�����,�����дrģʽ����ôĬ�Ͼ��Ƕ�ȡrģʽ
f = open('text3.txt','r')
while True:
    line = f.readline()
    if len(line)==0:
        break
    print(line)
    
f.close()
