#coding=gbk

'''
CodIng By Seay
Blog www.cnseay.com
'''

import os
import sys
import datetime
import time

#----------------------����������-----------------------------------

_php_arr = ['eval(','assert(','disk_total_space','wscript.shell','gethostbyname(','cmd.exe','shell.application','touch(','documents and settings','system32','serv-u','','��Ȩ','phpspy','����']
_asp_arr = ['eval(','execute(','wscript.shell','cmd.exe','touch(','documents and settings','system32','serv-u','','��Ȩ','aspspy','����']
_jsp_arr = ['getHostAddress(','wscript.shell','gethostbyname(','cmd.exe','documents and settings','system32','serv-u','','��Ȩ','jspspy','����']
_aspx_arr = ['eval(','UseShellExecute','wscript.shell','cmd.exe','documents and settings','system32','serv-u','','��Ȩ','aspxspy','����']

#----------------------����������-----------------------------------

#�ű��ļ�����
_Type_list = ['asp', 'php','aspx','jsp','cer','asa','cdx','ashx','ascx' ]


#ɨ�躯��
#��ȡ·����ָ����չ���ļ����ж��Ƿ���ں���
def _Get_Files(_type,_path):
    
    print('\n')
    print('             �����ļ�                   ')
    print('##############################################')
    print('    ����˵��        �ļ�·��               \n')
    
    for _root,_dirs,_files in os.walk(_path):
        for _file in _files:
            
            if _file.find('.')!=-1:
                
                _txt = _file[(_file.rindex('.')+1):]
                
                _Is_Over = False
                
                if _txt==_type : 
                    
                    #��ȡ�ļ�����
                    _R_Str = open(os.path.join(_root,_file),'r')
                    _Str = _R_Str.read()
                    _R_Str.close()
                    
                    if _type =='php':    #ɨ��PHP���͵��ļ�
                        for code in _php_arr:
                            if _Str.find(code)!=-1:
                                print('    ���ɴ���        '+os.path.join(_root,_file))
                                break
                    elif _type =='jsp':  #ɨ��JSP���͵��ļ�
                        for code in _jsp_arr:
                            if _Str.find(code)!=-1:
                                print('    ���ɴ���        '+os.path.join(_root,_file))
                                break
                    elif _type =='asp':  #ɨ��ASP���͵��ļ�
                        for code in _asp_arr:
                            if _Str.lower().find(code)!=-1:
                                print('    ���ɴ���        '+os.path.join(_root,_file))
                                break                       
                    elif _type =='aspx':  #ɨ��ASPX���͵��ļ�
                        for code in _aspx_arr:
                            if _Str.find(code)!=-1:
                                print('    ���ɴ���        '+os.path.join(_root,_file))
                                break    
                    continue
                else:  #�ж��Ƿ�Ϊ�����ű�����
                    for _File_Type in _Type_list:
                        if _File_Type == _txt:
                            print('    '+_File_Type+' �ű��ļ�    '+os.path.join(_root,_file))  
                            _Is_Over = True
                            break 
                    
                #���û�������룬Ҳ���������ű��ļ����ͼ���ǲ��ǻ����ļ�
                if _Is_Over == False:
                    __FreakFile_Scan(_root,_file) 
        #����Ŀ¼ɨ��
        _FreakDir_Scan(_root)
            
                


#���ļ�����޸�ʱ��ɨ��
def _Get_Time_Files(_type,_path,_time):
    print('\n')
    print('             �����ļ�                   ')
    print('#####################################################')
    print('    ����˵��        �ļ�·��           ����޸�ʱ��   \n')
        
    for _root,_dirs,_files in os.walk(_path):
        for _file in _files:
            if _file.find('.')!=-1:
                    
                _txt = _file[(_file.rindex('.')+1):]
                    
                if _txt==_type : 
                    _File_Time =os.path.getmtime(_root+'\\'+_file)
                    if _File_Time>_time:
                        print('    ʱ�����        '+_root+'\\'+_file+'    '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(_root+'\\'+_file))))
    


#�����ļ����
def __FreakFile_Scan(_root,_FileName):
    if _FileName.find('.')!=-1 and _FileName.count('.')>1:
        if _FileName[_FileName.index('.'):_FileName.rindex('.')].find('php')!=-1:
            print('    �����ļ���      '+os.path.join(_root,_FileName))
    elif _FileName.find('.')!=-1 and _FileName.find(';')!=-1:
        print('    �����ļ���      '+os.path.join(_root,_FileName)) 
                
             

#�����ļ��м��
def _FreakDir_Scan(_root):
    if _root.find('.') and _root[-(_root.rfind('.')):].lower().find('asp')!=-1:
        print('    ����Ŀ¼��      '+os.path.join(_root)) 



#���󱨸溯��
def _Error_Report(_Err):
    print('  ------------------------------\n\n')
    
    print('  '+_Err+'\n\n')
    
    print('  ------------------------------\n\n')
    
    
    
#main����-�������
def main(): 
    if len(sys.argv)==3 :
        if sys.argv[1].lower()!='-p' and  sys.argv[1].lower()!='-j':
            _Error_Report('-- ɨ�����Ͳ�������ȷ -p ���� -j')
            return
        
        if os.path.lexists(sys.argv[2])==False:
            _Error_Report('-- Ŀ¼������ ')
            return
        
        if sys.argv[1].lower() == '-p' and os.path.lexists(sys.argv[2])==True :
            _Get_Files('php',sys.argv[2])
                
        elif sys.argv[1].lower() == '-j' and os.path.lexists(sys.argv[2])==True :
            _Get_Files('jsp',sys.argv[2])   
            
        elif sys.argv[1].lower() == '-a' and os.path.lexists(sys.argv[2])==True :
            _Get_Files('asp',sys.argv[2])       
            
        elif sys.argv[1].lower() == '-x' and os.path.lexists(sys.argv[2])==True :
            _Get_Files('aspx',sys.argv[2])       
        
    elif len(sys.argv)==2 and sys.argv[1].lower()=='-h':
        print('\n  ����˵����\n')
        print('   -p ɨ��php�ļ�\n')
        print('   -a ɨ��asp�ļ�\n')
        print('   -j ɨ��jsp�ļ�\n')
        print('   -x ɨ��aspx�ļ�\n')
         
        print('   -t ����ʱ��ɨ��\n')
        
        print('   -h ����\n')
        
        print('   ����ʾ����\n')
        print('    s.py �Cp E:\\wwwroot\n')
        print('    ɨ��E:\\wwwrootĿ¼�µ�php�ļ�\n')
            
        print('    s.py �Cp E:\\wwwroot �Ct "2012-12-12 12:12:12"\n')
        print('    ����ʱ�䡰2012-12-12 12:12:12��ɨ��E:\\wwwrootĿ¼�µ�php�ļ�\n')
            
        print('    ��ʾ��ֱ�����г��򣬿ɸ�����ʾ����ɨ�������\n')
        
        exit(0)
    elif len(sys.argv)==1:
        
        _type = 0
        
        while _type !=1 and _type != 2:
            print('��ѡ��ɨ���ļ����ͣ�\n\n')
            print('1�� PHP\n')
            print('2�� JSP\n')
            print('3�� ASP\n')
            print('4�� ASPX\n')
            print('5�� �˳�\n\n')
            
            try:
                _type = int(raw_input('��ѡ��'))
            
            except Exception:
                _type=0
                
            if _type==5:
                exit(0)
        
        _path = ''  
        
        while os.path.lexists(_path) == False:
            _path = raw_input('\n\n��������ڵ�ɨ��·����')
        
        _Is_Time = False
        
        _Scan_Type = 0
        while _Scan_Type!=1 and _Scan_Type!=2 :
            print('��ѡ��ɨ�����ͣ�')
            print('1�� ����ɨ��\n')
            print('2�� ʱ��ɨ��\n') 
            try:
                _Scan_Type = int(raw_input('��ѡ��'))
            except Exception:
                _Scan_Type = 0
                                        
            if _Scan_Type==1:
                if _type==1:
                    _Get_Files('php',_path)  
                elif _type==2:
                    _Get_Files('jsp',_path)  
                elif _type==3:
                    _Get_Files('asp',_path)  
                elif _type==4:
                    _Get_Files('aspx',_path)   
                    
            elif _Scan_Type==2:
                _True_Time = False
                _time = time.time
                while _True_Time==False:
                    _Str_Time = raw_input('������ʱ��(����2012-12-12 12:12:12)��')
                    try:
                        _time = time.mktime(time.strptime(_Str_Time, '%Y-%m-%d %H:%M:%S'))
                        _True_Time = True
                    except Exception:
                        _Error_Report('-- ʱ���������ȷ ����2012-12-12 12:12:12')
                else:
                    if _type==1:
                        _Get_Time_Files('php',_path,_time)
                    elif _type==2:
                        _Get_Time_Files('jsp',_path,_time)
                    elif _type==3:
                        _Get_Time_Files('asp',_path,_time)
                    elif _type==4:
                        _Get_Time_Files('aspx',_path,_time)   
                
                

    elif len(sys.argv)==5:
        _time = time.time
        try:
            _time = time.mktime(time.strptime(sys.argv[4], '%Y-%m-%d %H:%M:%S'))
        except Exception:
            _Error_Report('-- ʱ���������ȷ ����"2012-12-12 12:12:12"')        
            
        if sys.argv[1].lower() == '-p' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('php',sys.argv[2],_time)
                
        elif sys.argv[1].lower() == '-j' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('jsp',sys.argv[2],_time) 
            
        elif sys.argv[1].lower() == '-a' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('asp',sys.argv[2],_time)       
            
        elif sys.argv[1].lower() == '-x' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('aspx',sys.argv[2],_time)
        else:
            _Error_Report('-- ��������ȷ ')
            return
    else :
        _Error_Report('-- ��������ȷ ')
        return    
    _Is_Con = raw_input('\n�Ƿ����Y/N��').lower()
    if _Is_Con=='y':
        main()

#��ӡLOGO����
def _P_Logo_Code():
    print('\n')
    print('                    /--------\    ')
    print('                  .-          -.    ')
    print('                  /            \    ')
    print('                 |              |   ')
    print('                 |;  .-.  .-.  ;|   ')
    print('                 | )(__/  \__)( |   ')
    print('                 |/     /\     \|   ')
    print('       (@_       (_     ^^     _)   ')
    print('  _     ) \_______\__|IIIIII|__/__________________________')
    print(' (_)@8@8{}<________|-\IIIIII/-|___________________________>  ')
    print('        )_/        \          /     ')
    print('       (@           `--------`      ')
    
    print('\n\n                ����-webshell��ɱ����     ')
    print('                ~~~Coding By Seay~~~   ')
    print('                -->Blog: www.cnseay.com     ')
    print('                ---------------------------    \n')
    
    
#��ӡLOGO
_P_Logo_Code()

#�������
main()