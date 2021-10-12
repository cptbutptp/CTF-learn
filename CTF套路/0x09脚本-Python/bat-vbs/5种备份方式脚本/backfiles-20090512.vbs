'On Error Resume Next

'===================定义全局变量========================
	Dim backpath '目标备份路径
	Dim copys    '保存历史备份数目
	Dim bkspath  'BKS文件完整路径
	Dim back2path '第二备份路径
	'-----------------------
	Dim bksname  'BKS备份文件名，备份文件名（不包含扩展名）
	Dim delename   '删除文件的参数（delete函数调用）
	Dim row        '获取备份路径目录下的文件数目
	Dim namearr    '包含备份路径目录下的文件名的数组
	Dim temppath   '包含扫描文件名的临时文件的完整路径
	'-----------------------	 
    Const tempFolder="temp"
    Const tempfile="temp.txt"
	
'=============执行过程================================
Function main() 
'-----------传入参数backpath,copys,bkspath       
    Set objArgs = WScript.Arguments       
	Dim p,m()
	p=objArgs.Count
	 If p <>4 Then 
	 Exit Function 
	End if
	ReDim m(p-1)	
    For p=objArgs.Count To 1 Step -1    
    	m(p-1)=objargs(p-1)
    Next  
    backpath=ReplaceVar(m(0))
    copys=CInt(m(1))
    bkspath=m(2)
    back2path=ReplaceVar(m(3))    
'-----------变量运算
   bksname=ExtractFileBodyName(ExtractFileName(bkspath))    ' 
   backpath=backpath&"\"&bksname
   back2path=back2path&"\"&bksname
   temppath=backpath&"\"&tempFolder&"\"&tempfile            '给变量赋值temppath    
   row=getfilelist(temppath)                            
'------------判断，删除多余文件
 If row >=copys Then 
     namearr=read(row,temppath)                  '获取文件名到namearr数组
     Do Until row<copys  
     delename=backpath&"\"&namearr(row-copys)   
     deletefiles(delename)
     row=row-1
     Loop
 End If 
'-----------删除临时文件
 delename=temppath
 deletefiles(delename)
 delename=backpath&"\"&tempFolder
 deletefolder(delename)
'-----------开始备份
	Dim mydate,myfname
	mydate="("&Date()&"-"&DatePart("h",Now())&"-"&DatePart("n",Now())&"-"&DatePart("s",Now())&")"
	myfname=bksname&mydate	
'------------备份到第一备份路径
 	Dim WshShell,Path 
    Set WshShell = CreateObject("wscript.Shell")
    path=WshShell.ExpandEnvironmentStrings("%windir%") 	
	WshShell.Run ""&path&"\system32\ntbackup.exe backup ""@"&bkspath&""" /n """&bksname&" 创建于 2009-4-30，13:21"" /d ""集创建于 2009-4-30，13:21"" /v:no /r:yes /rs:no /hc:off /m normal /j """&bksname&""" /l:s /f """&backpath&"\"&myfname&".bkf""" ,0,True 
	
'------------压缩备份到第二备份路径
    Const Path7zip="c:\Program Files\7-Zip\7z.exe"
    Dim ziprun
    ziprun=""&Chr(34)&path7zip&chr(34)&" a -tzip "&back2path&"\"&myfname&".zip "&backpath&"\"&myfname&".bkf"
    WshShell.Run ziprun,0,true

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

'=============获取文本文件总行数============================
Function getfilelist(filepath)
	Dim WshShell,command1,command2
	getfilelist=0
	command1="cmd.exe /c md "&backpath&"\"&tempFolder&""    
    command2="cmd.exe /c dir "&backpath&" /a-d /o-d /b >"&temppath&""   
	set WshShell = CreateObject("wscript.Shell")
	WshShell.Run command1,0,true
	WshShell.Run command2,0,True
	Const ForReading = 1
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	Set objTextFile = objFSO.OpenTextFile _
	    (filepath, ForReading)
	Do Until objTextFile.AtEndOfStream
	    strNextLine = objTextFile.Readline
	    getfilelist=getfilelist+1  
	Loop
	objTextFile.Close 
End Function

'=============读取文件内容到数组====================
Function read(readrow,readpath) 
  If readrow<=0 Then
  Exit Function 
  End If 
  Dim readnamearr
  ReDim readnamearr(readrow-1)
  Const ForReading = 1
  Set objFSO = CreateObject("Scripting.FileSystemObject")
  Set objTextFile = objFSO.OpenTextFile _
    (readpath, ForReading)    
    Dim i
    For i=readrow To 1 Step -1
       readnamearr(i-1) = objTextFile.Readline
    Next 
   read=readnamearr
   objTextFile.Close 
End Function

'===============删除文件==========================
Function deletefiles(filesname)
	Dim fso
	Set fso = CreateObject("scripting.filesystemobject")
	fso.DeleteFile filesname
End Function

'===============删除文件夹==========================
Function deletefolder(foldername)
	Dim fso
	Set fso = CreateObject("scripting.filesystemobject")
	fso.DeleteFolder foldername
End Function

'===============替换参数变量========================
Function ReplaceVar(cs)
	cs=Replace(cs,"%yyyy%",DatePart("yyyy",Now()))
	cs=Replace(cs,"%m%",DatePart("m",Now()))	
	ReplaceVar=cs
End Function 
'==================END===================================================================