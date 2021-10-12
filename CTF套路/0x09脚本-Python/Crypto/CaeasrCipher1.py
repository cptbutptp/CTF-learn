#!/usr/bin/env python
#encoding = utf-8

#��������  
import pyperclip  

#��Ҫ�����ܻ���ܵ��ַ���
message = 'This is my secret message.'

#���ܽ��ܵ�key
key = 13

#���߳���ǰ��ģʽ�Ǽ��ܻ����
mode = 'encrypt'

#��Ӧ�������
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#�����洢���ܻ����ת��֮����ַ�
translated = ''

#��Ҫ������ַ���ת���ɴ�д
message = message.upper()

#����Ϣ���е�ÿ�����������м���/���ܴ���
for symbol in message:
    
    #����ַ����������
    if symbol in LETTERS:
        
        #��ȡ��ǰ���ܻ�����ַ���������е�λ��
        num = LETTERS.find(symbol)
        
        #����Ǽ���ģʽ����Ӧ���ܵõ����ַ���λ������num���ڵ�ǰλ�ü�����Կֵ
        if mode == 'encrypt':
            num = num+key
            
        #����ǽ���ģʽ����Ӧ���ܵõ����ַ���λ������num���ڵ�ǰλ�ü�ȥ��Կֵ
        if mode == 'decrypt':
            num = num-key
            
        #�������õ���num���ڻ�С����ĸ��ĳ��ȣ��Ǿ��ƻؼ���
        if num>=len(LETTERS):
            num = num - len(LETTERS)
        if num < 0:
            num = num + len(LETTERS)          
        #num�����Ǽ��ܻ����֮����ĸ��LETTERS�е�����������ϣ����������ܻ����֮�����ĸ��ӵ�
        #translated�ַ���ĩβ
        translated = translated + LETTERS[num]       
    else:
        #������ܽ��ܵ��ַ��Ƿ���ĸ���磻'�������ַ�����ô��ԭ�ⲻ������ӵ�translated�ַ�����
        translated = translated + symbol
print(translated)
pyperclip.copy(translated)




