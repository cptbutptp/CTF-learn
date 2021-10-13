#�� /bin/bash

## Shell Script For Linux OS Defence, Depends on CentOS 7��Version 1.0, Written By CaiMengChen 2016-06-13
## Maybe You Need To Restart Linux After Execute This Shell Script

echo "Start To Run This Script ......"
## ����˻���������

echo "***************************************************************"
echo "***************************************************************"
echo "***************************************************************"
if [ -e /etc/pam.d/system-auth ];then
	echo "File: system-auth Is Found, Now Check String "pam_tally.so" ..."
	
	## �ж�pam_tally�Ƿ��Ѿ����ڣ�����Ѿ����ڷ���ֵ$?Ϊ0��������$?����ֵΪ1
	## grep -q ����ӡ�κα�׼����������ƥ���������������״ֵ̬0,û��ƥ���򷵻�״ֵ̬1
	## Linux�µ�if�ж����0ֵΪ�棬��C���������෴

	if grep	-q 'pam_tally' /etc/pam.d/system-auth ;then
		echo "The pam_tally has already been configured, Please Check it in-hand ..."
		grep 'pam_tally' /etc/pam.d/system-auth
	else
		echo "The pam_tally is not configured, Now CONFIGURE it ..."
		sed -i -e '/pam_env.so/a\auth        required      pam_tally.so onerr=fail deny=3 unlock_time=300' /etc/pam.d/system-auth
		grep 'pam_tally' /etc/pam.d/system-auth
		echo "The pam_tally has been configured, Please Check it out ..."
	fi
else
	echo "File: system-auth Cannot Be Found, Please Check it in-hand ... "
fi

## ����һ��Զ�̵�½�˻���������su��ROOTȨ�ޣ���ֹ�����κ��û�su��ROOTȨ�ޣ����ҹر�ROOT�û���Զ�̵�½Ȩ��
## ����su���û�������wheel���У�usermod -G wheel �û���
echo "***************************************************************"
echo "***************************************************************"
echo "***************************************************************"

useradd justforssh
usermod -G wheel justforssh  
passwd justforssh

## �����½��û�su��ROOTȨ�ޣ���ֹ�����û�su��ROOTȨ��

if [ -e /etc/pam.d/su ];then
	echo "File: su Is Found, Now Check String "pam_wheel.so use_uid" ..."
	
	## �ж�"#auth required pam_wheel.so use_uid"�Ƿ��Ѿ����ڣ�����Ѿ����ڷ���ֵ$?Ϊ0��������$?����ֵΪ1
	## grep -q ����ӡ�κα�׼����������ƥ���������������״ֵ̬0,û��ƥ���򷵻�״ֵ̬1
	## Linux�µ�if�ж����0ֵΪ�棬��C���������෴

	if grep	-q '#.*pam_wheel.so use_uid' /etc/pam.d/su ;then
		echo "The pam_wheel.so group is not configured, configure it now..."
		sed -i -e 's/#.*pam_wheel.so use_uid/auth\t\trequired\tpam_wheel.so use_uid/' /etc/pam.d/su
		grep 'pam_wheel.so use_uid' /etc/pam.d/su
	elif grep -q 'auth.*pam_wheel.so use_uid' /etc/pam.d/su ;then
		echo "The pam_wheel.so group is already configured, Please check it out..."
		grep 'pam_wheel.so use_uid' /etc/pam.d/su
	else
		sed -i -e '$a auth\t\trequired\tpam_wheel.so use_uid' /etc/pam.d/su
	fi
else
	echo "File: su Cannot Be Found, Please Check it in-hand ... "
fi

## �鿴SSH�汾����������������
echo "***************************************************************"
echo "***************************************************************"
echo "***************************************************************"

if [ -e /etc/ssh/sshd_config ];then
	echo "File: sshd_config Is Found ..."
				
	## �޸�SSH�汾Ϊ2����ȡֱ��ɾ��ע�͵ķ�ʽ
	
	if grep	-q '#Protocol 2' /etc/ssh/sshd_config ;then
		echo "The Protocol is not configured, Now CONFIGURE it ..."
		sed -i -e 's/#Protocol 2/Protocol 2/' /etc/ssh/sshd_config
		grep 'Protocol 2' /etc/ssh/sshd_config
		echo "The Protocol has been configured, Please Check it out ..."
	elif grep -q 'Protocol 2' /etc/ssh/sshd_config ;then
		echo "The Protocol has already been configured ..."
		grep 'Protocol 2' /etc/ssh/sshd_config
	else
		echo "Cannot Find Anything About Protocol, Please Check it out ..."
	fi
	
	## �޸���������������Ϊ3��ֱ���޸�ע���ļ���ȥ��ע�Ͳ���ֵ
	
	if grep	-q '#MaxAuthTries' /etc/ssh/sshd_config ;then
		echo "The MaxAuthTries is not configured, Now CONFIGURE it ..."
		sed -i -e 's/#MaxAuthTries.*/MaxAuthTries 3' /etc/ssh/sshd_config

	elif grep -q 'MaxAuthTries' /etc/ssh/sshd_config ;then
		sed -i -e 's/MaxAuthTries.*/MaxAuthTries 3' /etc/ssh/sshd_config
		
	else
		sed -i -e '$a MaxAuthTries 3' /etc/ssh/sshd_config
		
	fi
	
	grep 'MaxAuthTries' /etc/ssh/sshd_config
	echo "The MaxAuthTries has been configured, Please Check it out ..."
	
	## �޸����������Ϊ2��ֱ���޸�ע���ļ���ȥ��ע�Ͳ���ֵ
	if grep	-q '#MaxSessions' /etc/ssh/sshd_config ;then
		echo "The MaxSessions is not configured, Now CONFIGURE it ..."
		sed -i -e 's/#MaxSessions.*/MaxSessions 2' /etc/ssh/sshd_config

	elif grep -q 'MaxSessions' /etc/ssh/sshd_config ;then
		sed -i -e 's/MaxSessions.*/MaxSessions 2' /etc/ssh/sshd_config
		
	else
		sed -i -e '$a MaxSessions 2' /etc/ssh/sshd_config
		
	fi
	
	grep 'MaxSessions' /etc/ssh/sshd_config
	echo "The MaxSessions has been configured, Please Check it out ..."
	
	echo "!!!!!!!!!!!!!!!!!!!!!!"
	echo "Now Restart SSH Server"
	service sshd restart
	
else
	echo "File: sshd_config Cannot Be Found, Please Check it in-hand ... "
fi

## �޸���ҪĿ¼���ĵ���Ȩ��
#echo "***************************************************************"
#echo "***************************************************************"
#echo "***************************************************************"

#chmod 700 /bin/rpm
#chmod 600 /etc/exports
#chmod 600 /etc/hosts.*
#chmod 644 /var/log/messages
#chmod 640 /etc/syslog.conf
#chmod 660 /var/log/wtmp
#chmod 640 /var/log/lastlog
#chmod 600 /etc/ftpusers
#chmod 644 /etc/passwd
#chmod 600 /etc/shadow
#chmod 600 /etc/lilo.conf
#chmod 600 /etc/securetty
#chmod 400 /etc/shutdown.allow
#chmod 700 /etc/security
#chmod 600 /etc/xinetd.conf
#chmod 600 /etc/inetd.conf
#chmod 750 /etc/rc.d/init.d/*
#chmod 600 /etc/crontab
#chmod 400 /etc/cron.*
#chmod 750 /etc/ssh
#chmod 400 /etc/sysctl.confg
#chmod -R 750 /etc/pam.d
#chmod -R 751 /etc/sysconfig
#chmod -R 750 /etc/rc.d/init.d/

#echo "==============================================================="
#echo "The Authority of These Directories and Files Have Been Changed:"
#echo "/bin/rpm---700			/etc/exports---600	/etc/hosts.*---600	/var/log/messages---644"
#echo "/etc/syslog.conf---640		/var/log/wtmp---660	/var/log/lastlog---640	/etc/ftpusers---600"
#echo "/etc/passwd---644		/etc/shadow---600	/etc/lilo.conf---600	/etc/securetty---600"
#echo "/etc/shutdown.allow---400	/etc/security---700	/etc/xinetd.conf---600	/etc/inetd.conf---600"
#echo "/etc/rc.d/init.d/*---750	/etc/crontab---600	/etc/cron.*---400	/etc/ssh---750"
#echo "/etc/sysctl.confg---400	/etc/pam.d---750	/etc/sysconfig---751	/etc/rc.d/init.d/---750"
#echo "==============================================================="

#echo "***************************************************************"
#echo "***************************************************************"
#echo "***************************************************************"

echo "Scirpt Runs Completed ......"