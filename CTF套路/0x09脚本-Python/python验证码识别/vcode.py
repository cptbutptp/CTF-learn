#!/usr/bin/env python
# -*- coding: cp936 -*-
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/11/27
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print 'ģ�鵼�����,��ʹ��pip��װ,pytesseract�������¿⣺'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit

img = Image.open('vcode.png','r')
img.load()
print img
vcode = pytesseract.image_to_string(img)
print vcode
print 'okaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
