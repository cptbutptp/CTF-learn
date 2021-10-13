<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<div class="facebookAWD">
    <br />
    <ul class="list-group">
        <li class="lists-group-item ">
            <a href="?page=<?php echo $this->container->getSlug(); ?>&master_settings=1" class="btn btn-warning pull-right">
                <span class="glyphicon glyphicon-cog"></span> <?php echo $this->_('Setup'); ?>
            </a>
            <h4 class="list-group-item-heading"><?php echo $this->container->getTitle(); ?></h4>
            <p class="list-group-item-text">Base <?php echo $this->container->getTitle(); ?></p>
            <hr />
        </li>

        <?php
        foreach ($plugins as $plugin) {
            ?>
            <li class="lists-group-item">
                <a href="?page=<?php echo $plugin->getSlug();
            ?>" class="btn btn-default pull-right animated fadeInLeft">
                    <span class="glyphicon glyphicon-cog"></span> <?php echo $this->_('Settings');
            ?>
                </a>
                <h5 class="list-group-item-heading">
                    <?php echo $this->_($plugin->getTitle());
            ?>
                    <span class="label label-info label-sm"><?php echo $plugin->getVersion();
            ?></span>
                </h5>
                <p class="list-group-item-text"><?php echo $this->_($plugin->getDescription());
            ?></p>
                <p class="list-group-item-text">
                    <small><em><?php echo $this->_('Author:');
            ?> <?php echo $plugin->getAuthor();
            ?></em></small>
                </p>
                <hr />
            </li>
        <?php 
        }
        ?>
    </ul>
    <a href="#">
        <span class="glyphicon glyphicon-shopping-cart"></span>
        <?php echo $this->_('Find more Facebook AWD plugins'); ?>
    </a>
</div>
