#!/usr/bin/env python
#encoding = utf-8
#��ת���ܷ�

#Reverse Cipher

#����������
messgae = 'CTF is a good game!'

#ת��֮��������ַ���
translated = ''

#������Ϣ�ĳ���
i = len(messgae) - 1

#�����ȴ��ڵ���0ʱ�������λ�滻
while i >=0:
    translated = translated + messgae[i]
    i = i-1
    
print(translated)