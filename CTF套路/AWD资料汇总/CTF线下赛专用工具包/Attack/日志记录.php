<?php
date_default_timezone_set('Asia/Shanghai');
$ip        = $_SERVER["REMOTE_ADDR"];   //访问IP
$filename  = $_SERVER['PHP_SELF'];  //访问的文件
$parameter = $_SERVER["QUERY_STRING"];  //查询的字符串
$method    = $_SERVER['REQUEST_METHOD']; //请求方法
...
$time      =  date('Y-m-d H:i:s',time()); //请求时间
$post      = file_get_contents("php://input",'r'); //接收POST数据
$others    = '**********************************************************************';
$logadd    = '访问时间：'.$time.'访问IP:'.$ip.'请求方法：'.$method.' '.'访问链接：'.$filename.'?'.$parameter."\r\n";...
//记录写入
$fh = fopen("log.txt", "a");
fwrite($fh, $logadd);
fwrite($fh,print_r($_COOKIE, true)."\r\n");
fwrite($fh,$others."\r\n");
fclose($fh);
?>