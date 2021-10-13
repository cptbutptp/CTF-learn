<?php

/**
 * Facebook AWD.
 *
 * This file is part of the facebook AWD package
 */
namespace FacebookAWD\Model;

use PopCode\Framework\Model\Model;
use PopCode\Framework\Form\FormType;

/**
 * This is the model of a facebook Application.
 *
 * This file is used to represent a facebook application.
 * (Will be removed before 2.0)
 *
 * @category     Extension
 *
 * @author       Alexandre Hermann <hermann.alexandre@pop-code.fr>
 */
class Application extends Model
{
    /**
     * The id of the application.
     *
     * @var int
     * @FormType(
     *          required=true,
     *          type="text",
     *          help="This is the ID of your facebook application. You can find it or create an application <a href='https://developers.facebook.com'>here</a>",
     *          )
     */
    protected $id;

    /**
     * The secret key of the application.
     *
     * @var string
     * @FormType(
     *             required=true,
     *             type="text",
     *             help="This is the secret key of your facebook application. You can find it or create an application <a href='https://developers.facebook.com/'>here</a>",
     *             )
     */
    protected $secretKey;

    /**
     * the name of the application.
     *
     * @var string
     */
    protected $name;

    /**
     * the public link of the application.
     *
     * @var string
     */
    protected $link;

    /**
     * The namespace of the application.
     *
     * @var string
     */
    protected $namespace;

    /**
     * the iconUrl of the application.
     *
     * @var string
     */
    protected $iconUrl;

    /**
     * The logo Url of the application.
     *
     * @var string
     */
    protected $logoUrl;

    /**
     * the nb of montly active users.
     *
     * @var int
     */
    protected $monthlyActiveUsers;

    /**
     * the rank of montly active users.
     *
     * @var int
     */
    protected $monthlyActiveUsersRank;

    /**
     * the nb of daily active users.
     *
     * @var int
     */
    protected $dailyActiveUsers;

    /**
     * the rank of daily active users.
     *
     * @var int
     */
    protected $dailyActiveUsersRank;

    /**
     * the nb of weekly active users.
     *
     * @var int
     */
    protected $weeklyActiveUsers;

    /**
     * Get the id.
     *
     * @return int
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set the id.
     *
     * @param int $id
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setId($id)
    {
        $this->id = $id;

        return $this;
    }

    /**
     * Get the secret key.
     *
     * @return string
     */
    public function getSecretKey()
    {
        return $this->secretKey;
    }

    /**
     * Set the secret key.
     *
     * @param string $secretKey
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setSecretKey($secretKey)
    {
        $this->secretKey = $secretKey;

        return $this;
    }

    /**
     * Get the name.
     *
     * @return string
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * Set the name.
     *
     * @param string $name
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setName($name)
    {
        $this->name = $name;

        return $this;
    }

    /**
     * Get the link.
     *
     * @return string
     */
    public function getLink()
    {
        return $this->link;
    }

    /**
     * Set the link.
     *
     * @param string $link
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setLink($link)
    {
        $this->link = $link;

        return $this;
    }

    /**
     * Get the namespace.
     *
     * @return string
     */
    public function getNamespace()
    {
        return $this->namespace;
    }

    /**
     * Set the namespace.
     *
     * @param string $namespace
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setNamespace($namespace)
    {
        $this->namespace = $namespace;

        return $this;
    }

    /**
     * Get the icon url.
     *
     * @return string
     */
    public function getIconUrl()
    {
        return $this->iconUrl;
    }

    /**
     * Set the icon url.
     *
     * @param string $iconUrl
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setIconUrl($iconUrl)
    {
        $this->iconUrl = $iconUrl;

        return $this;
    }

    /**
     * Get the logo url.
     *
     * @return string
     */
    public function getLogoUrl()
    {
        return $this->logoUrl;
    }

    /**
     * Set the icon url.
     *
     * @param string $logoUrl
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setLogoUrl($logoUrl)
    {
        $this->logoUrl = $logoUrl;

        return $this;
    }

    /**
     * Get the nb of monthly active users.
     *
     * @return int
     */
    public function getMonthlyActiveUsers()
    {
        return $this->monthlyActiveUsers;
    }

    /**
     * Set the nb of monthly active users.
     *
     * @param int $monthlyActiveUsers
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setMonthlyActiveUsers($monthlyActiveUsers)
    {
        $this->monthlyActiveUsers = $monthlyActiveUsers;

        return $this;
    }

    /**
     * Get the nb of dayly active users.
     *
     * @return int
     */
    public function getDailyActiveUsers()
    {
        return $this->dailyActiveUsers;
    }

    /**
     * Set the nb of dayly active users.
     *
     * @param int $dailyActiveUsers
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setDailyActiveUsers($dailyActiveUsers)
    {
        $this->dailyActiveUsers = $dailyActiveUsers;

        return $this;
    }

    /**
     * Get the rank of monthly active users.
     *
     * @return int
     */
    public function getMonthlyActiveUsersRank()
    {
        return $this->monthlyActiveUsersRank;
    }

    /**
     * Get the rank of daily active users.
     *
     * @return int
     */
    public function getDailyActiveUsersRank()
    {
        return $this->dailyActiveUsersRank;
    }

    /**
     * Get the nb of Weekly active users.
     *
     * @return int
     */
    public function getWeeklyActiveUsers()
    {
        return $this->weeklyActiveUsers;
    }

    /**
     * Set the rank of monthly active users.
     *
     * @param int $monthlyActiveUsersRank
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setMonthlyActiveUsersRank($monthlyActiveUsersRank)
    {
        $this->monthlyActiveUsersRank = $monthlyActiveUsersRank;

        return $this;
    }

    /**
     * Set the rank of daily active users.
     *
     * @param int $dailyActiveUsersRank
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setDailyActiveUsersRank($dailyActiveUsersRank)
    {
        $this->dailyActiveUsersRank = $dailyActiveUsersRank;

        return $this;
    }

    /**
     * Set the nb of weekly active users.
     *
     * @param int $weeklyActiveUsers
     *
     * @return \FacebookAWD\Model\Application
     */
    public function setWeeklyActiveUsers($weeklyActiveUsers)
    {
        $this->weeklyActiveUsers = $weeklyActiveUsers;

        return $this;
    }
}
