#!/usr/bin/env python
#encoding = utf-8
import Crypto

def testPass(cryptPass):
    salt = cryptPass[0:2]
dictFile = open('dictionary.txt','r')
for word in dictFile.readlines():
    word = word.strip('\n')
    cryptWord = crypt.crypt(word,salt)
    #cryptWord = Crypto.Hash.
    if(cryptPass == cryptWord):
        print "[+] Found Password: "+word+"\n"
        #return 
    print "[-] Password Not Found.\n"
    #return
def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = linesplit(":")[1].strip('')
            print "[+] Cracking Password For : "+user
            testPass(cryptPass)
if __name__ == "__main__":
    main()
