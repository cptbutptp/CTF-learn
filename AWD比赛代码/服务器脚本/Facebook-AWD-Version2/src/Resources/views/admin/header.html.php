<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>

<div class="wrap">
    <h2>
        <img src="<?php echo plugins_url('/public/img/logo_icon_fat.png', dirname(__DIR__)); ?>" style="float: left; width:29px; margin-right: 6px;"/>
        <?php echo $this->_($this->container->getTitle()); ?>
        <small><?php echo isset($title) ? str_replace($this->container->getTitle(), '', $title) : ''; ?></small>
    </h2>
    <div id="facebookAWD" class="container">
        <br />
