<?php

/**
 *      [Discuz!] (C)2001-2099 Comsenz Inc.
 *      This is NOT a freeware, use is subject to license terms
 *
 *      $Id: install.php 31304 2012-08-09 06:31:09Z liudongdong $
 */

if(!defined('IN_DISCUZ')) {
	exit('Access Denied');
}

$connect = C::t('common_setting')->fetch('connect', true);

$sql = <<<EOF

CREATE TABLE IF NOT EXISTS pre_common_member_connect (
  `uid` mediumint(8) unsigned NOT NULL default '0',
  `conuin` char(40) NOT NULL default '',
  `conuinsecret` char(16) NOT NULL default '',
  `conopenid` char(32) NOT NULL default '',
  `conisfeed` tinyint(1) unsigned NOT NULL default '0',
  `conispublishfeed` tinyint(1) unsigned NOT NULL default '0',
  `conispublisht` tinyint(1) unsigned NOT NULL default '0',
  `conisregister` tinyint(1) unsigned NOT NULL default '0',
  `conisqzoneavatar` tinyint(1) unsigned NOT NULL default '0',
  `conisqqshow` tinyint(1) unsigned NOT NULL default '0',
  PRIMARY KEY  (`uid`),
  KEY `conuin` (`conuin`),
  KEY `conopenid` (`conopenid`)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_connect_feedlog (
  flid mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  tid mediumint(8) unsigned NOT NULL DEFAULT '0',
  uid mediumint(8) unsigned NOT NULL DEFAULT '0',
  publishtimes mediumint(8) unsigned NOT NULL DEFAULT '0',
  lastpublished int(10) unsigned NOT NULL DEFAULT '0',
  dateline int(10) unsigned NOT NULL DEFAULT '0',
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (flid),
  UNIQUE KEY tid (tid)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_connect_postfeedlog (
  flid mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  pid int(10) unsigned NOT NULL DEFAULT '0',
  uid mediumint(8) unsigned NOT NULL DEFAULT '0',
  publishtimes mediumint(8) unsigned NOT NULL DEFAULT '0',
  lastpublished int(10) unsigned NOT NULL DEFAULT '0',
  dateline int(10) unsigned NOT NULL DEFAULT '0',
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (flid),
  UNIQUE KEY pid (pid)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_connect_memberbindlog (
  mblid mediumint(8) unsigned NOT NULL AUTO_INCREMENT,
  uid mediumint(8) unsigned NOT NULL DEFAULT '0',
  uin char(40) NOT NULL,
  `type` tinyint(1) NOT NULL DEFAULT '0',
  dateline int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (mblid),
  KEY uid (uid),
  KEY uin (uin),
  KEY dateline (dateline)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_connect_tthreadlog (
  twid char(16) NOT NULL,
  tid mediumint(8) unsigned NOT NULL DEFAULT '0',
  conopenid char(32) NOT NULL,
  pagetime int(10) unsigned DEFAULT '0',
  lasttwid char(16) DEFAULT NULL,
  nexttime int(10) unsigned DEFAULT '0',
  updatetime int(10) unsigned DEFAULT '0',
  dateline int(10) unsigned DEFAULT '0',
  PRIMARY KEY (twid),
  KEY nexttime (tid,nexttime),
  KEY updatetime (tid,updatetime)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_common_uin_black (
  uin char(40) NOT NULL,
  uid mediumint(8) unsigned NOT NULL DEFAULT '0',
  dateline int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (uin),
  UNIQUE KEY uid (uid)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS pre_common_connect_guest (
  `conopenid` char(32) NOT NULL default '',
  `conuin` char(40) NOT NULL default '',
  `conuinsecret` char(16) NOT NULL default '',
  `conqqnick` char(100) NOT NULL default '',
  PRIMARY KEY (conopenid)
) TYPE=MyISAM;

CREATE TABLE IF NOT EXISTS `pre_connect_disktask` (
  `taskid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '??????ID',
  `aid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '??????ID',
  `uid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '??????ID',
  `openid` char(32) NOT NULL DEFAULT '' COMMENT 'openId',
  `filename` varchar(255) NOT NULL DEFAULT '' COMMENT '????????????',
  `verifycode` char(32) NOT NULL DEFAULT '' COMMENT '???????????????',
  `status` smallint(6) unsigned NOT NULL DEFAULT '0' COMMENT '????????????',
  `dateline` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '?????????????????????',
  `downloadtime` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '??????????????????',
  `extra` text COMMENT '????????????',
  PRIMARY KEY (`taskid`),
  KEY `openid` (`openid`),
  KEY `status` (`status`)
) TYPE=MyISAM COMMENT='?????????????????????';


REPLACE INTO pre_common_setting VALUES ('regconnect', '1');

EOF;

runquery($sql);

$needCreateGroup = true;
if ($connect['feed']) {
	$group = C::t('common_usergroup')->fetch($connect['guest_groupid']);
	if ($group) {
		$needCreateGroup = false;
	}
} else {
	$connect = array (
		'allow' => '1',
		'feed' =>
		array (
			'allow' => '1',
			'group' => '0',
		),
		't' =>
		array (
			'allow' => '1',
			'group' => '0',
			'reply' => 1,
			'reply_showauthor' => 1,
		),
		'like_allow' => '1',
		'like_qq' => '',
		'turl_allow' => '1',
		'turl_qq' => '',
		'like_url' => '',
		'register_birthday' => '0',
		'register_gender' => '0',
		'register_uinlimit' => '',
		'register_rewardcredit' => '1',
		'register_addcredit' => '',
		'register_groupid' => '0',
		'register_regverify' => '1',
		'register_invite' => '1',
		'newbiespan' => '',
		'turl_code' => '',
		'mblog_app_key' => 'abc',
	);
}

if ($needCreateGroup) {
	include DISCUZ_ROOT . 'source/language/lang_admincp_cloud.php';
	$name = $extend_lang['connect_guest_group_name'];
	$userGroupData = array(
		'type' => 'special',
		'grouptitle' => $name,
		'allowvisit' => 1,
		'color' => '',
		'stars' => '',
	);
	$newGroupId = C::t('common_usergroup')->insert($userGroupData, true);

	$dataField = array(
		'groupid' => $newGroupId,
		'allowsearch' => 2,
		'readaccess' => 1,
		'allowgetattach' => 1,
		'allowgetimage' => 1,
	);
	C::t('common_usergroup_field')->insert($dataField);

	$connect['guest_groupid'] = $newGroupId;
	updatecache('usergroups');
}

C::t('common_setting')->update('connect', serialize($connect));
updatecache('setting');
$finish = true;