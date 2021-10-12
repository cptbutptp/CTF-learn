#!/usr/bin/env python
#encoding = utf-8

#凯撒密码  
import pyperclip  

#将要被加密或解密的字符串
message = 'This is my secret message.'

#加密解密的key
key = 13

#告诉程序当前的模式是加密或解密
mode = 'encrypt'

#对应的密码表
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#用来存储加密或解密转换之后的字符
translated = ''

#将要处理的字符串转换成大写
message = message.upper()

#在消息串中的每个符号上运行加密/解密代码
for symbol in message:
    
    #如果字符在密码表中
    if symbol in LETTERS:
        
        #获取当前加密或解密字符在密码表中的位置
        num = LETTERS.find(symbol)
        
        #如果是加密模式，对应加密得到的字符的位置数字num等于当前位置加上密钥值
        if mode == 'encrypt':
            num = num+key
            
        #如果是解密模式，对应解密得到的字符的位置数字num等于当前位置减去密钥值
        if mode == 'decrypt':
            num = num-key
            
        #如果计算得到的num大于或小于字母表的长度，那就绕回计算
        if num>=len(LETTERS):
            num = num - len(LETTERS)
        if num < 0:
            num = num + len(LETTERS)          
        #num将会是加密或解密之后字母在LETTERS中的索引，我们希望把这个加密或解密之后的字母添加到
        #translated字符串末尾
        translated = translated + LETTERS[num]       
    else:
        #如果加密解密的字符是非字母，如；'等特殊字符，那么将原封不动的添加到translated字符后面
        translated = translated + symbol
print(translated)
pyperclip.copy(translated)




