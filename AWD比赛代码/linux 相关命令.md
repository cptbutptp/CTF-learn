限制用户进程数量，防止 fork 炸弹
ubuntu - nproc 20

挂 waf 的 php 语句

    include_once('waf.php');
    require_once('waf.php');

按终端号踢出
$pkill -kill -t pts/4

禁止 ping
#echo 1 >/proc/sys/net/ipv4/icmp_echo_ignore_all

允许 ping
#echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_all
