#!/usr/bin/env python
#encoding=utf-8
#换位加密法

message = 'F1AG is no here ! Please go head'
key = 6

cipher = ['']*key

for col in range(key):
    pointer = col
    
    while pointer < len(message):
        cipher[col] += message[pointer]
        
        pointer += key
    print ''.join(cipher)
        
        