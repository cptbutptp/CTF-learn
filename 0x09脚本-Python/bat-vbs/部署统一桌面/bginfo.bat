cmd /c
@echo off
%logonserver%\netlogon\bginfo\bginfo.exe /nolicprompt /i%logonserver%\netlogon\bginfo\zhkd.bgi /timer:00
