<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
include dirname(__DIR__).'/header.html.php';
?>
<div class="facebookAWD">
    <div class="panel panel-default">
        <div class="panel-body">
            <?php
            $submit = '
                <div class="submit" style="text-align:center;">
                    <input type="submit" name="install" id="installawd" class="btn btn-primary" value="'.__('Install', $this->container->getPtd()).'" />
                    '.($isReady ? '
                        <a class="btn btn-default" href="?page=<?php echo $this->container->getRoot()->getSlug(); ?>">
                            '.__('Cancel', $this->container->getPtd()).'
                        </a>' : '').
                    '</div>';
            echo $this->render($this->container->getRoot()->getRootPath().'/Resources/views/admin/settingsForm.html.php', array(
                'form' => $form,
                'afterForm' => $submit,
            ));
            ?>
            </form>
        </div>
    </div>
</div>
<?php
include dirname(__DIR__).'/footer.html.php';
