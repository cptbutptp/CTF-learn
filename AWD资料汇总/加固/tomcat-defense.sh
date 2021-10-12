#！ /bin/bash

## Shell Script For Tomcat Defence, Version 2.0, Written By CaiMengChen 2016-06-12
## Tested on Tomcat 9、 Tomcat 8、 Tomcat 6、 Tomcat 5
## !!!!!IMPORTANT!!!!! You Need To Restart Tomcat Server After Execute This Shell Script

date
echo "Start Running Script Tomcat Defence"

## Identify Tomcat Path

## Note Using Function Which Will Never Be Called


## Tomcat_Path Means The Path Tomcat Has Been Installed
Tomcat_Path=/tmp/testshell/tomcat8/
echo "The Tomcat Path Is : $Tomcat_Path"

## Test Tomcat_Path/webapps/examples  Tomcat_Path/webapps/manager  Tomcat_Path/webapps/host-manager Are Available
if [ -d $Tomcat_Path/webapps/examples ];then
	echo "$Tomcat_Path/webapps/examples Is Available"
        mv $Tomcat_Path/webapps/examples $Tomcat_Path/webapps/temp
	echo "examples has been moved to temp"
else
	echo "$Tomcat_Path/webapps/examples Cannot Be Found"
fi

if [ -d $Tomcat_Path/webapps/manager ];then
	echo "$Tomcat_Path/webapps/manager Is Available"
	mv $Tomcat_Path/webapps/manager $Tomcat_Path/webapps/temp
	echo "manager has been moved to temp"
else
	echo "$Tomcat_Path/webapps/manager Cannot Be Found"
fi

if [ -d $Tomcat_Path/webapps/host-manager ];then
	echo "$Tomcat_Path/webapps/host-manager Is Available"
	mv $Tomcat_Path/webapps/host-manager $Tomcat_Path/webapps/temp
	chmod -R 000 $Tomcat_Path/webapps/temp
	echo "host-manager has been moved to temp"
else
	echo "$Tomcat_Path/webapps/host-manager Cannot Be Found"
fi

## Disable Auto Listing

Listings_String="<param-name>listings</param-name>"
False_String="<param-value>false</param-value>"
True_String="<param-value>true</param-value>"

	## 取web.xml中listings所在配置语句的下一句，即listings的值（<param-value>xxx</param-value>）

List_Auto=`cat $Tomcat_Path/conf/web.xml | grep -A 1 "<param-name>listings" |tail -1| awk '{print $1}'`

if [ $List_Auto = $False_String ];then
	echo "Auto Listing Is Disable, Safe"
	##sed -i -e '/listings/{n;s/<param-value>false/<param-value>true/}' $Tomcat_Path/conf/web.xml

	##cat /tmp/testshell/web1.xml | grep -A 1 "<param-name>listings</param-name>" | tail -1 | awk '{print $1}'

elif [ $List_Auto = $True_String ];then
	echo "Auto Listing Is Enable, Need To Be Disabled"
	sed -i -e '/listings/{n;s/<param-value>true/<param-value>false/}' $Tomcat_Path/conf/web.xml
	cat $Tomcat_Path/conf/web.xml | grep -A 1 "<param-name>listings</param-name>" | tail -1 | awk '{print $1}'
fi

## Change The Password For Shutdown In Port 8005

Shut_Down=`cat $Tomcat_Path/conf/server.xml | grep  "SHUTDOWN" | awk '{print $0}'`
Shut_Origin="<Server port=\"8005\" shutdown=\"SHUTDOWN\">"
##if [ $Shut_Down = $Shut_Origin ];then
	echo "$Shut_Down"
	echo "The Password For Shutdown Needs To Be Changed"
	sed -i 's/SHUTDOWN/YouCannotShutMeDown/' $Tomcat_Path/conf/server.xml 
	Shut_DownEdited=`cat $Tomcat_Path/conf/server.xml | grep  "shutdown=" | awk '{print $0}'`
##else
	echo "The Password For Shutdown Has Been Changed Already"
	echo "$Shut_DownEdited"
##fi

## Disable WAR Auto Deploy

Auto_Deploy=`cat $Tomcat_Path/conf/server.xml | grep  "autoDeploy" | awk '{print $2}'`
Deploy_True="autoDeploy=\"true\">"
Deploy_False="autoDeploy=\"false\">"
if [ $Auto_Deploy = $Deploy_True ];then
	echo "$Auto_Deploy"
	echo "Auto Deploy For WARs Needs To Be Disabled"
	sed -i 's/autoDeploy="true"/autoDeploy="false"/' $Tomcat_Path/conf/server.xml 
	cat $Tomcat_Path/conf/server.xml | grep  "autoDeploy" | awk '{print $2}'
elif [ $Auto_Deploy = $Deploy_False ];then
	echo "Auto Deploy For WARs Has Been Disabled"
	echo "$Auto_Deploy" 
fi

## Change The Startup & 404 Error Information

if [ -e $Tomcat_Path/lib/catalina.jar ];then
	cd $Tomcat_Path/lib/
	if [ -e $Tomcat_Path/lib/org ];then
		if [ -e $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties ];then
			echo "The Current Config Is :"
			cat $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
			echo "Need To Be Hidden"
 			sed -i 's/server.info=.*/server.info=YouKnowMe/' $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties
			cat $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
		else
			echo "The Config File ServerInfo.properties Cannot Be Found"
		fi
	else
		jar xf $Tomcat_Path/lib/catalina.jar
		if [ -e $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties ];then
			echo "The Current Config Is :"
			cat $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
			echo "Need To Be Hidden"
 			sed -i 's/server.info=.*/server.info=YouKnowMe/' $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties
			cat $Tomcat_Path/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
		else
			echo "The Config File ServerInfo.properties Cannot Be Found"
		fi
	fi
elif [ -e $Tomcat_Path/server/lib/catalina.jar ];then
	cd $Tomcat_Path/server/lib/
	if [ -e $Tomcat_Path/server/lib/org ];then
		if [ -e $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties ];then
			echo "The Current Config Is :"
			cat $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
			echo "Need To Be Hidden"
 			sed -i 's/server.info=.*/server.info=YouKnowMe/' $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties
			cat $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
		else
			echo "The Config File ServerInfo.properties Cannot Be Found"
		fi
	else
		jar xf $Tomcat_Path/server/lib/catalina.jar
		if [ -e $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties ];then
			echo "The Current Config Is :"
			cat $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
			echo "Need To Be Hidden"
 			sed -i 's/server.info=.*/server.info=YouKnowMe/' $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties
			cat $Tomcat_Path/server/lib/org/apache/catalina/util/ServerInfo.properties | grep  "server.info" | awk '{print $0}'
		else
			echo "The Config File ServerInfo.properties Cannot Be Found"
		fi
	fi
else
	echo "The Config File catalina.jar Cannot Be Found"
fi

## Change The Information When Telnet 8080

sed -e 's/port=\"8080\"/port=\"8080\" server=\"IIS\"/' $Tomcat_Path/conf/server.xml
cat $Tomcat_Path/conf/server.xml | grep -A 4 "port=\"8080\""|  awk '{print $0}'


	