@echo off
ECHO ====此脚本用于手动开启远程桌面====

set machinename=
set/p machinename=请输入目标机器名/IP地址：

set username=
set/p username=请输入您的帐号：

Wmic /node:"%machinename%" /USER:"%username%" PATH win32_terminalservicesetting WHERE (__Class!="") CALL SetAllowTSConnections 1 

ECHO =========添加完成!===========


