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
