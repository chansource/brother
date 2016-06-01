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
var pages=1;
var baseUrl="/brotherinfo?";
$("#more-btn").click(function (){
    var offset=perCount*pages;
    var url=baseUrl+'offset='+offset+'&'+'count='+perCount;
    $.getJSON(url.replace(),function  (data) {
        if(data['data'].length!==0){
            data['data'].forEach(function(item) {
                $(".contents").append(template(item));
            });
            pages=pages+1;
        }
    });
});
