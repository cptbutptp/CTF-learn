#!/usr/bin/env python
#encoding=utf-8

import math
import pyperclip

def main():
    mymessage = ''
    mykey = 8
    
    plaintext = decryptmessage(mykey,mymessage)
    
    print(plaintext + '|')
    pyperclip.copy(plaintext)
    
def decryptmessage(key,message):
    numofcol = math.ceil(len(message)/key)
    numofrow = key
    numofshadow = (numofcol * numofrow) - len(message)
    
    plaintext = [''] * numofcol
    
    col = 0 
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        
        if(col == numofcol) or (col == numofcol-1 and row >= numofrow -numofshadow):
            col = 0
            row +=1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()
    