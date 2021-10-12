<div class="modal fade" id="<?php echo $id; ?>" tabindex="-1" role="dialog">
    <div class="modal-dialog <?php echo $classes; ?>" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <a class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></a>
                <h4 class="modal-title"><?php echo $title; ?></h4>
            </div>
            <div class="modal-body">
                <?php echo $content; ?>
            </div>
            <div class="modal-footer">
                <?php echo $footer; ?>
                <!--<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>-->
            </div>
        </div>
    </div>
</div>
