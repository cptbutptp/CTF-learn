<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 */
namespace FacebookAWD\Controller;

use PopCode\Wordpress\Controller\Controller;

/**
 * FacebookAWD FrontController.
 *
 * This file is the front controller
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
class FrontController extends Controller
{
    /**
     * {@inheritdoc}
     */
    public function init()
    {
        //add scripts
        add_action('wp_enqueue_scripts', array($this, 'enqueueScripts'));
        add_action('wp_enqueue_scripts', array($this, 'enqueueStyles'));

        //add cripts to admin also
        add_action('admin_print_scripts', array($this, 'enqueueScripts'));
        add_action('admin_print_scripts', array($this, 'enqueueStyles'));
    }

    /**
     * Enqueue scripts.
     */
    public function enqueueScripts()
    {
        wp_localize_script($this->container->getSlug(), $this->container->getSlug().'Data', $this->getPublicJSData());
        wp_enqueue_script($this->container->getSlug());
    }

    /**
     * Enqueue styles.
     */
    public function enqueueStyles()
    {
        wp_enqueue_style($this->container->getSlug().'bootstrap');
    }

    /**
     * Expose public js variales in the plugin object Data.
     *
     * @return array
     */
    public function getPublicJSData()
    {
        $application = $this->om->get('options.application');
        $data = array(
            'appId' => $application->getId(),
            'locale' => get_locale(),
        );

        return $data;
    }
}
