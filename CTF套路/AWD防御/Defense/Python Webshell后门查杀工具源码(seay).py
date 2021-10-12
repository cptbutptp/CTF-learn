#coding=gbk

'''
CodIng By Seay
Blog www.cnseay.com
'''

import os
import sys
import datetime
import time

#----------------------特征码数组-----------------------------------

_php_arr = ['eval(','assert(','disk_total_space','wscript.shell','gethostbyname(','cmd.exe','shell.application','touch(','documents and settings','system32','serv-u','','提权','phpspy','后门']
_asp_arr = ['eval(','execute(','wscript.shell','cmd.exe','touch(','documents and settings','system32','serv-u','','提权','aspspy','后门']
_jsp_arr = ['getHostAddress(','wscript.shell','gethostbyname(','cmd.exe','documents and settings','system32','serv-u','','提权','jspspy','后门']
_aspx_arr = ['eval(','UseShellExecute','wscript.shell','cmd.exe','documents and settings','system32','serv-u','','提权','aspxspy','后门']

#----------------------特征码数组-----------------------------------

#脚本文件集合
_Type_list = ['asp', 'php','aspx','jsp','cer','asa','cdx','ashx','ascx' ]


#扫描函数
#获取路径下指定扩展名文件，判断是否存在后门
def _Get_Files(_type,_path):
    
    print('\n')
    print('             可疑文件                   ')
    print('##############################################')
    print('    可疑说明        文件路径               \n')
    
    for _root,_dirs,_files in os.walk(_path):
        for _file in _files:
            
            if _file.find('.')!=-1:
                
                _txt = _file[(_file.rindex('.')+1):]
                
                _Is_Over = False
                
                if _txt==_type : 
                    
                    #读取文件内容
                    _R_Str = open(os.path.join(_root,_file),'r')
                    _Str = _R_Str.read()
                    _R_Str.close()
                    
                    if _type =='php':    #扫描PHP类型的文件
                        for code in _php_arr:
                            if _Str.find(code)!=-1:
                                print('    可疑代码        '+os.path.join(_root,_file))
                                break
                    elif _type =='jsp':  #扫描JSP类型的文件
                        for code in _jsp_arr:
                            if _Str.find(code)!=-1:
                                print('    可疑代码        '+os.path.join(_root,_file))
                                break
                    elif _type =='asp':  #扫描ASP类型的文件
                        for code in _asp_arr:
                            if _Str.lower().find(code)!=-1:
                                print('    可疑代码        '+os.path.join(_root,_file))
                                break                       
                    elif _type =='aspx':  #扫描ASPX类型的文件
                        for code in _aspx_arr:
                            if _Str.find(code)!=-1:
                                print('    可疑代码        '+os.path.join(_root,_file))
                                break    
                    continue
                else:  #判断是否为其他脚本语言
                    for _File_Type in _Type_list:
                        if _File_Type == _txt:
                            print('    '+_File_Type+' 脚本文件    '+os.path.join(_root,_file))  
                            _Is_Over = True
                            break 
                    
                #如果没有特征码，也不是其他脚本文件，就检测是不是畸形文件
                if _Is_Over == False:
                    __FreakFile_Scan(_root,_file) 
        #畸形目录扫描
        _FreakDir_Scan(_root)
            
                


#由文件最后修改时间扫描
def _Get_Time_Files(_type,_path,_time):
    print('\n')
    print('             可疑文件                   ')
    print('#####################################################')
    print('    可疑说明        文件路径           最后修改时间   \n')
        
    for _root,_dirs,_files in os.walk(_path):
        for _file in _files:
            if _file.find('.')!=-1:
                    
                _txt = _file[(_file.rindex('.')+1):]
                    
                if _txt==_type : 
                    _File_Time =os.path.getmtime(_root+'\\'+_file)
                    if _File_Time>_time:
                        print('    时间符合        '+_root+'\\'+_file+'    '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(_root+'\\'+_file))))
    


#畸形文件检测
def __FreakFile_Scan(_root,_FileName):
    if _FileName.find('.')!=-1 and _FileName.count('.')>1:
        if _FileName[_FileName.index('.'):_FileName.rindex('.')].find('php')!=-1:
            print('    畸形文件名      '+os.path.join(_root,_FileName))
    elif _FileName.find('.')!=-1 and _FileName.find(';')!=-1:
        print('    畸形文件名      '+os.path.join(_root,_FileName)) 
                
             

#畸形文件夹检测
def _FreakDir_Scan(_root):
    if _root.find('.') and _root[-(_root.rfind('.')):].lower().find('asp')!=-1:
        print('    畸形目录名      '+os.path.join(_root)) 



#错误报告函数
def _Error_Report(_Err):
    print('  ------------------------------\n\n')
    
    print('  '+_Err+'\n\n')
    
    print('  ------------------------------\n\n')
    
    
    
#main函数-程序入口
def main(): 
    if len(sys.argv)==3 :
        if sys.argv[1].lower()!='-p' and  sys.argv[1].lower()!='-j':
            _Error_Report('-- 扫描类型参数不正确 -p 或者 -j')
            return
        
        if os.path.lexists(sys.argv[2])==False:
            _Error_Report('-- 目录不存在 ')
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
        print('\n  参数说明：\n')
        print('   -p 扫描php文件\n')
        print('   -a 扫描asp文件\n')
        print('   -j 扫描jsp文件\n')
        print('   -x 扫描aspx文件\n')
         
        print('   -t 根据时间扫描\n')
        
        print('   -h 帮助\n')
        
        print('   参数示例：\n')
        print('    s.py –p E:\\wwwroot\n')
        print('    扫描E:\\wwwroot目录下的php文件\n')
            
        print('    s.py –p E:\\wwwroot –t "2012-12-12 12:12:12"\n')
        print('    根据时间“2012-12-12 12:12:12”扫描E:\\wwwroot目录下的php文件\n')
            
        print('    提示：直接运行程序，可根据提示输入扫描参数。\n')
        
        exit(0)
    elif len(sys.argv)==1:
        
        _type = 0
        
        while _type !=1 and _type != 2:
            print('请选择扫描文件类型：\n\n')
            print('1、 PHP\n')
            print('2、 JSP\n')
            print('3、 ASP\n')
            print('4、 ASPX\n')
            print('5、 退出\n\n')
            
            try:
                _type = int(raw_input('请选择：'))
            
            except Exception:
                _type=0
                
            if _type==5:
                exit(0)
        
        _path = ''  
        
        while os.path.lexists(_path) == False:
            _path = raw_input('\n\n请输入存在的扫描路径：')
        
        _Is_Time = False
        
        _Scan_Type = 0
        while _Scan_Type!=1 and _Scan_Type!=2 :
            print('请选择扫描类型：')
            print('1、 常规扫描\n')
            print('2、 时间扫描\n') 
            try:
                _Scan_Type = int(raw_input('请选择：'))
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
                    _Str_Time = raw_input('请输入时间(例：2012-12-12 12:12:12)：')
                    try:
                        _time = time.mktime(time.strptime(_Str_Time, '%Y-%m-%d %H:%M:%S'))
                        _True_Time = True
                    except Exception:
                        _Error_Report('-- 时间参数不正确 例：2012-12-12 12:12:12')
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
            _Error_Report('-- 时间参数不正确 例："2012-12-12 12:12:12"')        
            
        if sys.argv[1].lower() == '-p' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('php',sys.argv[2],_time)
                
        elif sys.argv[1].lower() == '-j' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('jsp',sys.argv[2],_time) 
            
        elif sys.argv[1].lower() == '-a' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('asp',sys.argv[2],_time)       
            
        elif sys.argv[1].lower() == '-x' and sys.argv[3].lower() == '-t':
            _Get_Time_Files('aspx',sys.argv[2],_time)
        else:
            _Error_Report('-- 参数不正确 ')
            return
    else :
        _Error_Report('-- 参数不正确 ')
        return    
    _Is_Con = raw_input('\n是否继续Y/N：').lower()
    if _Is_Con=='y':
        main()

#打印LOGO函数
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
    
    print('\n\n                幻刃-webshell查杀工具     ')
    print('                ~~~Coding By Seay~~~   ')
    print('                -->Blog: www.cnseay.com     ')
    print('                ---------------------------    \n')
    
    
#打印LOGO
_P_Logo_Code()

#程序入口
main()