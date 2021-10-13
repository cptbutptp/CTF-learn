# -*- coding:utf-8 -*-
#获取图片的所有颜色值并把所有颜色值的最低位提取出来

import Image

import binascii

image = Image.open("hack.jpg")

width, height = image.size

binary_string = ""

for y in range(height):

    for x in range(width):

        #获取坐标(x, y)处的颜色值

        r, g, b = image.getpixel((x, y))

        color = (r << 16) + (g << 8) + b

        #获取颜色二进制值的最后一位

        last_bit = str(bin(color))[-1]

        binary_string += last_bit

print binary_string

#将2进制字符串转成16进制字符串

hex_string = "%x"%(int(binary_string, 2))

#截取偶数个字符，因为字符是奇数会报错

hex_string = hex_string[ : len(hex_string) / 2 * 2]

#输出16进制值对应的字符串

print "key :", binascii.a2b_hex(hex_string)