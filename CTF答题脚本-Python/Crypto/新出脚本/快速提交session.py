#coding:utf-8
import requests
fast_session = requests.Session()
print fast_session.ppost(url,data={'key':base64.b64decode(fast_session.get(url).headers['hint']).split('in')[0]}).content