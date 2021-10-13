<?php

require_once dirname(dirname(__DIR__)) . '/vendor/autoload.php';

use FacebookAWD\Model\Application;
use PopCode\Wordpress\OptionManager\OptionManager;

$testdir = getenv('WP_TESTS');
require_once $testdir . '/tmp/wordpress-tests-lib/includes/functions.php';

function _manually_load_plugin()
{
    /* $om = new OptionManager('facebookawd');
      $application = new Application();
      $application->setId('723161874437388');
      $application->setSecretKey('50807f581495a0b6ae3acf8cdfe8f2c7');
      $om->set('options.application', $application); */

    require dirname(__FILE__) . '/../../boot.php';
}

tests_add_filter('muplugins_loaded', '_manually_load_plugin');
require $testdir . '/tmp/wordpress-tests-lib/includes/bootstrap.php';
