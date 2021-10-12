<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
include dirname(__DIR__).'/header.html.php';
?>

<div class="facebookAWD">
    <div class="panel panel-success animated fadeInDown">
        <div class="panel-heading">
            <?php _e('Facebook AWD is ready.', $ptd); ?> <img src="<?php echo $application->getIconUrl(); ?>" alt="...">
        </div>
        <table class="table table-hover table-bordered">
            <tr>
                <th colspan="2"><?php _e('App Name', $ptd); ?></th>
                <td colspan="2"><?php echo $application->getName(); ?></td>
            </tr>
            <tr>
                <th colspan="2"><?php _e('Namespace', $ptd); ?></th>
                <td colspan="2"><?php echo $application->getNamespace(); ?></td>
            </tr>
            <tr>
                <th colspan="2"><?php _e('Monthly Active Users', $ptd); ?></th>
                <td><?php echo $application->getMonthlyActiveUsers(); ?></td>
                <td><?php _e('Rank', $ptd); ?>: <?php echo $application->getMonthlyActiveUsersRank(); ?></td>
            </tr>
            <tr>
                <th colspan="2"><?php _e('Daily Active Users', $ptd); ?></th>
                <td><?php echo $application->getDailyActiveUsers(); ?></td>
                <td><?php _e('Rank', $ptd); ?>: <?php echo $application->getDailyActiveUsersRank(); ?></td>
            </tr>
            <tr>
                <th colspan="2"><?php _e('Weekly Active Users', $ptd); ?></th>
                <td colspan="2"><?php echo $application->getWeeklyActiveUsers(); ?></td>
            </tr>
        </table>
    </div>
    <div style="text-align:center;">
        <a class="btn btn-success btn-lg animated bounceIn" role="button" href="?page=<?php echo $this->container->getSlug(); ?>"><?php _e('Start now !', $ptd); ?></a>
    </div>
</div>

<?php
include dirname(__DIR__).'/footer.html.php';
