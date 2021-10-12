# -*- coding:utf-8 -*-
#��ȡͼƬ��������ɫֵ����������ɫֵ�����λ��ȡ����

import Image

import binascii

image = Image.open("hack.jpg")

width, height = image.size

binary_string = ""

for y in range(height):

    for x in range(width):

        #��ȡ����(x, y)������ɫֵ

        r, g, b = image.getpixel((x, y))

        color = (r << 16) + (g << 8) + b

        #��ȡ��ɫ������ֵ�����һλ

        last_bit = str(bin(color))[-1]

        binary_string += last_bit

print binary_string

#��2�����ַ���ת��16�����ַ���

hex_string = "%x"%(int(binary_string, 2))

#��ȡż�����ַ�����Ϊ�ַ��������ᱨ��

hex_string = hex_string[ : len(hex_string) / 2 * 2]

#���16����ֵ��Ӧ���ַ���

print "key :", binascii.a2b_hex(hex_string)