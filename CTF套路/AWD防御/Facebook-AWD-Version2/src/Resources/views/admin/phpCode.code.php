<?php
/**
 * Facebook AWD Template.
 *
 * @author PopCode (Alexandre Hermann) [hermann.alexandre@ahwebev.fr]
 */
$code = htmlentities('<?php') . "\n";
if ($shortcode) {
    $code .= '/***********************************' . "\n";
    $code .= ' * ' . $this->_('Using the shortcode with php') . " *\n";
    $code .= ' ***********************************/' . "\n";
    $code .= 'echo do_shortcode(\'' . $shortcode . '\')' . "\n\n";
}
if ($phpCode) {
    $code .= '/***********************************' . "\n";
    $code .= ' * ' . $this->_('Using the php object') . " *\n";
    $code .= ' ***********************************/' . "\n";
    $code .= $phpCode;
    $code .= "\n" . htmlentities('?>');
}
?>
<pre class="prettyprint lang-php"><?php echo $code; ?></pre>
