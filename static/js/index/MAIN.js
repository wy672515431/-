/*
js
主页面
BY王勇
* */
//1.pre_load
    function pre_Load() {
        $("#load").fadeOut();
        $("#pre_load").delay(0).fadeOut("slow");
    }
    pre_Load();
//2.language
    function language_dropdown() {
        $(".language_default").on("click", function() {
            $("#language").slideToggle();
        });
        $("#language li").on("click", function() {
            $(this).parent().slideUp();
        });
    }
    language_dropdown();
 //2. slide_show
function home_slider(){
    $('.home-slideshow').slick({
        dots: false,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        fade: true,
        arrows: true,
        autoplay: true,
        autoplaySpeed: 4000,
        lazyLoad: 'ondemand'
    });
}
home_slider();
$(window).resize(function() {
    var bodyheight = $(this).height() - 20;
    $(".sliderFull .bg-size").height(bodyheight);
}).resize();
//productslider
function house_slider(){
    $('.productSlider').slick({
        dots: false,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]

    });
}
house_slider();
$(".tab_content").hide();
$(".tab_content:first").show();
$("ul.tabs li").on('click', function () {
    $(".tab_content").hide();
    var activeTab = $(this).attr("rel");
    $("#"+activeTab).fadeIn();

    $("ul.tabs li").removeClass("active");
    $(this).addClass("active");

    $(".tab_drawer_heading").removeClass("d_active");
    $(".tab_drawer_heading[rel^='"+activeTab+"']").addClass("d_active");

    $('.productSlider').slick('refresh');

});
$('ul.tabs li').last().addClass("tab_last");

$(".bg-top" ).parent().addClass('b-top');
$(".bg-bottom" ).parent().addClass('b-bottom');
$(".bg-center" ).parent().addClass('b-center');
$(".bg-left" ).parent().addClass('b-left');
$(".bg-right" ).parent().addClass('b-right');
$(".bg_size_content").parent().addClass('b_size_content');
$(".bg-img").parent().addClass('bg-size');
$(".bg-img.blur-up" ).parent().addClass('');
jQuery('.bg-img').each(function() {

    var el = $(this),
        src = el.attr('src'),
        parent = el.parent();

    parent.css({
        'background-image': 'url(' + src + ')',
        'background-size': 'cover',
        'background-position': 'center',
        'background-repeat': 'no-repeat'
    });

    el.hide();
});