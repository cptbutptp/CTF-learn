'On Error Resume Next
'=========数据连接===========================================
Set dbconn = wscript.CreateObject("ADODB.Connection")
dbconn.Open"driver={sql server};Server=onepeople;Database=test;uid=sa;pwd=123456;"
'============================================================

main()
'===================================
'----------------运行主函数
'===================================
Function main ()
Dim main_num
	main_num=InputBox ("please input num"&vbCr&"1.查询---2.插入---3.删除","请输入数据库操作类型:")
	If main_num="" Or main_num=Null Then 
	  MsgBox "请重新输入!"
	  call main
	  Exit Function 
	ElseIf main_num="Exit" Or main_num="exit" Then
	  Exit function
	End If 
	
	Select Case main_num
	     Case 1    
	     	operate_data 1,selectdata 
	     Case 2
	     	operate_data 2,insertdata  
	     Case 3
	        operate_data 3,deletedata
	     Case Else	msgbox "你输入错误!"
	End Select

dbconn.Close    
End Function                                   '关闭数据库
'====================================
'----------------结束
'=================================


'=============================带返回值的函数集合==============================================================================
'==============查询数据函数(1)=========
Function  selectdata()
'selectnum为查询的字段，selectdata为查询的内容
	Dim select_num,select_content,showcontent,select_var
	select_num=InputBox ("please input num"&vbCr&"1.电脑名---2.IP地址---3.用户名---4.所有数据","请输入查询对象:")
    If select_num=Null Or select_num="" Then 
        selectdata=false
    	Exit Function 
    End If 
	Select Case select_num
	     Case 1     
		     showcontent="电脑名"
		     select_var="com_name"
		     select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 2	    
	    	 showcontent="IP地址"
	    	 select_var="com_ip" 
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 3     
	    	 showcontent="用户名"
	    	 select_var="user_name"
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 4
	         selectdata="select * from computer" 
	     Case Else	
	         msgbox "你输入错误!"
	         selectdata=false
	End Select	
End Function 
'===============End sub=======

'===================插入数据过程(2)=============================
Function  insertdata()
    Dim name,user,psw,ip,yesorno
    '---------输入插入的数据
	name=InputBox("please input name","请输入电脑名:")
	user=InputBox ("please input user","请输入用户名:")
	psw=InputBox ("please input psw","请输入密码:")
	ip=InputBox ("please input ip","请输入IP地址:")
	If name="" Or user="" Or psw="" Or ip="" Then 
		insertdata=False
		MsgBox "Error!内容不能为空!"
		Call insertdata
		Exit Function 
		End If 
	name="'"&name&"'"
	user="'"&user&"'"
	psw="'"&psw&"'"
	ip="'"&ip&"'"

    '---------插入数据库
	insertdata="insert into computer (com_name,user_name,user_psw,com_ip) values ("&name&","&user&","&psw&","&ip&")"
End Function  
'=====================end sub ==========================

'==============删除数据过程=========
Function deletedata()
  Dim select_num,select_content,showcontent,select_var
	select_num=InputBox ("please input num"&vbCr&"1.电脑名---2.IP地址---3.用户名---4.所有数据","请输入查询对象:")
    If select_num=Null Or select_num="" Then 
        selectdata=false
    	Exit Function 
    End If 
	Select Case select_num
	     Case 1     
		     showcontent="电脑名"
		     select_var="com_name"
		     select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 2	    
	    	 showcontent="IP地址"
	    	 select_var="com_ip" 
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 3     
	    	 showcontent="用户名"
	    	 select_var="user_name"
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"请输入"&showcontent&"内容:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 4
	         selectdata="select * from computer" 
	     Case Else	
	         msgbox "你输入错误!"
	         deletedata=false
	End Select	
End Function 
'===================================
'--------------------------------------子函数集合-------------------------------------------------

'===============操作数据函数=============
Function operate_data(operate_num,operate_cmd)
	If operate_cmd=false Then 
	   Exit Function
	End if
	Select Case operate_num
	   Case 0    '-------------0查询
		   Set rs=dbconn.Execute(operate_cmd)
			If rs.BOF Then
			   operate_data=false
			   Else operate_data=true 
			End If     
	   Case 1    '-------------1显示
	 	  	show_data(operate_cmd)
	   Case 2    '-------------2插入
	   		insert_data(operate_cmd)
	   Case 3
	        delete_data(operate_cmd)
	 End select
End Function 



  '-------------1显示子函数
Function show_data(show_cmd)
    Dim name,user,psw,ip
	
	Set rs=dbconn.Execute(show_cmd)
	If rs.EOF Then
	  WScript.Echo "Sorry!数据查询失败!"
	  Exit Function 
	End If

	While Not rs.eof 
		name=rs(1).Value
	    user=rs(2).Value
	    psw=rs(3).Value
	    ip=rs(4).Value
	    WScript.Echo ("您需要查询的数据是:"&vbcr&vbcr&"电脑名:"&name&"---IP地址:"&ip&"---用户:"&user&"---密码:******")
	    rs.MoveNext 
	Wend
End Function 
'--------------------------
'--------------2
Function insert_data(insert_cmd)
	Set rs=dbconn.Execute(insert_cmd)

End Function 
'--------------3
Function delete_data(delete_cmd)
	Set rs=dbconn.Execute(delete_cmd)
End Function 