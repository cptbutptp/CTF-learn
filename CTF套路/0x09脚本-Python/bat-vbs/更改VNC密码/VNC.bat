echo off
regedit /s \\winlandcn.com\NETLOGON\VNC\vnc-client.reg
echo y|copy \\winlandcn.com\NETLOGON\VNC\vnc-client.reg c:\windows\system32 >> nul
echo on
