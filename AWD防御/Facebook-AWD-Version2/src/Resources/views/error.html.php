<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<div id="facebookAWD" class="wrap container">
    <div class="panel panel-danger">
        <div class="panel-heading">
            <h2>ERROR <?php echo $error->getCode(); ?></h2>
        </div>
        <div class="panel-body">
            <p><?php echo $error->getMessage(); ?></p>
        </div>
    </div>
</div>
