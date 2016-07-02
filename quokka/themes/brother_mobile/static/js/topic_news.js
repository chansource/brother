// banner初始化
var banner = new Swiper ('.banner', {
    direction: 'horizontal',
    loop: true,
});
// 初始化模板
var source ='<a href="{{link}}">\
                <div class="item">\
                    <div class="item-cover">\
                        <img src="{{cover_img}}" alt="">\
                    </div>\
                    <div class="item-text">\
                        <h1>{{title}}</h1>\
                        <p>{{summary}}</p>\
                    </div>\
                </div>\
            </a>';
var template = Handlebars.compile(source);

var perCount = 5,
    pages = 0,
    offset = perCount * pages;

var url = baseUrl + '?offset=' + offset + '&count=' + perCount;

// TODO: 声明理解运行的函数
function getData (url) {
    $.getJSON(url, function(data) {
        if(data['data'].length !== 0){
            data['data'].forEach(function(item) {
                $(".contents").append(template(item));
            });
            pages += 1;
        }
        if(data['data'].length < perCount){
            $("#more-btn").attr("disabled","disabled");
            $("#more-btn").text("无更多内容");
        }
    });
}
getData(url);

$("#more-btn").on("tap", function (){
    console.debug("pages:" + pages);
    console.debug("perCount:" + perCount);
    if($(this).attr("disabled") != "disabled"){
        var offset = perCount * pages;
        console.debug("offset:" + offset);
        var url = baseUrl + '?offset=' + offset + '&count=' + perCount;
        getData(url);
    }
});