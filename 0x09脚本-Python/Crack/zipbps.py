#!/usr/bin/env python
#coding: utf-8

import optparse
import threading
import zipfile

lock = threading.Lock()

def zipbp(z, p):
    try:
        lock.acquire()
        z.extractall(pwd=p)
        print 'password found :%s' % p
    except:
        pass
    lock.release()

def main():
    parser = optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    options, args = parser.parse_args()
    zfile = options.zname
    dict = options.dname
    z = zipfile.ZipFile(zfile)
    pwds = open(dict)
    for pwd in pwds.readlines():
        p = pwd.strip('\n')
        t = threading.Thread(target=zipbp, args=(z, p))
        t.start()
        t.join()

if __name__ == '__main__':
    main()