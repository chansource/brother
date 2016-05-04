// $(document).ready(function(){
    var width=($("#sharing").width()-$("#shares").width())/2-2;
   $("#cut-line1").css("width",width);
   $("#cut-line2").css("width",width);

   $(window).resize(function(){
    width=($("#sharing").width()-$("#shares").width())/2-2;
   $("#cut-line1").css("width",width);
   $("#cut-line2").css("width",width);
   });
    var shareLink = location.href;
    var shareTitle = document.title;
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
    $('#wechat-qrcode').qrcode({
        render: "canvas",
        width: 200,
        height: 200,
        text    : shareLink
    });
    $('.social-share-wechat').hover(
            function(){
            $('#wechat-help').css("display","block");
        },    
        function(){
            $('#wechat-help').css("display","none");
        }
    );
// });