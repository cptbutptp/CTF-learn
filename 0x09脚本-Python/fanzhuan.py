#coding=utf-8

with open('1.jpg') as f:
    with open('2.jpg','wb') as ff:
        ff.write(f.read()[::-1])
