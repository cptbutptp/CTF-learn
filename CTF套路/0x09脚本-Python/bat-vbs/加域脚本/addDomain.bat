@echo off
ECHO ====�˽ű������ֶ���ӵ���====
echo=========��ѡ����============
ECHO 1. ������
ECHO 2. ���ְ칫
ECHO 3. ��������
ECHO 4. ���Ŵ���
ECHO 5. ������Ʒ
ECHO 6. ���ż���
ECHO 7. ���幤��վ

set OU=
set/p OU=����������OU����Ų��س�:

if %OU% EQU 1 (set OUName=������)
if %OU% EQU 2 (set OUName=���ְ칫)
if %OU% EQU 3 (set OUName=��������)
if %OU% EQU 4 (set OUName=���Ŵ���)
if %OU% EQU 5 (set OUName=������Ʒ)
if %OU% EQU 6 (set OUName=���ż���)
if %OU% EQU 7 (set OUName=���幤��վ)


set username=
set/p username=�����������û�����

set password=
set/p password=�������������룺

netdom join %computername% /Domain:winlandcn\ems /ou:ou=%OUName%,ou="����վ",dc=winlandcn,dc=com /Userd:winlandcn\%username% /Passwordd:%password%

ECHO =========������!===========


