<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 *
 * @author Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
namespace FacebookAWD\Admin;

use PopCode\Framework\ContainerInterface;
use PopCode\Wordpress\Admin\Admin as BaseAdmin;

/**
 * This is the base admin class.
 *
 * This file add required hooks in wordpress admin using controllers and models
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
class Admin extends BaseAdmin
{
    /**
     * {@inheritdoc}
     */
    public function __construct(ContainerInterface $container)
    {
        parent::__construct($container);
        add_action('admin_init', array($this, 'adminInit'));
    }

    /**
     * init the admin screen layout.
     */
    public function initScreen()
    {
        add_screen_option('layout_columns', array('max' => 2, 'default' => 1));
    }

    /**
     * Init the admin.
     */
    public function adminInit()
    {
        $pageHook = $this->getAdminMenuHook($this->container->getSlug());

        $this->enqueueAssetsHook($pageHook);

        foreach ($this->getAdminMenuHooks() as $hook) {
            add_action('load-'.$hook, array($this, 'initScreen'));
            $this->enqueueAssetsHook($hook);
        }
    }

    /**
     * Register hook to print assets.
     *
     * @param string $pageHook
     */
    public function enqueueAssetsHook($pageHook)
    {
        add_action('admin_print_styles', array($this, 'enqueueGlobalStyles'));
        add_action('admin_print_scripts', array($this, 'enqueueGlobalScripts'));

        add_action('admin_print_styles-'.$pageHook, array($this, 'enqueueStyles'));
        add_action('admin_print_scripts-'.$pageHook, array($this, 'enqueueScripts'));
        add_action('admin_print_styles-widgets.php', array($this, 'enqueueScripts'));
        add_action('admin_print_styles-widgets.php', array($this, 'enqueueStyles'));
    }

    /**
     * Enqueue the globals css styles.
     */
    public function enqueueGlobalStyles()
    {
        wp_enqueue_style($this->container->getSlug());
    }

    /**
     * Enqueue the globals javascripts scripts.
     */
    public function enqueueGlobalScripts()
    {
        wp_enqueue_script($this->container->getSlug().'_admin');
        wp_enqueue_script($this->container->getSlug().'_admin-init');
    }

    /**
     * Enqueue the css styles.
     */
    public function enqueueStyles()
    {
        $sg = $this->container->getSlug();
        $required = array(
            'thickbox',
            $sg.'_prettify',
        );
        array_walk($required, function ($style) {
            wp_enqueue_style($style);
        });
    }

    /**
     * Enqueue the javascripts scripts.
     */
    public function enqueueScripts()
    {
        //add local scripts
        $sg = $this->container->getSlug();
        $required = array(
            'media-upload',
            'thickbox',
            'common',
            'postbox',
            'wp-list',
            'jquery',
            $sg.'_prettify',
            $sg.'_select2',
            $sg.'_bootstrap',
            $sg.'_jquery-validate',
        );
        array_walk($required, function ($script) {
            wp_enqueue_script($script);
        });
    }
}
