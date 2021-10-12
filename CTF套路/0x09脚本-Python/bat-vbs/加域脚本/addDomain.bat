@echo off
ECHO ====此脚本用于手动添加到域====
echo=========请选择部门============
ECHO 1. 佧邦崎
ECHO 2. 威乐办公
ECHO 3. 新信兴美
ECHO 4. 新信创意
ECHO 5. 新信礼品
ECHO 6. 新信集团
ECHO 7. 繁体工作站

set OU=
set/p OU=请输入上面OU的序号并回车:

if %OU% EQU 1 (set OUName=佧邦崎)
if %OU% EQU 2 (set OUName=威乐办公)
if %OU% EQU 3 (set OUName=新信兴美)
if %OU% EQU 4 (set OUName=新信创意)
if %OU% EQU 5 (set OUName=新信礼品)
if %OU% EQU 6 (set OUName=新信集团)
if %OU% EQU 7 (set OUName=繁体工作站)


set username=
set/p username=请输入您的用户名：

set password=
set/p password=请输入您的密码：

netdom join %computername% /Domain:winlandcn\ems /ou:ou=%OUName%,ou="工作站",dc=winlandcn,dc=com /Userd:winlandcn\%username% /Passwordd:%password%

ECHO =========添加完成!===========


