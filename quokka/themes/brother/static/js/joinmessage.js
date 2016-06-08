if (!window.location.origin) {
  window.location.origin = window.location.protocol + "//" 
    + window.location.hostname 
    + (window.location.port ? ':' + window.location.port : '');
}
var file_id=null;
var sendStatus=false;
var uploader = WebUploader.create({
    headers: { "X-CSRFToken": $("meta[name=csrf_token]").attr("content")},
    auto:true,
    // swf文件路径
    swf: 'http://cdn.staticfile.org/webuploader/0.1.0/Uploader.swf',
    // 文件接收服务端。
    server: window.location["origin"]+'/media/uploadfile',
    // 选择文件的按钮。可选。
    // 内部根据当前运行是创建，可能是input元素，也可能是flash.
    pick: '#chooseBtn',
    // 不压缩image, 默认如果是jpeg，文件上传前会压缩一把再上传！
    resize: false
});
uploader.on('uploadSuccess', function( file,response ) {
    if(!response["rtn"]){
        file_id=response["data"]["file_id"];
    }
    else{
        alert(response["rtn"]+":附件上传失败!");
        delAttach(file.id);
    }
});

function delAttach (id) {
    file_id=null;
    $( '#'+id ).remove();
    uploader.removeFile(id);
}
//只允许上传一个附件
uploader.on( 'beforeFileQueued',function  () {
    if($(".item").length>0){
        alert("只能添加一个附件哦!");
        return false;
    }
});
//添加附加图标和文件名
uploader.on( 'fileQueued', function( file ) {
        $("#filelist").append( '<div id="' + file.id + '" class="item">' +
            '<a class="ico_att"></a>'+
            '<span class="filename">' + file.name + '</span>' +
        '</div>' );
       
    });
// 文件上传过程中创建进度条实时显示
uploader.on( 'uploadProgress', function( file, percentage ) {
    var $li = $( '#'+file.id );
    $percent = $li.find('.progress .progress-bar');

    // 避免重复创建
    if ( !$percent.length ) {
        $percent = $('<div class="progress">' +
          '<div class="progress-bar" style="width: 0%">' +
          '</div>' +
        '</div>').appendTo( $li ).find('.progress-bar');
    }
    $percent.css( 'width', percentage * 100 + '%' );
});
//上传完成之后，去掉进度条，增加删除按钮
uploader.on( 'uploadComplete', function( file ) {
    $( '#'+file.id ).find('.progress').hide();
    $( '#'+file.id ).append('<a onclick="delAttach('+"'"+file.id+"'"+')" class="att_del">删除</a>');
});
//上传完成之后，去掉进度条，增加删除按钮
uploader.on( 'uploadError', function( file,reason ) {
    alert(reason+" 上传文件出错");
    delAttach(file.id);
});
//增加csrf_token
$(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": $("meta[name=csrf_token]").attr("content")
        }
    });
});
function showMessage (message) {
    $("#confirm-message").text(message);
    $("body").css("overflow","hidden");
    $(".confirm-mask").toggle();
}
var validator = new FormValidator('messageForm', [{
    name: 'sender_email',
    display: '你的邮箱',
    rules: 'required|valid_email'
},{
    name: 'message',
    display: '消息内容',
    rules: 'required'
} ], function(errors) {
    if (errors.length > 0) {
        showMessage(errors[0].message);
    }
    else{
            event.preventDefault();
            var data={
                        "title":"我要加入",
                        "message":$("textarea[name='message']").val(),
                        "sender_email":$("input[name='sender_email']").val(),
                        "status":"未读",
                        "channel":$("input[name='channel']").val()
                    };
              if(file_id!==null){
                data['document']=file_id;
              }
            $.post(
                    '/joinmessages/sendmessage',
                    data,
                    function(data){
                        if(!data["rtn"]){
                            showMessage("提交成功!");
                            sendStatus=true;
                            $("#send-button").attr("disabled", "true");
                            $("#send-button").removeClass("valid-button").addClass("novalid-button");

                        }
                        else{
                            showMessage(data["rtn"]+":系统又捣乱出错了\n");
                        }
                    }
            );
    }
});
$("#confirm-btn").click(function  () {
    if(sendStatus){
        history.back();
    }
    else{
        $("body").css("overflow","auto");
        $(".confirm-mask").toggle();
    }
});
validator.setMessage('required', '填上%s，才能收到回答哦！');
validator.setMessage('valid_email', '要填上正确的邮箱地址，才能收到回答哦！');
function checkForm()  {
    if( validator.valid() ){
        $("#send-button").removeClass("novalid-button").addClass("valid-button");
    }
    else{
        $("#send-button").removeClass("valid-button").addClass("novalid-button");
    }
}