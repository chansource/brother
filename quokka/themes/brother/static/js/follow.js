$(document).ready(function(){
    var shareLink = location.href;
    var shareTitle = document.title;
    // var img_src='http://www.hdwallpapers.in/walls/cute_dog_boo-wide.jpg';
    $(".social-share-weibo").click(function () {
        window.open(
            "http://v.t.sina.com.cn/share/share.php?title=" + encodeURIComponent(shareTitle) + "&url=" + encodeURIComponent(shareLink)
        );
    });
    $(".social-share-tweibo").click(function () {
        window.open(
            "http://share.v.t.qq.com/index.php?c=share&a=index&url=" + encodeURIComponent(shareLink)+"&title=" +encodeURIComponent(shareTitle)
        );
    });
    $('.social-share-wechat').hover(
            function(){
            $('#wechat-help').css("display","block");
        },     
        function(){
            $('#wechat-help').css("display","none");
        }
    );
});