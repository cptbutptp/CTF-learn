<?php

/**
  Plugin Name: Facebook AWD
  Plugin URI: http://www.facebook-awd.com
  Description: Facebook AWD adds required facebook's extensions on your site.
  Version: 2.0
  Author: Alexandre Hermann (PopCode) <hermann.alexandre@pop-code.fr>
  Author URI: http://www.pop-code.com
  License: Copywrite PopCode
  Text Domain: facebookawd
  DomainPath: /src/Resources/translations
  Last modification: 22/05/2014
 */
require_once __DIR__ . '/vendor/autoload.php';

use FacebookAWD\FacebookAWD;

/**
 * Helpers to getFacebookAWD
 * 
 * @global FacebookAWD $facebookAWD
 * @return FacebookAWD
 */
if (!function_exists('getFacebookAWD')) {

    function getFacebookAWD()
    {
        global $facebookAWD;
        if (empty($facebookAWD)) {
            $facebookAWD = new FacebookAWD();
        }
        return $facebookAWD;
    }

}


$facebookAWD = getFacebookAWD();


