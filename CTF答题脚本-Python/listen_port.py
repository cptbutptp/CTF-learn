#!/usr/bin/env python
import sys
import commands
import json
import subprocess  
import time

while 1:
    cmd = 'netstat -tnp'
    result =commands.getoutput(cmd)
    #d2 = json.dumps(result)
    result= result.split('\n')
    #print result[1]
    #print len(result)
    for i in range(2, len(result)):
        for j in range(1,10):
            result[i]=result[i].replace('  ',' ')
        result[i]=result[i].split(' ')
        #print result[i]
        result[i][3]=result[i][3].split(':')
        #print result[i][3][1]
        xinren=0
        file_object = open('bai.txt')
        try:
            #list_of_all_the_lines = file_object.readlines( )
            for line in file_object:
                #print result[i][4][0]+'  '+line
                if line.__contains__(result[i][3][1]):
                    xinren=1
                    #print 'safe connection!'+result[i][4][0]
                    break
        finally:
            file_object.close( )
            if xinren==0:
                 result[i][6]=result[i][6].split('/')
                 #print result[i][6][0]
                 if result[i][6][0]!='-':
                     print 'found unsafe link port:'+ result[i][4]+':'+result[i][6][0]
                     commands.getoutput("kill -9 "+result[i][6][0])
    
    time.sleep(3)

