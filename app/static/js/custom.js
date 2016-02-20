/**
 * Created by zhanghe on 16-1-31.
 */

/* 轮播大图延时加载 */
function lazyContainer(searchNode) {
    $(searchNode).find('.active').find('img.lazy').each(function () {
        var imgSrc = $(this).attr('data-src');
        if (imgSrc) {
            $(this).attr('src', imgSrc);
            $(this).attr('data-src', '');
        }
    });
}

$('#myCarousel').bind('slid.bs.carousel', function () {
    lazyContainer(this);
});

lazyContainer('#myCarousel');


/* 生成工具提示 */
$('[rel="tooltip"]').tooltip();


/* 附加导航 */
$(function(){
    // 滚动页面侧边悬浮动态导航宽度控制
    $(window).resize(function(){
        $('#affix_nav_ul').width($('#affix_nav_ul').parent().width());
        //console.log($('.container').width());
        // 如果屏幕宽度小于940px 隐藏侧边导航
        if ($('.container').width() <= 940){
            $('#affix_nav_ul').hide();
        }else {
            $('#affix_nav_ul').show();
        }
    });
    $(window).resize();
});
