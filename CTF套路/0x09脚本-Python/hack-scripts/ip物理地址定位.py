#!/usr/bin/python
# coding:utf-8
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}   

list_info = {

1:'�������ڲ�����',

167:'��λʧ��',

101:'AK����������',

200:'Ӧ�ò����ڣ�AK������������',

201:'Ӧ�ñ��û��Լ���ֹ',

202:'Ӧ�ñ�����Աɾ��',

203:'Ӧ�����ʹ���',

210:'Ӧ��IPУ��ʧ��',

211:'Ӧ��SNУ��ʧ��',

220:'Ӧ��Refer����ʧ��',

240:'Ӧ�÷��񱻽���',

251:'�û����Լ�ɾ��',

252:'�û�������Աɾ��',

260:'���񲻴���',

261:'���񱻽���',

301:'�������ޣ���ֹ����',

302:'�������ޣ���ֹ����',

401:'��ǰ�������ޣ����Ʒ���',

402:'��ǰ�������ܲ�������'
}


def handle_traffic(url):
    http_res = {}
    res = requests.get(url,timeout=100,headers=headers)
    http_res['code'] = res.status_code
    http_res['text'] = res.text
    return http_res

def ip_chk(ip,equ):
        #ע����Ҫak��
    url = 'http://api.map.baidu.com/highacciploc/v1?qcip={ip}&qterm={equ}&ak=ak&coord=bd09ll&extensions=3'.format(ip=ip,equ=equ)
    #ע����Ҫak��
    a = handle_traffic(url)
    res = a['text']
    res = json.loads(res)
    c_code = res['result']['error']
    if c_code == 161:
            d = res['content']['formatted_address']
            f = res['content']['address_component']['admin_area_code']
            w = res['content']['location']['lat']
            j = res['content']['location']['lng']
            print '��IP�ĵ�ַΪ��',d
            print '�õ������֤ǰ6λ��'+str(f)
            print '���ȣ�',j
            print 'γ�ȣ�',w
            print 'Full :('+str(j)+','+str(w)+')'
    else:
            for i in list_info:
                    if c_code == i:
                            print list_info[i]


if __name__ == '__main__':
        ip = raw_input('Enter ip addr: ')
        equ = raw_input('PC or MOBILE <p/m> :')
        if equ == 'p' or equ == 'P':
                equ = 'pc'
                ip_chk(ip,equ)
        elif equ == 'm' or equ == 'M':
                equ = 'mb'
                ip_chk(ip,equ)