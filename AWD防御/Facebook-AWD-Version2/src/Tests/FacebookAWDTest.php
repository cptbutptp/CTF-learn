<?php

namespace FacebookAWD\Tests;

use FacebookAWD\FacebookAWD;

class FacebookAWDTest extends \WP_UnitTestCase
{

    /**
     * @var FacebookAWD
     */
    protected $object;

    public function setUp()
    {
        parent::setUp();

        $this->object = getFacebookAWD();
    }

}
