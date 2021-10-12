#!/usr/bin/env python
#encoding=utf-8
#统计字符串中每一个单词出现的个数

import re

file = open('english.txt','r')
data = re.findall(r"[\w']+",file.read())
print data

word_dic = {}

for word in data:
    if word not in word_dic:
        word_dic[word] = 0  
        for item in data:
            if item==word:
                word_dic[word] +=1
print sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
                