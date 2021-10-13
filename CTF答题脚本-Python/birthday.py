#!/usr/bin/env python
#coding=utf-8

#import zipFile
import zipfile
import threading

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print("Password success",password)
        return password
    except:
        pass

def main():
    zFile=zipfile.ZipFile('birthday.zip')
    for num1 in range(1990,1991):
        for num2 in range(1,13):
            for num3 in range(1,31):
                password = str(num1)
                if(num2<10):
                    password += '0'+str(num2)
                else:
                    password += str(num2)
                if(num3<10):
                    password += '0'+str(num3)
                else:
                    password += str(num3)
                t = threading.Thread(target=extractFile,args=(zFile,password))
                if password:
                    print u"爆破中:"+password
                t.start()

if __name__ =='__main__':
    main()
                        