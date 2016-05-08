$(document).ready(function(){
    var shareLink = location.href;
    var shareTitle = document.title;
    $(".social-share-weibo").click(function () {
        window.open(
            "http://weibo.com/u/5872263244"
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