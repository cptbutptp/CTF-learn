/*
 * Facebook AWD Admin helpers
 */
var FacebookAWDAdmin = function () {
    var $ = jQuery;
    var admin = this;
    /**
     * Bind the events
     * @returns {void}
     */
    this.bindEvents = function () {

        /**
         * Prettyprint
         */
        prettyPrint();

        /**
         * Hide event on change value.
         * true = show
         * false = hidden
         */
        $(document).on('change', '.hideIfOn', function (e, data) {
            var $elem = $(e.currentTarget);
            if ($elem.prop('checked')) {
                var sectionsHideOn = $elem.data('hideOn');
                var $section = $elem.parents('form').find(sectionsHideOn);
                var shouldHide = $elem.val() === '1' ? false : true;
                data = data || {};
                if (!shouldHide) {
                    !data.direct ? $section.slideDown() : $section.show();
                    $section.find('select').select2();
                } else {
                    !data.direct ? $section.slideUp() : $section.hide();
                }
            }

        });
        $('.hideIfOn').trigger('change', {direct: 1});

        /**
         * Select2
         */
        var $selects = $('.facebookAWD select');
        if ($selects.length) {
            $selects.select2({'width': '100%'});
        }
        //reload the widget when the are updated/added
        $(document).on('widget-updated, widget-added', function (e, $widget) {
            //if ('widget-added' === e.type) {
                $widget.find('.select2').remove();
                $widget.find('select').select2({'width': '100%'});
            //}
            /*if ("facebookawd".indexOf($widget.get(0).id)) {
             $widget.find('select').select2({'width': '100%'});
             }*/
        });

    };

    /**
     * Submit settings form
     * @param {Object} $form
     * @returns {void}
     */
    this.submitSettingsForm = function ($form, action, callback) {
        var data = $form.serialize() + '&action=' + action;
        $.post(ajaxurl, data, function (data) {
            if (callback) {
                callback(data);
                return;
            }
            admin.insertSection(data);
        }, 'json');
    };

    /**
     * Insert a section in admin
     * @param {Object} data
     * @returns {void}
     */
    this.insertSection = function (data) {
        var $newHtml = $(data.view);
        var id = $newHtml.attr('id');

        $('#' + id).replaceWith($newHtml);

        var $newSection = $('#' + id);
        $('.hideIfOn').trigger('change', {direct: 1});

        //re parse xfbml if needed
        FB.XFBML.parse($newSection.get(0));

        //parse code block if needed
        prettyPrint();

        //select2
        $('#' + id).find('select').select2();

        //scroll to the top of the section
        var top = typeof $newSection.offset() !== 'undefined' ? $newSection.offset().top : 0;
        $('html, body').animate({
            scrollTop: top - 40
        });

        //hide alert after 5 secondes
        var $alert = $newSection.find('.alert-success');
        $alert.addClass('animated fadeInDown');
        clearTimeout(t1);
        var t1 = setTimeout(function () {
            $alert.removeClass('fadeInDown').addClass('fadeOutUp');
            clearTimeout(t2);
            var t2 = setTimeout(function () {
                $alert.slideUp();
            }, 500);
        }, 5000);
    };
};
