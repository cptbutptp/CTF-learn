#coding=utf-8
import sys
def open_txt():  #��TXT�ı�д������
    try:
        xxx = file(sys.argv[1], 'r')
        for xxx_line in xxx.readlines():
            passlist.append(xxx_line)
        xxx.close()
    except:
        return 0
         
def write_txt():  #��TXT�ı�д������
    try:
        yyy = file(sys.argv[2], 'w')
        for i in list_passwed:
            yyy.write(i)
        yyy.close()
    except:
        return 0
         
         
global  passlist  #����ȫ�ֱ���
passlist = []    #�û�����anonymous ����Ϊ��
open_txt()   #TXT��������
#passlist = list(set(passlist))   #python �б�ȥ��
global  list_passwed  #�б�ȥ�أ�������ԭ����˳��
list_passwed=[]
for i in passlist:
    if i not in list_passwed:
        list_passwed.append(i)
write_txt()