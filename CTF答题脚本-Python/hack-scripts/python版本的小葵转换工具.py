#coding=utf-8
'python�汾С��ת������'
import base64
import md5
import urllib

def toHex(input):
    payload = ""
    for i in input:
        payload += hex(ord(i))[2:]
#hex(ord(i))Ϊ\0x68,0x64����ʽ��ÿ���ַ���1���ֽڴ洢
    return "0x"+payload

def toAscii(input):
    payload = ""
    for i in input:
        payload += str((ord(i)))+" "
    return payload

def toURL(input):
    payload = ""
    for i in input:
        payload += "%"+hex(ord(i))[2:]
    return payload

def toMd5(input):
    m = md5.new()
    m.update(input)
    payload = m.hexdigest()
    return payload

def toBase64(input):
    return base64.b64encode(input)

def Base64_decode(input):
    missing_padding = 4 - len(input) % 4
    if missing_padding:
        input += b'='* missing_padding
    return base64.decodestring(input)
    
if __name__=="__main__":
    while True:
        input = raw_input("please input the string:")
        print "Hex:",toHex(input)
        print "Ascii:",toAscii(input)
        print u"URL��ʽ:",toURL(input)
        print "MD5_32:",toMd5(input)
        print "Base64:",toBase64(input)
        print u"Base64����",Base64_decode(input)
        raw_input("please click 'enter' key ")