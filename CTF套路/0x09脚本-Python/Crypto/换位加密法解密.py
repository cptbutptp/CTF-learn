#!/usr/bin/env python
#encoding=utf-8

import math

ciphertext = 'F eah1n seAo!eaG   d hPgielosre'
key = 7

numrow = key
numcol = round(len(ciphertext)/key)
numshadow = (numcol*numrow)-len(ciphertext)

plaintext = [''] * int(numcol)

col = 0
row = 0

for symbol in ciphertext:
    plaintext[col] += symbol
    col +=1
    
    if(col==numcol) or (col == numcol-1 and row >= numrow - numshadow):
        col = 0
        row += 1
    print ''.join(plaintext)

