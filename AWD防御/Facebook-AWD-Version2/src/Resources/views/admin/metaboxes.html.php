<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
?>
<?php
$screen = get_current_screen();
include dirname(__FILE__).'/header.html.php';
?>

<div id="poststuff">
    <div id="post-body" class="metabox-holder columns-2">
        <div id="post-body-content">

            <?php
            if (isset($action)) {
                do_action($action);
            }
            ?>

            <?php
            if (isset($blockContent)) {
                echo $blockContent;
            }
            ?>

            <div id="postbox-container-2" class="postbox-container">
                <?php
                if (isset($boxes)) {
                    foreach ($boxes as $action) {
                        call_user_func_array($action['type'], array($screen->id, $action['context'], $args));
                    }
                }
                ?>
            </div>
            <div id="postbox-container-1" class="postbox-container">
                <?php
                if (isset($boxesSide)) {
                    foreach ($boxesSide as $action) {
                        call_user_func_array($action['type'], array($screen->id, $action['context'], $args));
                    }
                }
                ?>
            </div>
        </div>
    </div>
</div>
<?php wp_nonce_field('closedpostboxes', 'closedpostboxesnonce', false); ?>
<?php wp_nonce_field('meta-box-order', 'meta-box-order-nonce', false); ?>
<script type="text/javascript">
    jQuery(document).ready(function ($) {
        postboxes.add_postbox_toggles("<?php echo $screen->id; ?>");

        //fix the support of select2 in postbox when the post box is hidden of toogled
        $(this).on("postbox-toggled", function (e, postbox) {
            var $postbox = $(postbox);
            if (!$postbox.hasClass('closed')) {
                $postbox.find('select').select2();
            }
        });
    });
</script>

<?php
include dirname(__FILE__).'/footer.html.php';
