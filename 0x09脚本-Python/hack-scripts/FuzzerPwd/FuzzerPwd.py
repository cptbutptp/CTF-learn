# coding=gb2312
__author__ = '����'


pwdlist=[]
#��ȡFuzzer�����ģ�壬ÿ��Ϊһ���Ž�pwdlist�б���
def getPwdTemplat():
    fr=open('pwd.yx','r')
    while 1:
        line=fr.readline().strip()
        if not line:
            break
        pwdlist.append(line)

    fr.close()
#��������ֵ�������ǰĿ¼�µ�password.txt�ļ�
def outputDicFile(fuzzerPwdList):
    f=open('password.txt','w')
    for pwd in fuzzerPwdList:
       f.write(pwd+'\n')
    f.close()
if __name__ == '__main__':
    word=raw_input('������Fuzzer����Ĺؼ���[����ؼ���","����]:')
    wordlist=word.split(',')
    getPwdTemplat()
    '''
        �����б�������ģ��������滻Ϊ�б���Ĺؼ���
    '''
    fuzzerResult=[]
    for word in wordlist:
        for i in pwdlist:
            i=i.replace('%username%',word)
            if i not in fuzzerResult:
                fuzzerResult.append(i)
    '''
        ����������Fuzzer��������
    '''
    for temp in fuzzerResult:
        print temp

    outputDicFile(fuzzerResult)
    print '����ѱ��浽password.txt��...'


