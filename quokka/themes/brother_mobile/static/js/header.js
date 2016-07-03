"use strict";
var navStatus=true;
var shareStatus=true;

$("#nav-btn").on('tap',function (){
    $("#share-btn img").toggle();
    $(".page-nav").toggle();
    $("#nav-btn img").toggle();
    $(".help-btn").toggle();
    $(".fix-btn").toggle();
    navStatus=!navStatus;
    shareStatus=!shareStatus;
});


var shareLink = location.href;
var shareTitle = document.title;
$(".share-btn").on("tap", function(event) {
    window.location.href = "http://v.t.sina.com.cn/share/share.php?title=" + encodeURIComponent(shareTitle) + "&url=" + encodeURIComponent(shareLink);
});
// $(".social-share-tweibo").click(function () {
//     window.open(
//         "http://share.v.t.qq.com/index.php?c=share&a=index&url=" + encodeURIComponent(shareLink)+"&title=" +encodeURIComponent(shareTitle)
//     );
// });
// $(".social-share-qzone").click(function () {
//     window.open('http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url='+ encodeURIComponent(shareLink)+ '&title='+encodeURIComponent(shareTitle)
//     );
// });