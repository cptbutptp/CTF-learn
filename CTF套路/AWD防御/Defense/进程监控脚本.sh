#!/bin/bash
IP=`ifconfig eth0 | grep "inet addr" | cut -f 2 -d ":" | cut -f 1 -d " "`
tomcat_dir="/opt/apache-tomcat-7.0.8"
mysql_dir="/usr/local/mysql/bin/mysqld_safe"
vsftp_dir="/usr/sbin/vsftpd"
ssh_dir="/usr/sbin/sshd"
for dir in $tomcat_dir $mysql_dir $vsftp_dir  $ssh_dir 
do
process_count=$(ps -ef | grep "$dir" | grep -v grep | wc -l)
        for service in tomcat mysql vsftp ssh 
        do
                echo "$dir" |grep -q "$service"
                if [ $? -eq 0 ]
                then
                        if [ $process_count -eq 0 ]
                        then
                            echo "$service is down at $(date +%Y%m%d%H:%M:%S)" >>/usr/monitor/process/process_$(date +%Y%m%d).log
                            echo "$service is down at $(date +%Y%m%d%H:%M:%S)" | mail -s "$IP服务器 $service服务关闭告警" XXXX@qq.com
                        else
                            echo "$service is running at $(date +%Y%m%d%H:%M:%S)" >>/usr/monitor/process/process_$(date +%Y%m%d).log
                        fi
                else
                        continue
                fi
        done
done