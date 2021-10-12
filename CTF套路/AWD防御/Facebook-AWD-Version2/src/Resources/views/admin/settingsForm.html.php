<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<div class="facebookAWD<?php echo isset($classes) ? ' ' . $classes : null; ?>" id="<?php echo $form->getId(); ?>">
    <?php if (!empty($success)) {
        ?>
        <div class="alert alert-xs alert-success">
            <a class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only"><?php _e('Close', $this->container->getPtd());
        ?></span></a>
            <?php echo $success;
            ?>
        </div>
    <?php }
    ?>
    <form role="form" method="post" action="#<?php echo $form->getId(); ?>">
        <?php if (count($form->getErrors())) {
            ?>
            <div class="alert alert-danger">
                <?php
                foreach ($form->getErrors() as $error) {
                    echo $error->getMessage() . '<br>';
                }
                ?>
            </div>
        <?php }
        ?>

        <?php
        if (isset($beforeForm)) {
            echo $beforeForm;
        }

        echo $form->createView();

        if (isset($afterForm)) {
            echo $afterForm;
        }
        ?>

        <?php if (!empty($withSubmit)) {
            ?>
            <input type="submit" name="submit" id="submit_settings" class="btn btn-xs btn-primary btn-mini" value="<?php echo is_string($withSubmit) ? $this->_($withSubmit) : $this->_('Save');
            ?>" />
               <?php }
               ?>
    </form>
</div>
