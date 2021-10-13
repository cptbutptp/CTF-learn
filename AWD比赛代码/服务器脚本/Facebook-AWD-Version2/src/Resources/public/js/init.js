//check if the fb-root node is exisiting
if (!jQuery('#fb-root').length) {
    jQuery('body').append('<div id="fb-root" />');
}

//init the facebook sdk
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/" + facebookawdData.locale + "/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

//init the facebook awd js object
var facebookAWD = new FacebookAWD();

//trigger the init when all ready
jQuery(document).ready(function ($) {
    facebookAWD.bindEvents();
});
