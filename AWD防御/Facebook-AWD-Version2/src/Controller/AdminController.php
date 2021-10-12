<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 */

namespace FacebookAWD\Controller;

use PopCode\Wordpress\Controller\AdminMenuController as BaseController;
use PopCode\Wordpress\Admin\MetaboxInterface;

/**
 * This is the admin controller.
 *
 * This file add required hooks in wordpress admin using
 * controllers and models
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
class AdminController extends BaseController implements MetaboxInterface
{

    /**
     * {@inheritdoc}
     */
    public function getMenuType()
    {
        return self::TYPE_MENU;
    }

    /**
     * {@inheritdoc}
     */
    public function getIconUrl()
    {
        return plugins_url('/Resources/public/img/logo_icon.png', __DIR__);
    }

    /**
     * get the templates.
     */
    public function getTemplates()
    {
        return array(
            'index' => $this->container->getRoot()->getRootPath() . '/Resources/views/admin/metaboxes.html.php',
            'welcome' => $this->container->getRoot()->getRootPath() . '/Resources/views/admin/home/welcome.html.php',
            'plugins' => $this->container->getRoot()->getRootPath() . '/Resources/views/admin/home/plugins.html.php',
            'donate' => $this->container->getRoot()->getRootPath() . '/Resources/views/admin/home/donate.html.php',
            'documentation' => $this->container->getRoot()->getRootPath() . '/Resources/views/admin/home/documentation.html.php',
        );
    }

    public function addDefaultMetaboxes($pageHook)
    {
        $title = '<span class="facebookAWD"><span class="glyphicon glyphicon-info-sign"></span></span> ' . __('Documentation', $this->container->getPtd());
        add_meta_box($pageHook . '_documentation', $title, array($this, 'documentationSection'), $pageHook, 'side', 'default');

        $title = '<span class="facebookAWD"><span class="glyphicon glyphicon-thumbs-up"></span></span> ' . __('Be cool...', $this->container->getPtd());
        add_meta_box($pageHook . '_donate', $title, array($this, 'donateSection'), $pageHook, 'side', 'default');
    }

    /**
     * {@inheritdoc}
     */
    public function addMetaboxes($pageHook)
    {
        $this->addDefaultMetaboxes($pageHook);

        $title = '<span class="facebookAWD"><span class="glyphicon glyphicon-th-list"></span></span> ' . __('Plugins', $this->container->getPtd());
        add_meta_box($pageHook . '_plugins', $title, array($this, 'pluginsSection'), $pageHook, 'normal', 'default');
    }

    /**
     * Welcome section.
     */
    public function welcomeSection()
    {
        $application = $this->container->getRoot()->get('services.option_manager')->get('options.application');
        echo $this->render($this->getTemplates()['welcome'], array('application' => $application));
    }

    /**
     * Plugins Section.
     */
    public function pluginsSection()
    {
        echo $this->render($this->getTemplates()['plugins'], array(
            'plugins' => $this->container->getRoot()->getPlugins(),
        ));
    }

    /**
     * Donate section.
     */
    public function donateSection()
    {
        echo $this->render($this->getTemplates()['donate']);
    }

    /**
     * Documentation Section.
     */
    public function documentationSection()
    {
        echo $this->render($this->getTemplates()['documentation']);
    }

}
