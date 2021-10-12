<?php

/**
 * Facebook AWD config.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
$configs = array(
    '__' => array(
        'src' => '/js/init.js',
        'deps' => array('jquery', '__lib'),
        'footer' => true,
    ),
    '__lib' => array(
        'src' => '/js/facebookawd.js',
    ),
    '__prettify' => array(
        'src' => '/google-code-prettify/prettify.js',
    ),
    '__bootstrap' => array(
        'src' => '/js/bootstrap/bootstrap.min.js',
    ),
    '__select2' => array(
        'src' => '/js/select2/select2.full.min.js',
    ),
    '__admin' => array(
        'src' => '/js/admin/admin.js',
        'deps' => array('__prettify'),
    ),
    '__admin-init' => array(
        'src' => '/js/admin/init.js',
        'deps' => array('__admin'),
        'footer' => true,
    ),
);

$path = plugins_url('/public', __DIR__);

return $this->applyPrefixPath($configs, $path);
