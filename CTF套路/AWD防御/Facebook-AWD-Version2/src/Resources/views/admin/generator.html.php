<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<?php if (!empty($shortcode)) { ?>
    <h4 class="text-primary"><?php echo $this->_('Using shortcode'); ?></h4>
    <pre class="prettyprint"><?php echo $shortcode; ?></pre>
<?php } ?>
<h4 class="text-primary"><?php echo $this->_('Using PHP'); ?></h4>
<?php include __DIR__ . DIRECTORY_SEPARATOR . 'phpCode.code.php'; ?>

<?php if (!empty($preview)) { ?>
    <h4 class="text-primary"><?php echo $this->_('Preview'); ?></h4>
    <div class="well well-xs"><?php echo $preview; ?></div>
<?php } ?>