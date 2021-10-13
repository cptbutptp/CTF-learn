#！ /bin/bash

## 禁止ROOT远程登陆
## ！！！！！！强烈建议在执行此脚本前测试新增的用户能否su到root权限，
## ！！！！！！否则一旦失败而此脚本被执行将会导致SSH登陆永远无法执行ROOT操作

if [ -e /etc/ssh/sshd_config ];then
	echo "File: sshd_config Is Found ..."
	
	## 禁止ROOT用户远程登陆
	
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