<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 */

namespace FacebookAWD;

use FacebookAWD\Admin\Admin;
use FacebookAWD\Controller\AdminController;
use FacebookAWD\Controller\FrontController;
use FacebookAWD\Controller\InstallController;
use FacebookAWD\Listener\RequestListener;
use FacebookAWD\Model\Application;
use PopCode\Wordpress\Asset\AssetManager;
use PopCode\Wordpress\Cache\CacheDataHolder;
use PopCode\Wordpress\OptionManager\OptionManager;
use PopCode\Wordpress\Plugin;
use Facebook\Facebook;

/**
 * FacebookAWD.
 *
 * This file is the base container of the Facebook AWD extension
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
final class FacebookAWD extends Plugin
{

    /**
     * Constructor.
     */
    public function __construct()
    {
        $this->rootPath = __DIR__;
        parent::__construct();

        $this->createServices();
        $this->createListeners();
        $this->createControllers();
    }

    /**
     * Init the default services.
     */
    protected function createServices()
    {
        //Cache
        $cache = new CacheDataHolder();
        $this->set('services.cache_manager', $cache);
        $cache->setDebug(false);

        $om = new OptionManager($this->getSlug(), array('ready' => false));
        $om->load();
        $this->set('services.option_manager', $om);

        $jsm = new AssetManager($this->slug, $this->getRootPath('Resources', 'config', 'js.php'));
        $this->set('services.js_manager', $jsm);

        $cssm = new AssetManager($this->slug, $this->getRootPath('Resources', 'config', 'css.php'));
        $this->set('services.css_manager', $cssm);

        //load default models
        $application = $om->get('options.application');
        if (!$application instanceof Application) {
            $application = new Application();
        }
        $om->set('options.application', $application, false);

        //load api
        $om->set('ready', false, false);
        if ($application->getId() && $application->getSecretKey()) {
            $om->set('ready', true, false);
            $facebookApi = new Facebook(['app_id' => $application->getId(), 'app_secret' => $application->getSecretKey()]);
            $this->set('services.facebook', $facebookApi);
        }

        //flush the data
        $om->flush();

        return $this;
    }

    /**
     * Set the defaults listeners.
     */
    protected function createListeners()
    {
        $requestListener = new RequestListener($this);
        $this->set('listener.request_listener', $requestListener);

        return $this;
    }

    /**
     * Set the defaults controllers.
     */
    protected function createControllers()
    {
        $admin = new Admin($this);
        $this->set('admin', $admin);

        $adminController = new AdminController($this, $admin);
        $this->set('controller.backend', $adminController);

        $installController = new InstallController($this, $admin);
        $this->set('controller.install', $installController);

        $frontController = new FrontController($this);
        $this->set('controller.front', $frontController);

        return $this;
    }

    /**
     * {@inheritdoc}
     */
    public function boot()
    {
        parent::boot();

        $isReady = $this->get('services.option_manager')->get('ready');
        if (!$isReady || filter_input(INPUT_GET, 'master_settings')) {
            $this->get('controller.install')->init();
        } else {
            $this->get('listener.request_listener')->init();
            $this->get('controller.backend')->init();
            $this->get('controller.front')->init();
            \do_action($this->getSlug() . '_register_plugins', $this);
        }

        return $this;
    }

}
