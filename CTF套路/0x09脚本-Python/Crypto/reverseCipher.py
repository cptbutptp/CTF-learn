#!/usr/bin/env python
#encoding = utf-8
#反转加密法

#Reverse Cipher

#请输入明文
messgae = 'CTF is a good game!'

#转换之后的密文字符串
translated = ''

#定义消息的长度
i = len(messgae) - 1

#当长度大于等于0时，逐次逐位替换
while i >=0:
    translated = translated + messgae[i]
    i = i-1
    
print(translated)