#!/usr/bin/env python
#encoding=utf-8
#create a 4 num dict

f=open("dict.txt",'w+')
chars=['0','1','2','3','4','5','6','7','8','9']
base=len(chars)
end=len(chars)**4
for i in range(0,end):
    n=i
    ch0=chars[n%base]
    n=n/base
    ch1=chars[n%base]
    n=n/base
    ch2=chars[n%base]
    n=n/base
    ch3=chars[n%base]
    print i,ch3,ch2,ch1,ch0
    f.write(ch3+ch2+ch1+ch0+'\r')
f.close()

