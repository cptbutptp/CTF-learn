#!/usr/bin/env python
#encoding = utf-8

import zipfile

zfile = zipfile.ZipFile("E:\flag.zip")
passFile = open('dictionary.txt')
num =0
for line in passFile.readlines():
    password = line.strip('\n') 
    try:
        zfile.extractall(pwd=password)
        num = num+1 
        print '[+] Password = '+password + '\n'
        print 'The crack num is:'
        print num 
        exit(0)
    except Exception,e:
        print '[-] Password error!'
        num = num+1
        

