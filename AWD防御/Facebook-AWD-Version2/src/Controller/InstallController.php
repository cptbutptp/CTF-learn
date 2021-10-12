<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 */

namespace FacebookAWD\Controller;

use PopCode\Framework\Form\Form;
use PopCode\Framework\Form\FormFactory;
use PopCode\Framework\Form\FormType;
use PopCode\Wordpress\Controller\AdminMenuController;
use Exception;
use Facebook\Facebook;

/**
 * This is the install controller.
 *
 * This file will add some install step at first install of the plugin.
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
class InstallController extends AdminMenuController
{

    /**
     * @var Form
     */
    protected $installForm;

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
    public function getMenuTitle()
    {
        return $this->container->getTitle() . ' Setup';
    }

    /**
     * {@inheritdoc}
     */
    public function init()
    {
        parent::init();

        //hack to let the install works also on tab app canvas
        remove_action('login_init', 'send_frame_options_header');
        remove_action('admin_init', 'send_frame_options_header');

        //clone the default application to do not play with php reference
        $application = clone $this->om->get('options.application');

        $formType = new FormType();
        $formType->setEntity('FacebookAWD\\Model\\Application');
        $this->installForm = FormFactory::createForm('fawd', $formType, $application);

        $this->installForm->build();
        $this->setListenerResponse($this->handleInstall());
    }

    /**
     * The success install view.
     */
    public function installSuccess()
    {
        echo $this->render($this->container->getRoot()->getRootPath() . '/Resources/views/admin/install/install.html.php', array(
            'isReady' => $this->isReady(),
            'title' => __('Setup', $this->container->getPtd()),
            'form' => $this->installForm,
        ));
    }

    /**
     * Install layout.
     *
     * @return string
     */
    public function index()
    {
        //hanlde success
        if ($this->getListenerResponse()) {
            echo $this->render($this->container->getRoot()->getRootPath() . '/Resources/views/admin/install/install-success.html.php', array(
                'application' => $this->om->get('options.application'),
                'title' => __('Success !', $this->container->getPtd()),
            ));

            return;
        }

        echo $this->render($this->container->getRoot()->getRootPath() . '/Resources/views/admin/install/install.html.php', array(
            'isReady' => $this->om->get('ready'),
            'title' => __('Setup', $this->container->getPtd()),
            'form' => $this->installForm,
        ));
    }

    /**
     * Handle the install.
     *
     * @return bool
     */
    public function handleInstall()
    {
        if ($this->isMethod('POST') && $this->installForm->hasRequest()) {
            $this->installForm->bind(filter_input_array(INPUT_POST));
            if ($this->installForm->isValid()) {
                $application = $this->installForm->getData();
                try {
                    $facebookApi = new Facebook([
                        'app_id' => $application->getId(),
                        'app_secret' => $application->getSecretKey(),
                        'default_graph_version' => 'v2.2',
                    ]);
                    $response = $facebookApi->get('/' . $application->getId(), $facebookApi->getApp()->getAccessToken());
                    $applicationData = $response->getGraphObject('\Facebook\GraphNodes\GraphApplication')->asArray();
                    $this->installForm->getPropertyAccessor()->hydrateObject($application, $applicationData);
                    $this->om->set('ready', true, false);
                    $this->om->set('options.application', $application);

                    return true;
                } catch (Exception $e) {
                    $this->installForm->addError($e);
                    $this->om->set('ready', false);
                }
            }
        }

        return false;
    }

}
