#!/usr/bin/env python
#encoding = utf-8

#凯撒密码暴力破解程序

#定义要输入的密文消息
message = 'GUVF VF ZL FRPERG ZRFFNTR'

#定义密码表
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#循环每一个可能的key值，从0-26，即就是每次平移的位置
for key in  range(len(LETTERS)):
    
    #设置解密后转换的字符串值
    translated = ''
    
    #循环遍历密文消息
    for symbol in message:
        if symbol in LETTERS:
            
            #获取当前字母的索引数值
            num = LETTERS.find(symbol)
            
            #对得到的索引值减去当前的key值得到明文字符的索引值
            num = num -key 
            
            #如该计算的到的值超过LETTERS表，对索引值重新赋值
            if num < 0:
                num = num + len(LETTERS)
                
            #新的转换后的密文消息等于当前密文加上当前计算出来的密文字符
            translated = translated + LETTERS[num]
        else:
            #如果这个密文字符不在LETTERS中，直接将其添加到translated之后即可
            translated = translated + symbol
            
    print('Key #%s: %s' %(key,translated))