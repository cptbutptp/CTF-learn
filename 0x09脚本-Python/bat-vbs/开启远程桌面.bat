@echo off
ECHO ====�˽ű������ֶ�����Զ������====

set machinename=
set/p machinename=������Ŀ�������/IP��ַ��

set username=
set/p username=�����������ʺţ�

Wmic /node:"%machinename%" /USER:"%username%" PATH win32_terminalservicesetting WHERE (__Class!="") CALL SetAllowTSConnections 1 

ECHO =========������!===========


