(function($, window, document, undefined) {
    'use strict';
    

    // init cubeportfolio
    $('#js-grid-masonry').cubeportfolio({
        filters: '#js-filters-masonry',
        layoutMode: 'grid',
        defaultFilter: '*',
        animationType: 'slideDelay',
        gapHorizontal: 30,
        gapVertical: 30,
        gridAdjustment: 'responsive',
        mediaQueries: [{
            width: 1500,
            cols: 4
        }, {
            width: 1100,
            cols: 4
        }, {
            width: 800,
            cols: 3
        }, {
            width: 480,
            cols: 2,
            options: {
                caption: ''
            }
        }, {
            width: 320,
            cols: 1,
            options: {
                caption: ''
            }
        }],
        caption: 'overlayBottomAlong',
        displayType: 'bottomToTop',
        displayTypeSpeed: 100,

        // lightbox
        lightboxDelegate: '.cbp-lightbox',
        lightboxGallery: true,
        lightboxTitleSrc: 'data-title',
        lightboxCounter: '<div class="cbp-popup-lightbox-counter">{{current}} of {{total}}</div>',
    });
})(jQuery, window, document);

