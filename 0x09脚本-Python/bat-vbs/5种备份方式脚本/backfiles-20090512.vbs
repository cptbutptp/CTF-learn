'On Error Resume Next

'===================����ȫ�ֱ���========================
	Dim backpath 'Ŀ�걸��·��
	Dim copys    '������ʷ������Ŀ
	Dim bkspath  'BKS�ļ�����·��
	Dim back2path '�ڶ�����·��
	'-----------------------
	Dim bksname  'BKS�����ļ����������ļ�������������չ����
	Dim delename   'ɾ���ļ��Ĳ�����delete�������ã�
	Dim row        '��ȡ����·��Ŀ¼�µ��ļ���Ŀ
	Dim namearr    '��������·��Ŀ¼�µ��ļ���������
	Dim temppath   '����ɨ���ļ�������ʱ�ļ�������·��
	'-----------------------	 
    Const tempFolder="temp"
    Const tempfile="temp.txt"
	
'=============ִ�й���================================
Function main() 
'-----------�������backpath,copys,bkspath       
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
'-----------��������
   bksname=ExtractFileBodyName(ExtractFileName(bkspath))    ' 
   backpath=backpath&"\"&bksname
   back2path=back2path&"\"&bksname
   temppath=backpath&"\"&tempFolder&"\"&tempfile            '��������ֵtemppath    
   row=getfilelist(temppath)                            
'------------�жϣ�ɾ�������ļ�
 If row >=copys Then 
     namearr=read(row,temppath)                  '��ȡ�ļ�����namearr����
     Do Until row<copys  
     delename=backpath&"\"&namearr(row-copys)   
     deletefiles(delename)
     row=row-1
     Loop
 End If 
'-----------ɾ����ʱ�ļ�
 delename=temppath
 deletefiles(delename)
 delename=backpath&"\"&tempFolder
 deletefolder(delename)
'-----------��ʼ����
	Dim mydate,myfname
	mydate="("&Date()&"-"&DatePart("h",Now())&"-"&DatePart("n",Now())&"-"&DatePart("s",Now())&")"
	myfname=bksname&mydate	
'------------���ݵ���һ����·��
 	Dim WshShell,Path 
    Set WshShell = CreateObject("wscript.Shell")
    path=WshShell.ExpandEnvironmentStrings("%windir%") 	
	WshShell.Run ""&path&"\system32\ntbackup.exe backup ""@"&bkspath&""" /n """&bksname&" ������ 2009-4-30��13:21"" /d ""�������� 2009-4-30��13:21"" /v:no /r:yes /rs:no /hc:off /m normal /j """&bksname&""" /l:s /f """&backpath&"\"&myfname&".bkf""" ,0,True 
	
'------------ѹ�����ݵ��ڶ�����·��
    Const Path7zip="c:\Program Files\7-Zip\7z.exe"
    Dim ziprun
    ziprun=""&Chr(34)&path7zip&chr(34)&" a -tzip "&back2path&"\"&myfname&".zip "&backpath&"\"&myfname&".bkf"
    WshShell.Run ziprun,0,true

End Function

'=================================================================================
Call main()
'===================================���̺�������====================================

'===============��·���л�ȡ�ļ���=======================
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

'=============��ȡ�ı��ļ�������============================
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

'=============��ȡ�ļ����ݵ�����====================
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

'===============ɾ���ļ�==========================
Function deletefiles(filesname)
	Dim fso
	Set fso = CreateObject("scripting.filesystemobject")
	fso.DeleteFile filesname
End Function

'===============ɾ���ļ���==========================
Function deletefolder(foldername)
	Dim fso
	Set fso = CreateObject("scripting.filesystemobject")
	fso.DeleteFolder foldername
End Function

'===============�滻��������========================
Function ReplaceVar(cs)
	cs=Replace(cs,"%yyyy%",DatePart("yyyy",Now()))
	cs=Replace(cs,"%m%",DatePart("m",Now()))	
	ReplaceVar=cs
End Function 
'==================END===================================================================