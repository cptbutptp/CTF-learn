On Error Resume Next

'===================定义全局变量========================
	Dim backpath '目标备份路径
	Dim bkspath  'BKS文件完整路径
	'-----------------------
	Dim bksname  'BKS备份文件名，备份文件名（不包含扩展名）
	Dim back2path
	'--------------定义日志变量
	Dim  mark
	Dim marktime1  '脚本开始运行时间
	Dim marktime2  '脚本结束运行时间
	Dim marktimeoneback  '第一备份时间
	Dim content '日志内容
	'------------程序标记--
    Dim MarkRnd
    MarkRnd=DatePart("n",Now()) 
'------------------
'=============执行过程================================
Function main() 
'-----------传入参数backpath,copys,bkspath       
    Set objArgs = WScript.Arguments       
	Dim p,m()
	p=objArgs.Count
	 If p <>3 Then 
	 Exit Function 
	End if
	ReDim m(p-1)	
    For p=objArgs.Count To 1 Step -1    
    	m(p-1)=objargs(p-1)
    Next  
    backpath=m(0)
    bkspath=m(1)
    back2path=ReplaceVar(m(2))
'-----------变量运算
   mark = backpath&"-"&"MarkFile.txt" 
   bksname=ExtractFileBodyName(ExtractFileName(bkspath))    ' 
   backpath=backpath&"\"&bksname  
   back2path=back2path&"\"&bksname           
'-----------开始备份
	Dim mydate,myfname
	mydate="("&DatePart("yyyy",Now())&"-"&DatePart("m",Now())&"-"&DatePart("d",Now())&"-"&DatePart("h",Now())&"-"&DatePart("n",Now())&"-"&DatePart("s",Now())&")"
	myfname=bksname&"-"&"Daily"&"-"&mydate	
'-----------标记开始时间---time-----
	marktime1=Now()
	content=MarkRnd&"---["&myfname&"]---[脚本开始运行---TIME:"&marktime1&"]"
	WriteToFile mark,content
'------------备份到第一备份路径
 	Dim WshShell,Path 
    Set WshShell = CreateObject("wscript.Shell")
    path=WshShell.ExpandEnvironmentStrings("%windir%") 	
	WshShell.Run ""&path&"\system32\ntbackup.exe backup ""@"&bkspath&""" /n """&bksname&" 创建于 2009-4-30，13:21"" /d ""集创建于 2009-4-30，13:21"" /v:no /r:yes /rs:no /hc:off /m daily /j """&bksname&""" /l:s /f """&backpath&"\"&myfname&".bkf""" ,0,True 	
'-----------标记第一备份完成时间---time-----
	marktimeoneback=Now()
	content=MarkRnd&"---["&myfname&"]---[已经完成第一备份..即将开始第二备份---TIME:"&marktimeoneback&"]"
	WriteToFile mark,content
'------------压缩备份到第二备份路径
  
    Const Path7zip="c:\Program Files\7-Zip\7z.exe"
    Dim ziprun
    ziprun=""&Chr(34)&path7zip&chr(34)&" a -tzip "&back2path&"\"&myfname&".zip "&backpath&"\"&myfname&".bkf"
    WshShell.Run ziprun,0,True
'-----------标记结束时间---------time-----------
	Dim times 
	marktime2=Now()
	times=DateDiff("s",marktime1,marktime2)
	content=MarkRnd&"---["&myfname&"]---[脚本执行完成---TIME:"&marktime2&"]"
	WriteToFile mark,content
    content=MarkRnd&"---["&myfname&"]---[脚本执行时间为---"&Int(times/86400)&"天"&Int(Int(times/3600) Mod 24)&"小时"&Int(Int(times/60) Mod 60)&"分钟"&Int( times Mod 60)&"秒]"
    WriteToFile mark,content
End Function
'=================================================================================
Call main()
'===================================过程函数集合====================================

'===============从路径中获取文件名=======================
Function ExtractFileName(ByVal sFileName )
    Dim nIdx    
    For nIdx=Len(sFileName) To 1 Step -1    
    	If Mid(sFileName,nIdx,1)="\" Then   	
    		ExtractFileName=Mid(sFileName,nIdx+1)
    		Exit function  	
    	End If    
    Next   
    ExtractFileName=sFileName
End Function
'----------------------------
Function ExtractFileBodyName(ByVal sFileName )
    Dim nIdx   
    For nIdx = Len(sFileName) To 1 Step -1
        If Mid(sFileName, nIdx, 1) = "." Then
            ExtractFileBodyName = Mid(sFileName, 1, nIdx-1)
            Exit Function
        End If
    Next 	
	ExtractFileBodyName=sFileName	
End Function 

'===============替换参数变量========================
Function ReplaceVar(cs)
	cs=Replace(cs,"%yyyy%",DatePart("yyyy",Now()))
	cs=Replace(cs,"%m%",DatePart("m",Now()))	
	ReplaceVar=cs
End Function 
'===================向文件写数据========temp=======
Function WriteToFile (filename,filecontent)
     Dim fso
     Set fso = CreateObject("scripting.filesystemobject")
     If IsExitFile (filename)=0 Then
     fso.CreateTextFile filename,True,True 
     End If
     Set f = fso.OpenTextFile(filename,8,False,-1)
     f.WriteLine filecontent   
     f.Close
End Function 
'------------判断文件是否存在
Function IsExitFile(isfile)
	Dim fso
	Set fso = CreateObject ("scripting.filesystemobject")
	If fso.FileExists(isfile)Then
	IsExitFile =True
	Else 
	IsExitFile=False
	End If
End Function 
'==================END===================================================================