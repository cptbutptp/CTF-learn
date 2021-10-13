"""
This is a Hash Attack Script For CTF.

@author: BingKong
@info: auto generate with https://www.wishingstarmoye.com/cipher/hashattack
"""

import sys
import json
import hashlib
import re
import time

data = '{"str":[{"texttype":"plainttext", "plaint":""}], "hash":{"hashtype":"md5", "pattern":""}}'

def hashAttack():
    data_json = json.loads(data)
    num = len(data_json['str'])

    # print start information
    print("[+] HASHATTACK start at " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    info = ""
    for j in range(num):
        if data_json['str'][j]['texttype']=="plainttext":
            info += data_json['str'][j]['plaint']
        elif data_json['str'][j]['texttype']=="ciphertext":
            for t in range(data_json['str'][j]['len']):
                info += "?"
    print("[+] String: " + info)
    print("[+] Hash Type: " + data_json['hash']['hashtype'])
    print("[+] Pattern: " + data_json['hash']['pattern'])

    # attack start
    index = -1
    i = 0
    string = ""
    hashEnumerate(index, num, data_json,string,  i)


    print("Can not find result")

def hashEnumerate(index, num, json, string, i):
    temp = string
    if i==0:
        index+=1
    if index<num and json['str'][index]['texttype']=="plainttext":
        temp=string+json['str'][index]['plaint']
    elif index<num and json['str'][index]['texttype']=="ciphertext":
        len = json['str'][index]['len']
        pool = json['str'][index]['pool']
        if i==0:
            i=len
        if i>0 and i<=len:
            i-=1
            for c in ''.join(pool):
                temp = string + c
                hashEnumerate(index, num, json, temp, i)
            return
    if index==num:
        hash_result = ""
        if json['hash']['hashtype']=="md5":
            hash = hashlib.md5(string.encode('utf-8'))
        elif json['hash']['hashtype']=="sha1":
            hash = hashlib.sha1(string.encode('utf-8'))
        elif json['hash']['hashtype']=="sha256":
            hash = hashlib.sha256(string.encode('utf-8'))
        elif json['hash']['hashtype']=="sha384":
            hash = hashlib.sha384(string.encode('utf-8'))
        elif json['hash']['hashtype']=="sha512":
            hash = hashlib.sha512(string.encode('utf-8'))
        else:
            print("\n" + "[+] HASH TYPE: " + json['hash']['hashtype'] + "Not Support")
            exit()
        hash_result = hash.hexdigest()
        if re.match(json['hash']['pattern'], hash_result, flags=0):
            print("\n" + "[+] HASHATTACK end at " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            print("String: " + string)
            print("MD5: " + hash_result)
            exit()
        return
    hashEnumerate(index, num, json, temp, i)
    return

if __name__=="__main__":
    hashAttack()
