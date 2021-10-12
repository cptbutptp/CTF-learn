Dim OperationRegistry
Set OperationRegistry=WScript.CreateObject("WScript.Shell")
OperationRegistry.RegWrite "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ProxyEnable",00000000,"REG_DWORD"
OperationRegistry.RegDelete("HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\AutoConfigURL")
msgbox("OK!The web-proxy has been del.")