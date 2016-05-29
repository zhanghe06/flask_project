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
$(function () {
    // 滚动页面侧边悬浮动态导航宽度控制
    $(window).resize(function () {
        $('#affix_nav_ul').width($('#affix_nav_ul').parent().width());
        //console.log($('.container').width());
        // 如果屏幕宽度小于940px 隐藏侧边导航
        if ($('.container').width() <= 940) {
            $('#affix_nav_ul').hide();
        } else {
            $('#affix_nav_ul').show();
        }
    });
    $(window).resize();
});


/* 按钮加载状态 */
// html button 标签其中 autocomplete="off" 属性是针对FF浏览器在页面加载之后，禁用状态不会自动解除用的。
$(function () {
    $(".btn-load").click(function () {
        $(this).button('loading').delay(1000).queue(function () {
            //$(this).button('reset');
        });
    });
});


/* 返回顶部 */
$('#top-link').click(function () {
    $('html,body').animate({scrollTop: 0}, 'slow');
    return false;
});
if (($(window).height() + 100) < $(document).height()) {
    $('#top-link-block').removeClass('hidden').affix({
        // how far to scroll down before link "slides" into view
        offset: {top: 100}
    });
}