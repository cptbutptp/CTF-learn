#!/usr/bin/env python 
#encoding = utf-8

list1=[]
str1=''
str4=''
strings="79 67 85 123 67 70 84 69 76 88 79 85 89 68 69 67 84 78 71 65 72 79 72 82 78 70 73 69 78 77 125 73 79 84 65"
for i in strings.split(' '):
    str1+=chr(int(i))
print "得到的密文是:",str1
i=0
while i<36:
    str2=str1[i:i+7]
    list3=['','','','','','','']
    try:
        list3[0]=str2[1]
        list3[1]=str2[6]
        list3[2]=str2[5]
        list3[3]=str2[3]
        list3[4]=str2[4]
        list3[5]=str2[0]
        list3[6]=str2[2]
    except:
        pass
    str3=''
    for j in list3:
        str3+=j
    str4+=str3
    i+=7
print "得到的明文是:",str4