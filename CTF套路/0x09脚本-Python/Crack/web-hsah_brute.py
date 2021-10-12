#!/usr/bin/env python
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import hashlib

hash = "9ec6f9b428237082a103fba7f2b020a683e0ca0a"
for i in range(0,100001):
        hashmd5 = hashlib.md5(str(i)).hexdigest()
        hashsha1 = hashlib.sha1(hashmd5).hexdigest()
        if hashsha1 == hash:
                print i
                num = i
                break

url = "http://172.16.1.129/web/web47/index.php"
status = requests.session()
post_data = {"num":i,'submit': '%E6%8F%90%E4%BA%A4'}
result = status.post(url, data=post_data)
print result.content