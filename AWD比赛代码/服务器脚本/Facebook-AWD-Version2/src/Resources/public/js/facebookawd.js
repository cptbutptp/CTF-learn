var FacebookAWD = function (options) {
    var me = this;
    var $ = jQuery;
    this.bindEvents = function () {
        window.fbAsyncInit = function () {
            var defaults = {
                appId: facebookawdData.appId,
                xfbml: true,
                status: true,
                version: 'v2.0',
                cookie: true
            };
            var options = $.extend(defaults, options);
            FB.init(options);
            $(window).trigger('FacebookAWD_ready', me);
        };
    };
};
