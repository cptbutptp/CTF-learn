'On Error Resume Next
'=========��������===========================================
Set dbconn = wscript.CreateObject("ADODB.Connection")
dbconn.Open"driver={sql server};Server=onepeople;Database=test;uid=sa;pwd=123456;"
'============================================================

main()
'===================================
'----------------����������
'===================================
Function main ()
Dim main_num
	main_num=InputBox ("please input num"&vbCr&"1.��ѯ---2.����---3.ɾ��","���������ݿ��������:")
	If main_num="" Or main_num=Null Then 
	  MsgBox "����������!"
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
	     Case Else	msgbox "���������!"
	End Select

dbconn.Close    
End Function                                   '�ر����ݿ�
'====================================
'----------------����
'=================================


'=============================������ֵ�ĺ�������==============================================================================
'==============��ѯ���ݺ���(1)=========
Function  selectdata()
'selectnumΪ��ѯ���ֶΣ�selectdataΪ��ѯ������
	Dim select_num,select_content,showcontent,select_var
	select_num=InputBox ("please input num"&vbCr&"1.������---2.IP��ַ---3.�û���---4.��������","�������ѯ����:")
    If select_num=Null Or select_num="" Then 
        selectdata=false
    	Exit Function 
    End If 
	Select Case select_num
	     Case 1     
		     showcontent="������"
		     select_var="com_name"
		     select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 2	    
	    	 showcontent="IP��ַ"
	    	 select_var="com_ip" 
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 3     
	    	 showcontent="�û���"
	    	 select_var="user_name"
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 4
	         selectdata="select * from computer" 
	     Case Else	
	         msgbox "���������!"
	         selectdata=false
	End Select	
End Function 
'===============End sub=======

'===================�������ݹ���(2)=============================
Function  insertdata()
    Dim name,user,psw,ip,yesorno
    '---------������������
	name=InputBox("please input name","�����������:")
	user=InputBox ("please input user","�������û���:")
	psw=InputBox ("please input psw","����������:")
	ip=InputBox ("please input ip","������IP��ַ:")
	If name="" Or user="" Or psw="" Or ip="" Then 
		insertdata=False
		MsgBox "Error!���ݲ���Ϊ��!"
		Call insertdata
		Exit Function 
		End If 
	name="'"&name&"'"
	user="'"&user&"'"
	psw="'"&psw&"'"
	ip="'"&ip&"'"

    '---------�������ݿ�
	insertdata="insert into computer (com_name,user_name,user_psw,com_ip) values ("&name&","&user&","&psw&","&ip&")"
End Function  
'=====================end sub ==========================

'==============ɾ�����ݹ���=========
Function deletedata()
  Dim select_num,select_content,showcontent,select_var
	select_num=InputBox ("please input num"&vbCr&"1.������---2.IP��ַ---3.�û���---4.��������","�������ѯ����:")
    If select_num=Null Or select_num="" Then 
        selectdata=false
    	Exit Function 
    End If 
	Select Case select_num
	     Case 1     
		     showcontent="������"
		     select_var="com_name"
		     select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 2	    
	    	 showcontent="IP��ַ"
	    	 select_var="com_ip" 
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 3     
	    	 showcontent="�û���"
	    	 select_var="user_name"
	    	 select_content="'"&InputBox ("please input "&showcontent&""&vbCr,"������"&showcontent&"����:")&"'"
	         selectdata="select * from computer where "&select_var&"="&select_content&""
	     Case 4
	         selectdata="select * from computer" 
	     Case Else	
	         msgbox "���������!"
	         deletedata=false
	End Select	
End Function 
'===================================
'--------------------------------------�Ӻ�������-------------------------------------------------

'===============�������ݺ���=============
Function operate_data(operate_num,operate_cmd)
	If operate_cmd=false Then 
	   Exit Function
	End if
	Select Case operate_num
	   Case 0    '-------------0��ѯ
		   Set rs=dbconn.Execute(operate_cmd)
			If rs.BOF Then
			   operate_data=false
			   Else operate_data=true 
			End If     
	   Case 1    '-------------1��ʾ
	 	  	show_data(operate_cmd)
	   Case 2    '-------------2����
	   		insert_data(operate_cmd)
	   Case 3
	        delete_data(operate_cmd)
	 End select
End Function 



  '-------------1��ʾ�Ӻ���
Function show_data(show_cmd)
    Dim name,user,psw,ip
	
	Set rs=dbconn.Execute(show_cmd)
	If rs.EOF Then
	  WScript.Echo "Sorry!���ݲ�ѯʧ��!"
	  Exit Function 
	End If

	While Not rs.eof 
		name=rs(1).Value
	    user=rs(2).Value
	    psw=rs(3).Value
	    ip=rs(4).Value
	    WScript.Echo ("����Ҫ��ѯ��������:"&vbcr&vbcr&"������:"&name&"---IP��ַ:"&ip&"---�û�:"&user&"---����:******")
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