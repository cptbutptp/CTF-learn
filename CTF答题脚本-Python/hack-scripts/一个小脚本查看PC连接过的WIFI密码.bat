@echo off

echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo +    0.��ʹ�ù���ԱȨ������,��������鿴C�̵�WifiPassword�ļ��С� +              
echo +    1.WifiPassword�е��ļ���ʹ���ı��༭���ߴ򿪡�               +
echo +    2.��WifiPassword�е��ļ���,keyMaterial��ǩ������������롣 +
echo +    3.����һ����ѯ��ʷ���ӳɹ�������������С����,���������ƽ⣡  +
echo +                                           by:www.3ecurity.com   +
echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ipconfig | find "���߾����������� "
echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

set /p WifiName=�����롾���߾�������������������ַ���:

md C:\WifiPassword

netsh wlan export  profile interface=%WifiName% key=clear folder=C:\WifiPassword

echo �밴������˳�:)

Set /p Enter=""