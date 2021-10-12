AWD攻防赛参考思路：

本次比赛环境：
	Windows+Linux组合模式：
	Windows Server 2003 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01
	Window7 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01
	Windows Server 2008 + Centos6.x/Ubuntu14/16.04/Ubuntu17.01

Windows加固：
	先备份：Web源码、数据库
	1.445加固,开启防火墙或IP高级安全策略
	2.开启系统日志审计功能
	3.禁用guest账户、关闭文件共享
	4.确保启动项内容是可控的
	5.限制3389远程访问控制的连接数
		在本地组策略编辑器里面，依次展开计算机配置--->管理模板--->Windows组件--->远程桌面服务--->远程桌面会话主机--->连接--->限制连接的数量。
	6.使用工具监控关键目录文件:
		文件操作监控.exe/御剑文件监控.exe
	7.恶意代码文件，通过PCHunter,Monitor查找
	8.Web目录环境查找相关可疑文件：jpg/png/rar,属性、解压
	9.NTFS扫描磁盘查找隐藏的交换流数据
	10.查找系统所有账户信息，禁止非administrator账户
	11.修改Web站点管理员访问路径、默认口令、数据库口令
	12.安装WAF脚本，防护web站点，禁止其他漏洞

Linux加固：
	先备份：Web源码、数据库
	1.系统口令修改，团队统一口令
	2.通过.bash_history查找历史命令操作，发现痕迹
	3.查看计划任务：crontab -l；编辑计划任务:crontab -e
	4.查看/etc/init.d/rc.local中启动服务有无异常
	5.使用脚本开启进程监控、目录监控、流量监控
	6.Web站点口令,站点管理员路径修改
	7.系统加固：iptable
		进程线程：netstat / ps -aux/netstat -apt
		ssh：w/fuser 
		杀掉进程：kill  -9 pid

Mysql加固：
	1.不使用默认口令，修改成复杂的，并确保和web环境连接
	2.设置只允许本地127.0.0.1账户登录
	修改bind-address=127.0.0.1
	在配置文件中加入seccure_file_priv=NULL
	3.开启日志审计功能：general_log_file=路径

Mssql加固：
	1.删除不必要的账号	
	2.SQLServer用户口令安全	
	3.根据用户分配帐号避免帐号共享
	4.分配数据库用户所需的最小权限
	5.网络访问限制
	6.SQLServer登录审计
	7.SQLServer安全事件审计
	8.配置日志功能


攻击准备：
	1.各类CMS软件包最新版准备
	2.扫描工具：nmap、nessus、metasploit更新
	2.漏洞利用脚本poc、exp
kali更新，解决kali更新签名问题：
wget -q -O - https://archive.kali.org/archive-key.asc  | apt-key add
	uname -a
	cat /proc/version
	Windows提权：
	ms17-017
	ms17-010


	Linux提权：
	CVE-2017-6074 (DCCP双重释放漏洞 > 2.6.18 ）
	CVE-2016-5195（脏牛，kernel 2.6.22 < 3.9 (x86/x64)）
	CVE-2016-8655（Ubuntu 12.04、14.04，Debian 7、8）
	CVE-2017-1000367（sudo本地提权漏洞 ）
	CVE-2016-1247（Nginx权限提升漏洞）
	CVE-2017-16995(Ubuntu16.04   kernel:4.14-4.4)
中间件服务器：
	iis
	apache
	jboss
	mysql
	nginx
	tomcat
	weblogic

集成服务环境：
	wampserver
	xamppserver

CMS列表参考：
下载最新版本+每个CMS对应的漏洞poc、exp工具脚本文章，之后汇总
	apache
	aspcms
	dedecms
	dicuz
	drupal
	empirecms
	eshop
	finecms
	joomla
	lamp
	metainfo
	nginx
	phpcms
	phpwind
	qibocms
	seacms
	semcms
	tomcat
	wolfcms
	wordpress
	zabbix

参考链接：

http://freebuf.com/
https://github.com/Huseck
https://www.seebug.org/
https://www.anquanke.com/
https://www.exploit-db.com/
http://www.bugscan.net/source/template/vulns/


