#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2015/7/03
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
import sys, os
from Crypto.Cipher import DES


def decode_char(c):
    if c == 'a':
        r = '?'
    else:
        r = c
    return ord(r) - ord('!')


def ascii_to_binary(s):
    assert len(s) == 24

    out = [0] * 18
    i = 0
    j = 0

    for i in range(0, len(s), 4):
        y = decode_char(s[i + 0])
        y = (y << 6) & 0xffffff

        k = decode_char(s[i + 1])
        y = (y | k) & 0xffffff
        y = (y << 6) & 0xffffff

        k = decode_char(s[i + 2])
        y = (y | k) & 0xffffff
        y = (y << 6) & 0xffffff

        k = decode_char(s[i + 3])
        y = (y | k) & 0xffffff

        out[j + 2] = chr(y & 0xff)
        out[j + 1] = chr((y >> 8) & 0xff)
        out[j + 0] = chr((y >> 16) & 0xff)

        j += 3

    return "".join(out)


def decrypt_password(p):
    """
    huawei/h3c�����������ƽ⺯��
    p:����ļ�������
    return: ������������
    """
    r = ascii_to_binary(p)

    r = r[:16]

    d = DES.new("\x01\x02\x03\x04\x05\x06\x07\x08", DES.MODE_ECB)
    r = d.decrypt(r)

    return r.rstrip("\x00")


if __name__ == '__main__':
    print '+' + '-' * 50 + '+'
    print u'\t    huawei/h3c�����������ƽ⹤��'
    print u'\t   Blog��http://www.waitalone.cn/'
    print u'\t\t Code BY�� ���Եȴ�'
    print u'\t\t Time��2015-07-03'
    print '+' + '-' * 50 + '+'
    if len(sys.argv) != 2:
        print '�÷�: ' + os.path.basename(sys.argv[0]) + ' �������ܵ�����'
        print 'ʵ��: ' + os.path.basename(sys.argv[0]) + ' "aK9Q4I)J\'#[Q=^Q`MAF4<1!!"'
        sys.exit()
    print '���ܽ����' + decrypt_password(sys.argv[1])
