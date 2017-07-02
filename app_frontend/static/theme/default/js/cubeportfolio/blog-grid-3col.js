(function($, window, document, undefined) {
    'use strict';
        
    // init cubeportfolio
    $('#js-grid-blog-posts').cubeportfolio({
        filters: '#js-filters-blog-posts',
        search: '#js-search-blog-posts',
        defaultFilter: '*',
        animationType: '3dflip',
        gapHorizontal: 30,
        gapVertical: 30,
        gridAdjustment: 'responsive',
        mediaQueries: [{
            width: 1500,
            cols: 3
        }, {
            width: 1100,
            cols: 3
        }, {
            width: 800,
            cols: 3
        }, {
            width: 480,
            cols: 1,
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
        caption: 'revealBottom',
        displayType: 'fadeIn',
        displayTypeSpeed: 400,
    });
})(jQuery, window, document);
