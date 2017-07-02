(function ($, window, document, undefined) {
    'use strict';


    /***************** Header Search ******************/
    $('.search').click(function(e) {
        var searchbtn = $('.search-btn');
        var searchopen = $('.search-open');
        if (searchbtn.hasClass('fa-search')) {
            searchopen.fadeIn(500);
            searchbtn.removeClass('fa-search').addClass('fa-times');
        } else {
            searchopen.fadeOut(500);
            searchbtn.removeClass('fa-times').addClass('fa-search');
        }
    });

    /*
     /*
     * Custom Data Fixed
     */
    $('.beactive').addClass('active');
    $('.beactive').removeClass('beactive');


    /*============================================
     Tooltip
     ==============================================*/
    $('[data-toggle="tooltip"]').tooltip();

    /*============================================
     Progress Bar
     ==============================================*/
    var progress = $('.progress-bars');
    if (progress.length) {
        $(window).bind('scroll', function (e) {
            var hT = progress.offset().top,
                    hH = progress.outerHeight(),
                    wH = $(window).height(),
                    wS = $(this).scrollTop();
            if (wS > (hT + hH - wH)) {
                $(function () {

                    $('.progress-bars > .progress > .progress-bar').each(function () {
                        var width = $(this).attr('aria-valuenow');
                        $(this).css('width', width + '%');
                    });

                });
            }
        });
    }

    /*============================================
     Brand
     ==============================================*/
    $('#owl-clients').owlCarousel({
        items: 4,
        itemsDesktop: [1199, 4],
        itemsDesktopSmall: [979, 4],
        itemsTablet: [768, 3],
        pagination: true,
        autoPlay: true
    });


    /*============================================
     Counter
     ==============================================*/
    var count = $('.count');
    if (count.length)
    {
        count.counterUp({
            delay: 10,
            time: 1000
        });
    }

})(jQuery, window, document);

