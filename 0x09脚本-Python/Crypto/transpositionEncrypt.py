#!/usr/bin/env python
#encoding = utf-8
#换位加密法

import pyperclip

#定义主函数
def main():
    #明文消息
    myMessage = 'Common sense is so common'

    #加密密钥
    myKey = 8
    
    #密文消息
    ciphertxt = encryptMessage(myKey,myMessage)
    
    #打印出明文消息
    print(ciphertxt + '|')
    
    #让密文可以复制
    pyperclip.copy(ciphertxt)
    
def encryptMessage(key,message):
    
    #每一个字符在密文消息中代表一列
    ciphertext = ['']*key
    
    #循环遍历密文中的每列
     
    for col in range(key):
        pointer = col
        
        #保持循环直到超过胃消息胡长度
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            
            pointer += key
            
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
          

