#!/usr/bin/env python
#encoding = utf-8
#��λ���ܷ�

import pyperclip

#����������
def main():
    #������Ϣ
    myMessage = 'Common sense is so common'

    #������Կ
    myKey = 8
    
    #������Ϣ
    ciphertxt = encryptMessage(myKey,myMessage)
    
    #��ӡ��������Ϣ
    print(ciphertxt + '|')
    
    #�����Ŀ��Ը���
    pyperclip.copy(ciphertxt)
    
def encryptMessage(key,message):
    
    #ÿһ���ַ���������Ϣ�д���һ��
    ciphertext = ['']*key
    
    #ѭ�����������е�ÿ��
     
    for col in range(key):
        pointer = col
        
        #����ѭ��ֱ������θ��Ϣ������
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            
            pointer += key
            
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
          

