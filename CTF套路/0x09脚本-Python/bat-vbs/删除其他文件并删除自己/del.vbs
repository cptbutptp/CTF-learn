'本脚本用来删除驱动文件夹，删除启动自身的注册表，删除龙帝国DLL，删除自身

On Error Resume Next                                 '防止出现错误

Set fso = CreateObject("Scripting.FileSystemObject") '创建文件对象FSO

mystr=msgbox(" 本脚本将删除驱动残留！",48,"注意：")   '弹出提示框删除驱动

'删除脚本自身
WScript.Sleep 1000                                    '将脚本执行挂起1秒
fso.DeleteFile(WScript.ScriptfullName) 

'删除驱动文件夹
If fso.folderExists("c:\drivers") Then 
 fso.Deletefolder("c:\drivers"),true
 end if

'删除龙帝国DLL
if fso.fileexists("C:\WINDOWS\DllCacheManager.exe") then
 fso.deletefile("C:\WINDOWS\DllCacheManager.exe"),true
set fso=nothing
end if

'删除启动自身注册表项目
Dim OperationRegistry
Set OperationRegistry=WScript.CreateObject("WScript.Shell")
OperationRegistry.RegDelete("HKLM\Software\Microsoft\Windows\CurrentVersion\RUN\del")
