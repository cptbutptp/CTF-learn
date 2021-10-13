#!/usr/bin/env python
#encoding=utf-8

import string

#use maketrans function make a rot13 table
rot13 = string.maketrans( 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz" 
)

# print string.translate("Hello World!", rot13)

x = open('MinionQuest.pdf', 'rb').read()
y = open('out1.pdf', 'w')

y.write(string.translate(x, rot13))
print 'done.'

