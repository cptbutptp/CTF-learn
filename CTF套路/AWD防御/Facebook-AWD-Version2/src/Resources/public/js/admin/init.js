/*
 * Facebook AWD Admin helpers
 * 
 * Init
 */
var facebookAWDAdmin = new FacebookAWDAdmin();

/**
 * Init
 */
jQuery(document).ready(function ($) {
    facebookAWDAdmin.bindEvents();
    $(window).trigger('FacebookAWDAdmin_ready', facebookAWDAdmin);
});