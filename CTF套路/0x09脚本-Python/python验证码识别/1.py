# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
import ImageEnhance
import ImageFilter
import sys
from PIL import Image
from pytesseract import *

# ��ֵ��
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#���ڶ�������
#����ʶ�����ĸ�� ���øñ��������
rep={'O':'0',
    'I':'1','L':'1',
    'Z':'2',
    'S':'8'
    };

def  getverify1(name):
    
    #��ͼƬ
    im = Image.open(name)
    #ת��������
    imgry = im.convert('L')
    imgry.save('g'+name)
    #��ֵ��
    out = imgry.point(table,'1')
    out.save('b'+name)
    #ʶ��
    text = image_to_string(out)
    #ʶ�����
    text = text.strip()
    text = text.upper();

    for r in rep:
        text = text.replace(r,rep[r])

    #out.save(text+'.jpg')
    print text
    return text
getverify1('vcode.png')
