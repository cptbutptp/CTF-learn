#!/usr/bin/env python
#encoding=utf-8

import string

rot13 = string.maketrans("NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

x = str(raw_input("please enter string:"))

y = string.translate(x,rot13)

print "The convert rot13's string is: \n"+y