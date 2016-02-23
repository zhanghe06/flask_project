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


/* 按钮加载状态 */
$(function() {
    $(".btn").click(function(){
        $(this).button('loading').delay(1000).queue(function() {
            //$(this).button('reset');
        });
    });
});


/* 创建图表，实例化一个Chart对象 */

var lineChartData = {
	labels : ["January","February","March","April","May","June","July"],
	datasets : [
		{
			fillColor : "rgba(220,220,220,0.5)",
			strokeColor : "rgba(220,220,220,1)",
			pointColor : "rgba(220,220,220,1)",
			pointStrokeColor : "#fff",
			data : [65,59,90,81,56,55,40]
		},
		{
			fillColor : "rgba(151,187,205,0.5)",
			strokeColor : "rgba(151,187,205,1)",
			pointColor : "rgba(151,187,205,1)",
			pointStrokeColor : "#fff",
			data : [28,48,40,19,96,27,100]
		}
	]
};

$(function() {
    var ctx = $("#chart_line_canvas").get(0).getContext("2d");
    new Chart(ctx).Line(lineChartData, {responsive: true});
});
