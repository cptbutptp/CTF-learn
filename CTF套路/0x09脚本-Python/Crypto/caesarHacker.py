#!/usr/bin/env python
#encoding = utf-8

#�������뱩���ƽ����

#����Ҫ�����������Ϣ
message = 'GUVF VF ZL FRPERG ZRFFNTR'

#���������
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#ѭ��ÿһ�����ܵ�keyֵ����0-26��������ÿ��ƽ�Ƶ�λ��
for key in  range(len(LETTERS)):
    
    #���ý��ܺ�ת�����ַ���ֵ
    translated = ''
    
    #ѭ������������Ϣ
    for symbol in message:
        if symbol in LETTERS:
            
            #��ȡ��ǰ��ĸ��������ֵ
            num = LETTERS.find(symbol)
            
            #�Եõ�������ֵ��ȥ��ǰ��keyֵ�õ������ַ�������ֵ
            num = num -key 
            
            #��ü���ĵ���ֵ����LETTERS��������ֵ���¸�ֵ
            if num < 0:
                num = num + len(LETTERS)
                
            #�µ�ת�����������Ϣ���ڵ�ǰ���ļ��ϵ�ǰ��������������ַ�
            translated = translated + LETTERS[num]
        else:
            #�����������ַ�����LETTERS�У�ֱ�ӽ�����ӵ�translated֮�󼴿�
            translated = translated + symbol
            
    print('Key #%s: %s' %(key,translated))