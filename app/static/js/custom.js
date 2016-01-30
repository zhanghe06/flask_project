/**
 * Created by zhanghe on 16-1-31.
 */

/* 轮播大图延时加载 */
function lazyContainer(searchNode) {
   $(searchNode).find('.active').find('img.lazy').each(function() {
       var imgSrc = $(this).attr('data-src');
       if (imgSrc) {
           $(this).attr('src',imgSrc);
           $(this).attr('data-src','');
       }
   });
}

$('#myCarousel').bind('slid.bs.carousel', function() {
    lazyContainer(this);
});

lazyContainer('#myCarousel');
