//自定义表单开始
$(document).ready(function() {
    //预览
    var chss = 0;
    $('.btn-yulan').click(function() {
        if (chss == 0) {
            $("#colzuo").attr("class", "col-sm-12");
            $("#colyou").hide();
            $(".tools").hide();
            chss++;
        } else {
            $("#colzuo").attr("class", "col-sm-9");
            $("#colyou").show();
            $(".tools").show();
            chss = 0;
        }
    });
    setup_draggable();
    $("#copy-to-clipboard").on("click", function() {
            var $copy = $(".form-body").clone().appendTo(document.body);

            $copy.find(".tools, :hidden").remove();

            $.each(["draggable", "droppable", "sortable", "dropped", "ui-sortable", "ui-draggable", "ui-droppable", "form-body"], function(i, c) {
                $copy.find("." + c).removeClass(c).removeAttr("style")
            });

            var html = html_beautify($copy.html());
            $copy.remove();

            $modal = get_modal(html, 'cont').modal("show");
            $modal.find(".btn").remove();
            $modal.find(".modal-title").html("复制HTML代码");
            $modal.find(":input:first").select().focus();

            return false
        })
        //点击添加表单
    $(".btntext,.btntexts").click(function() {
        $(tableList($(this).attr("id"))).appendTo($(".ui-sortable"));
        $(".labcheck input").unbind('click');
        $(".labcheck input").click(function() {
            if ($(this).is(":checked")) {
                alert("选中");
            } else {
                alert("未选中");
            }
        });
        //时间初始化
                $(".form_datetime").datetimepicker({
                    language: 'en-US', //日期
                    format: "yyyy/mm/dd hh:ii",
                    initialDate: new Date(), //初始化当前日期
                    autoclose: true, //选中自动关闭
                    todayBtn: true //显示今日按钮
                });
                //upload初始化
                $('.uploadfile').fileinput({
                    language: 'zh'
                });
                //省市区初始化
                $('.distpicker').distpicker({
                    province: 'State',
                    city: 'City',
                    district: 'County',
                    autoSelect: true,
                    placeholder: false
                });
    });
});

var setup_draggable = function() {
    $(".draggable").draggable({
        appendTo: "body",
        helper: "clone"
    });
    $(".droppable").droppable({
        accept: ".draggable",
        helper: "clone",
        hoverClass: "droppable-active",
        drop: function(event, ui) {
            $(".empty-form").remove();
            var $orig = $(ui.draggable);
            if (!$(ui.draggable).hasClass("dropped")) {
                $(tableList($orig.attr("id"))).appendTo(this);
                //时间初始化
                $(".form_datetime").datetimepicker({
                    language: 'zh-CN', //日期
                    format: "yyyy/mm/dd hh:ii",
                    initialDate: new Date(), //初始化当前日期
                    autoclose: true, //选中自动关闭
                    todayBtn: true //显示今日按钮
                });
                //upload初始化
                $('.uploadfile').fileinput({
                    language: 'zh'
                });
                //省市区初始化
                $('.distpicker').distpicker({
                    province: '省份名',
                    city: '城市名',
                    district: '区名',
                    autoSelect: true,
                    placeholder: false
                });
            } else {
                if ($(this)[0] != $orig.parent()[0]) {
                    var $el = $orig.clone().appendTo(this);
                    $orig.remove()
                }
            }
        }
    }).sortable()

};
//表单自定义
function tableList(id) {
    var content = "";
    switch (id) {
        case "text":
            // Text
            var text = '<input type="text" class="form-control" placeholder="Please enter the Text">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label"> Text：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "select":
            // drop-down box
            var select = '<select class="form-control"><option>Please select</option><option>default</option></select>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label"> drop-down box：</label><div class="col-sm-7">' + select + '</div><p class="tools col-sm-3"><a class="edit-link" name="select" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "textarea":
            //Multiple lines Text
            var textarea = '<textarea class="form-control" placeholder="Please enter the Text"></textarea>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">Multiple lines Text：</label><div class="col-sm-7">' + textarea + '</div><p class="tools col-sm-3"><a class="edit-link" name="textarea" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "radio":
            //radio
            var radom = Math.ceil(Math.random() * 100000);
            var radio = '<label class="radio-inline"><input type="radio" value="default1" name="rad' + radom + '" checked> default1</label><label class="radio-inline"><input type="radio" name="rad' + radom + '" value="default2"> default2</label>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">Single-select：</label><div class="col-sm-7">' + radio + '</div><p class="tools col-sm-3"><a class="edit-link" name="radio" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "checkbox":
            //multi-select
            var checkbox = '<label class="radio-inline" style="padding-left:0px;"><input type="checkbox" name="default1"> default1</label><label class="radio-inline" style="padding-left:0px;"><input type="checkbox" name="default2"> default2</label>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">multi-select：</label><div class="col-sm-7">' + checkbox + '</div><p class="tools col-sm-3"><a class="edit-link" name="checkbox" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "datetime":
            //time
            var datetime = '<input readonly="" class="form-control form_datetime" type="text" style="border: 1px solid #e5e6e7;">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label"> Time：</label><div class="col-sm-7">' + datetime + '</div><p class="tools col-sm-3"><a class="edit-link" name="datetime" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "file":
            //upload
            var file = '<input class="file uploadfile" type="file" multiple data-min-file-count="1">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">upload：</label><div class="col-sm-7">' + file + '</div><p class="tools col-sm-3"><a class="edit-link" name="file" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "name":
            //name
            var text = '<input type="text" class="form-control" placeholder="Please enter your name">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">name：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "phone":
            //phone
            var text = '<input type="text" class="form-control" placeholder="Please enter your phone number">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">phone：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "email":
            //email
            var text = '<input type="text" class="form-control" placeholder="Please enter your email address">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">email：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "www":
            //name
            var text = '<input type="text" class="form-control" placeholder="Please enter the你的个人网站地址">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">个人网站：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "logo":
            //name
            var file = '<input class="file uploadfile" type="file" multiple data-min-file-count="1">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">uploadLogo：</label><div class="col-sm-7">' + file + '</div><p class="tools col-sm-3"><a class="edit-link" name="file" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "sex":
            //sex
            var radom = Math.ceil(Math.random() * 100000);
            var radio = '<label class="radio-inline"><input type="radio" value="Male" name="Male' + radom + '" checked> Male</label><label class="radio-inline"><input type="radio" name="rad' + radom + '" value="Female"> Female</label>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">sex：</label><div class="col-sm-7">' + radio + '</div><p class="tools col-sm-3"><a class="edit-link" name="radio" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a></p></div>';
            break;
        case "occupation":
            //position
            var text = '<input type="text" class="form-control" placeholder="Please enter the your position">';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">position：</label><div class="col-sm-7">' + text + '</div><p class="tools col-sm-3"><a class="edit-link" name="text" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
        case "profile":
            //Personal profile
            var textarea = '<textarea class="form-control" placeholder="Please enter the your personal profile"></textarea>';
            content = '<div class="form-group draggable ui-draggable dropped"><label class="col-sm-2 control-label">Personal profile：</label><div class="col-sm-7">' + textarea + '</div><p class="tools col-sm-3"><a class="edit-link" name="textarea" title="设置"><i class="fa fa-cog fa-fw"></i></a><a class="remove-link"><i class="fa fa-trash-o"></i></a><label class="labcheck"><input type="checkbox"> mandatory</label></p></div>';
            break;
    }
    return content;
}
//表单自定义设置
function tabUp(tabL, $el) {
    var content = "";
    switch (tabL) {
        case "text":
            // Text
            content = '<div class="row tabup"><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">Tips：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("input:eq(0)").attr("placeholder") + '" placeholder="Please enter theTips"></div></div></div>';
            break;
        case "select":
            // drop-down box
            content += '<div class="row tabup">';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children1：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("select").find("option:eq(0)").html() + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-plus-square select-add" title="添加" style="font-size:18px; cursor:pointer;"></i></label></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children2：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("select").find("option:eq(1)").html() + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"></label></div>';
            $el.find("select").find("option").each(function(index) {
                if (index > 1) {
                    content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children' + (index + 1) + '：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $(this).html() + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-trash-o select-del" title="删除" style="font-size:18px; cursor:pointer;"></i></label></div>';
                }
            });
            content += '</div>';
            break;
        case "textarea":
            //Multiple lines Text
            content = '<div class="row tabup"><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">Tips：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("textarea").attr("placeholder") + '" placeholder="Please enter theTips"></div></div></div>';
            break;
        case "radio":
            //radio
            content += '<div class="row tabup">';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children1：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("input[type='radio']:eq(0)").attr("value") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-plus-square select-add" title="添加" style="font-size:18px; cursor:pointer;"></i></label></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children2：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("input[type='radio']:eq(1)").attr("value") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"></label></div>';
            $el.find("input[type='radio']").each(function(index) {
                if (index > 1) {
                    content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children' + (index + 1) + '：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $(this).attr("value") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-trash-o select-del" title="删除" style="font-size:18px; cursor:pointer;"></i></label></div>';
                }
            });
            content += '</div>';
            break;
        case "checkbox":
            //multi-select
            content += '<div class="row tabup">';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children1：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("input[type='checkbox']:eq(0)").attr("name") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-plus-square select-add" title="添加" style="font-size:18px; cursor:pointer;"></i></label></div>';
            content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children2：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $el.find("input[type='checkbox']:eq(1)").attr("name") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"></label></div>';
            $el.find("input[type='checkbox']").each(function(index) {
                if (index > 1) {
                    content += '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children' + (index + 1) + '：</label><div class="col-sm-8"><input type="text" class="form-control" value="' + $(this).attr("name") + '" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-trash-o select-del" title="删除" style="font-size:18px; cursor:pointer;"></i></label></div>';
                }
            });
            content += '</div>';
            break;
        case "datetime":
            //time
            content = '<div class="row tabup"><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div></div>';
            break;
        case "file":
            //upload
            content = '<div class="row tabup"><div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">title：</label><div class="col-sm-9"><input type="text" class="form-control" value="' + $el.find("label:eq(0)").html().substring(0, $el.find("label:eq(0)").html().length - 1) + '" placeholder="Please enter thetitle"></div></div></div>';
            break;
    }
    return content;
}
var get_modal = function(content, tabL, $el) {
    var modal = "";
    if (tabL == "cont") {
        modal = $('<div class="modal" style="overflow: auto;" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><a type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</a><h4 class="modal-title">Form Information Setting</h4></div><div class="modal-body ui-front"><xmp class="form-control"  style="min-height: 200px; overflow-y: auto; margin-bottom: 10px;font-family: Monaco, Fixed">' + content + '</xmp><button class="btn btn-success">confirm</button></div></div></div></div>').appendTo(document.body);
    } else {
        modal = $('<div class="modal" style="overflow: auto;" tabindex="-1"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><a type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</a><h4 class="modal-title">Form Information Setting</h4></div><div class="modal-body ui-front">' + tabUp(tabL, $el) + '<xmp class="form-control"  style="min-height: 200px; display:none; overflow-y: auto; margin-bottom: 10px;font-family: Monaco, Fixed">' + content + '</xmp><button class="btn btn-success">confirm</button></div></div></div></div>').appendTo(document.body);
    }
    return modal;
};
$(document).on("click", ".edit-link", function(ev) {

    var tabname = $(this).attr('name');
    var $el = $(this).parent().parent();
    var $el_copy = $el.clone();
    var $edit_btn = $el_copy.find(".edit-link").parent().remove();
    var $modal = get_modal(html_beautify($el_copy.html()), tabname, $el).modal("show");

    $modal.find(".btn-success").click(function(ev2) {
            //表单自定义js
            switch (tabname) {
                case "text":
                    // Text
                    $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                    $el.find("input:eq(0)").attr("placeholder", $(this).parent().find("input:eq(1)").val());
                    $modal.modal("hide");
                    return false;
                    break;
                case "select":
                    // drop-down box
                    var option = "";
                    var panduan = 0;
                    $(this).parent().find("input").each(function(index, element) {
                        if (index == 0) {
                            $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                        } else {
                            if ($(this).val() == "") {
                                panduan = 1;
                                $(this).focus();
                                return false;
                            } else {
                                option += "<option>" + $(this).val() + "</option>";
                            }
                        }
                    });
                    if (panduan != 0) {
                        alert("Can't be blank");
                    } else {
                        $el.find("select").html(option);
                        $modal.modal("hide");
                    }
                    break;
                case "textarea":
                    //Multiple lines Text
                    $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                    $el.find("textarea").attr("placeholder", $(this).parent().find("input:eq(1)").val());
                    $modal.modal("hide");
                    return false;
                    break;
                case "datetime":
                    //time
                    $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                    $modal.modal("hide");
                    return false;
                    break;
                case "file":
                    //upload
                    $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                    $modal.modal("hide");
                    return false;
                    break;
                case "radio":
                    //radio
                    var option = "";
                    var panduan = 0;
                    var radom = Math.ceil(Math.random() * 100000);
                    $(this).parent().find("input").each(function(index, element) {
                        if (index == 0) {
                            $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                        } else if (index == 1) {
                            if ($(this).val() == "") {
                                panduan = 1;
                                $(this).focus();
                                return false;
                            } else {
                                option += '<label class="radio-inline"><input type="radio" name="rad' + radom + '" value="' + $(this).val() + '" checked=""> ' + $(this).val() + '</label>';
                            }
                        } else {
                            if ($(this).val() == "") {
                                panduan = 1;
                                $(this).focus();
                                return false;
                            } else {
                                option += '<label class="radio-inline"><input type="radio" name="rad' + radom + '" value="' + $(this).val() + '" > ' + $(this).val() + '</label>';
                            }
                        }
                    });
                    if (panduan != 0) {
                        alert("Can't be blank");
                    } else {
                        $el.find("div[class='col-sm-7']").html(option);
                        $modal.modal("hide");
                    }
                    return false;
                    break;
                case "checkbox":
                    //multi-select
                    var option = "";
                    var panduan = 0;
                    $(this).parent().find("input").each(function(index, element) {
                        if (index == 0) {
                            $el.find("label:eq(0)").html($(this).parent().find("input:eq(0)").val() + "：");
                        } else if (index == 1) {
                            if ($(this).val() == "") {
                                panduan = 1;
                                $(this).focus();
                                return false;
                            } else {
                                option += '<label class="radio-inline"><input type="checkbox" name="' + $(this).val() + '"> ' + $(this).val() + '</label>';
                            }
                        } else {
                            if ($(this).val() == "") {
                                panduan = 1;
                                $(this).focus();
                                return false;
                            } else {
                                option += '<label class="radio-inline"><input type="checkbox" name="' + $(this).val() + '" > ' + $(this).val() + '</label>';
                            }
                        }
                    });
                    if (panduan != 0) {
                        alert("Can't be blank");
                    } else {
                        $el.find("div[class='col-sm-7']").html(option);
                        $modal.modal("hide");
                    }
                    return false;
                    break;
            }

        })
        //select 增加和删除
    $modal.find(".select-add").click(function() {
        var str = '<div class="col-sm-12" style="margin-bottom:10px"><label class="col-sm-3 control-label">children1：</label><div class="col-sm-8"><input type="text" class="form-control" value="" placeholder="Please enter thechildren"></div><label class="col-sm-1 control-label"><i class="fa fa-trash-o select-del" title="删除" style="font-size:18px; cursor:pointer;"></i></label></div>';
        $(this).parent().parent().parent().parent().find("div[class='row tabup']").append(str);

        $(".select-del").unbind('click');

        $(".select-del").click(function() {
            var r = confirm("Whether to Delete？")
            if (r == true) {
                $(this).parent().parent().remove();
            }

        });
        $(this).parent().parent().parent().parent().find("label[class='col-sm-3 control-label']").each(function(index, element) {
            if (index > 1) {
                $(this).html("children" + index + "：");
            }
        });
    });
    $(".select-del").unbind('click');
    $modal.find(".select-del").click(function() {

        var r = confirm("Whether to Delete？")
        if (r == true) {
            $(this).parent().parent().remove();
        }
    });
    //select 增加和删除
});
$(document).on("click", ".remove-link", function(ev) {
    var r = confirm("Whether to Delete？")
    if (r == true) {
        $(this).parent().parent().remove();
    }

});
//自定义表单结束
