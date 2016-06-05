var source ='<a class="content-item" href="{{details_link}}">'+
                '<div class="item-cover"><img  src="{{photo}}"></div>'+
                '<div class="item-infos">'+
                    '<div class="server-tags">'+
                        '{{#if brother_is_ask }}'+
                        '<span class="ask-tag">答问</span>'+'{{/if}}'+'{{#if brother_is_share }}'+'<span class="share-tag">分享</span>'+'{{/if}}'+
                    '</div>'+
                    '<div class="basic-info">\n<p>{{name}}</p>\n<span class="other-info">{{brother_college_major}}</span>\n<span class="other-info">{{brother_college_name}}</span>\n</div>'+
                    '<div class="tags">'+
                        '{{#each brother_tags }}'+
                        '<span class="personal-tag">{{this}}\n</span>'+'{{/each}}'+
                    '</div>\n</div>\n</a>';
var template = Handlebars.compile(source);
var perCount=5;
var pages=0;
var offset=perCount*pages;
var order="time";
var baseUrl="/brotherinfo?";
var url=baseUrl+'offset='+offset+'&count='+perCount+"&order="+order;
getData ();
function getData () {
    $.getJSON(url.replace(),function  (data) {
            if(data['data'].length!==0){
                data['data'].forEach(function(item) {
                    $(".contents").append(template(item));
                });
                pages=pages+1;
            }
            if(data['data'].length<perCount){
                $("#more-btn").attr("disabled","disabled");
                $("#more-btn").text("无更多内容");
            }
        });
}
$("#more-btn").on("tap",function (){
    if($(this).attr("disabled")!="disabled"){
        offset=perCount*pages;
        url=baseUrl+'offset='+offset+'&count='+perCount+"&order="+order;
        getData ();
    }

});
function toggle_sort_btn () {
    $(".sort-wrap button").toggleClass("active-sort-btn");
    $(".sort-wrap button").toggleClass("deactive-sort-btn");
}
$(".sort-wrap button").eq(0).on("tap", function() {
    if($(this).hasClass("active-sort-btn")){
        pages=0;
        order="hot";
        offset=perCount*pages;
        toggle_sort_btn ();
        $(".contents").empty();
        url=baseUrl+'offset='+offset+'&count='+perCount+"&order="+order;
        getData ();
    }
});
$(".sort-wrap button").eq(1).on("tap", function() {
    if($(this).hasClass("active-sort-btn")){
        pages=0;
        order="time";
        offset=perCount*pages;
        url=baseUrl+'offset='+offset+'&count='+perCount+"&order="+order;
        toggle_sort_btn ();
        $(".contents").empty();
        getData ();
    }
});
$(".fix-btn img").eq(0).on("tap", function() {
    scroll(0,0);
});