"use strict";
var navStatus=true;
var shareStatus=true;

$("#nav-btn").click(function (){
    $("#share-btn img").toggle();
    $("nav").toggle();
    $("#nav-btn img").toggle();
    $(".help-btn").toggle();
    navStatus=!navStatus;
    shareStatus=!shareStatus;
});
