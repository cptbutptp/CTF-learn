On Error Resume Next
'===================定义全局变量========================
	Dim path(6),message,result,i
'-----------------
    path(1)="C:\Documents and Settings\资料空白\Recent"
    path(2)="C:\Documents and Settings\资料空白\Templates"
    path(3)="C:\Documents and Settings\资料空白\Cookies"
    path(4)="C:\Documents and Settings\资料空白\Local Settings\Temp"
    path(5)="C:\Documents and Settings\资料空白\Local Settings\Temporary Internet Files"
    path(6)="C:\Documents and Settings\资料空白\Local Settings\Temporary Internet Files"
'=============执行过程================================
For i=1 To 6 Step 1
	 result=IsExit(path(i))
	 If result=1 Then 
	 delfiles(path(i))
	 ElseIf result=-1 Then 
	 RemoveDir(path(i))
	 Else WScript.Echo "没找到---"&path(i)
	 End If 
next
'===================================过程函数集合====================================
'------------判断文件or文件夹是否存在 
Function IsExit(ispath)
	Dim fso
	Set fso = CreateObject ("scripting.filesystemobject")
	If fso.FolderExists(ispath)Then
	IsExit =True
	ElseIf fso.FileExists(ispath) Then 
	IsExit=1
	Else IsExit =false
	End If
End Function 
'---------------删除目录(folderspec)下的所有文件及文件夹---------------
Function  RemoveDir(folderspec)    
          Dim   fs ,f
          Set   fs   =   CreateObject("Scripting.FileSystemObject")  
          Set   f   =   fs.GetFolder(folderspec)  
          '---------删除文件夹  
          Set   SubSubFolders   =   f.SubFolders  
          Dim   TempFolder 
          For   Each   TempFolder   In   SubSubFolders  
                     WScript.Echo("成功删除文件夹---"&TempFolder.Name)
                    TempFolder.Delete   True  
          Next  
          '----------删除文件  
          Set   tempFiles   =   f.Files  
          Dim   tempFile
          For   Each   tempFile   In   tempFiles  
                 WScript.Echo("成功删除文件---"&tempFile.Name)
                 tempFile.Delete true              
          Next                    
 End Function 

'----------------删除文件----------------------------------------------------
Function delfiles(filespath)
	Dim fso
	Set fso = CreateObject("scripting.filesystemobject")
    fso.DeleteFile(filespath)
    message="成功删除文件---"&filespath
    WScript.Echo message
End Function 
'==================END===================================================================