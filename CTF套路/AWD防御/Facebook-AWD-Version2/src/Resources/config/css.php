<?php

/**
 * Facebook AWD config.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
$configs = array(
    '__' => array(
        'src' => '/css/styles.css',
    ),
    '__prettify' => array(
        'src' => '/google-code-prettify/tomorrow-night-blue.css',
        //'src' => '/google-code-prettify/prettify.css',
        //'src' => '/google-code-prettify/vibrant-ink.css',
        'deps' => array('__'),
    ),
);

$path = plugins_url('/public', __DIR__);

return $this->applyPrefixPath($configs, $path);
