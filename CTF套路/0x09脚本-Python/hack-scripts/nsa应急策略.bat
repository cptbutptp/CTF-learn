rem �ر����ܿ�����

net stop SCardSvr

net stop SCPolicySvc

sc config SCardSvr start= disabled

sc config SCPolicySvc start= disabled
rem ��������

net start MpsSvc
rem ��������

sc config MpsSvc start= auto
rem ���÷���ǽ

netsh advfirewall set allprofiles state on
rem ���ζ˿�

netsh advfirewall firewall add rule name="deny udp 137 " dir=in protocol=udp localport=137 action=block

netsh advfirewall firewall add rule name="deny tcp 137" dir=in protocol=tcp localport=137 action=block

netsh advfirewall firewall add rule name="deny udp 138" dir=in protocol=udp localport=138 action=block

netsh advfirewall firewall add rule name="deny tcp 138" dir=in protocol=tcp localport=138 action=block

netsh advfirewall firewall add rule name="deny udp 139" dir=in protocol=udp localport=139 action=block

netsh advfirewall firewall add rule name="deny tcp 139" dir=in protocol=tcp localport=139 action=block

netsh advfirewall firewall add rule name="deny udp 445" dir=in protocol=udp localport=445 action=block

netsh advfirewall firewall add rule name="deny tcp 445" dir=in protocol=tcp localport=445 action=block


pause