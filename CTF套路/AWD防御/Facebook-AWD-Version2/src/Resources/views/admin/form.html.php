<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<?php if (count($form->getErrors())) {
    ?>
    <div class="alert alert-danger">
        <?php
        foreach ($form->getErrors() as $error) {
            echo $error->getMessage().'<br>';
        }
    ?>
    </div>
<?php 
}
?>
<div class="form-content animated fadeInDown">
    <?php echo $form->createView(); ?>
</div>
