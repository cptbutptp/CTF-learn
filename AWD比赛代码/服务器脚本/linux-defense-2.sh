#�� /bin/bash

## ��ֹROOTԶ�̵�½
## ������������ǿ�ҽ�����ִ�д˽ű�ǰ�����������û��ܷ�su��rootȨ�ޣ�
## ����������������һ��ʧ�ܶ��˽ű���ִ�н��ᵼ��SSH��½��Զ�޷�ִ��ROOT����

if [ -e /etc/ssh/sshd_config ];then
	echo "File: sshd_config Is Found ..."
	
	## ��ֹROOT�û�Զ�̵�½
	
	if grep -q 'PermitRootLogin no' /etc/ssh/sshd_config ;then
		echo "The PermitRootLogin is configured ..."
		grep 'PermitRootLogin no' /etc/ssh/sshd_config
	elif grep -q '#PermitRootLogin yes' /etc/ssh/sshd_config ;then
		echo "The PermitRootLogin is not configured, Now CONFIGURE it ..."
		sed -i -e '/#PermitRootLogin yes/a\PermitRootLogin no' /etc/ssh/sshd_config
		grep 'PermitRootLogin yes' /etc/ssh/sshd_config
		echo "The PermitRootLogin has been configured, Please Check it out ..."
	else
		echo "Cannot Find Anything About PermitRootLogin, Please Check it out ..."
	fi
else
	echo "File: sshd_config Cannot Be Found, Please Check it in-hand ... "
fi