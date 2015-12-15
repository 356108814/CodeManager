/**
 * 客户端统一异步请求
 * Created by shiyong on 2015-12-14.
 */

$(function($){

    $('.ajaxPost').click(function(){
		var target_form = $('#'+$(this).attr('target-form'));
        //验证通过，提交
        var validform = target_form.Validform();
        if(!validform.check()){
            return;
        }
        var url = target_form.attr('action');
        var jsonObject = target_form.serializeObject();
        $.ajax({
          type: 'POST',
          url: url,
          data: jsonObject,
          dataType: 'json',
          success: function(rdata){
              var time = 1500;
              //请求成功
              if (rdata.result == 'success') {
                //有跳转链接
                if (rdata.url) {
                    layer.msg(rdata.message + '，页面即将自动跳转~!',{icon:6, time:time});
                }else{
                    layer.msg(rdata.message,{icon:6, time:time});
                }
                setTimeout(function(){
                    if (rdata.url) {
                        location.href = rdata.url;
                    }else{
                        location.reload();
                    }
                },time);
            }else{
                layer.msg(rdata.message,{icon:5, time:time});
                setTimeout(function(){
                    if (rdata.url) {
                        location.href = rdata.url;
                    }
                },time);
            }
          }
        })
	})
})

/**
 * 异步更新
 * @param url
 * @param jsonObject
 * @param successCallBack 请求成功回调函数
 * @param isReload 请求成功是否需要重新加载
 */
function ajaxUpdate(url,jsonObject,successCallBack,isReload){
    $.ajax({
      type: 'POST',
      url: url,
      dataType: 'json',
      data: jsonObject,
      success: function(rdata){
          var time = 1500;
          //请求成功
          if (rdata.result == 'success') {
            //有跳转链接
            if (rdata.url) {
                layer.msg(rdata.message + '，页面即将自动跳转~!',{icon:6, time:time});
            }else{
                if (rdata.message) {
                    layer.msg(rdata.message,{icon:6, time:time});
                }
            }
            //有回调函数
            if (successCallBack) {
                successCallBack(rdata.data)
            }
            setTimeout(function(){
                if (rdata.url) {
                    location.href = rdata.url;
                }else{
                    //处理加载
                    if(isReload === undefined){
                        isReload = true;
                    }
                    if(isReload == true){
                        location.reload();
                    }
                }
            },time);
        }else{
            layer.msg(rdata.message,{icon:5, time:time});
            setTimeout(function(){
                if (rdata.url) {
                    location.href = rdata.url;
                }
            },time);
        }
      },
    });
}

/**
 * 异步查询
 * @param url
 * @param jsonObject
 * @param successCallBack 请求成功回调函数
 */
function ajaxQuery(url,jsonObject,successCallBack){
    $.ajax({
      type: 'POST',
      url: url,
      dataType: 'json',
      data: jsonObject,
      success: function(rdata){
          var time = 1500;
          //请求成功
          if (rdata.result == 'success') {
            if(rdata.message){
              layer.msg(rdata.message,{icon:6,time:time});
            }
            //有回调函数
            if (successCallBack) {
                successCallBack(rdata.data)
            }
        }else{
            layer.msg(rdata.message,{icon:1,time:time});
            setTimeout(function(){
                if (rdata.url) {
                    location.href = rdata.url;
                }
            },time);
        }
      },
    });
}

/**
 * form表单序列化为json对象
 * @returns {{}}
 */
$.fn.serializeObject = function() {
	var o = {};
	var a = this.serializeArray();
	$.each(a, function() {
		if (o[this.name] !== undefined) {
			if (!o[this.name].push) {
				o[this.name] = [o[this.name]];
			}
			o[this.name].push(this.value || '');
		} else {
			o[this.name] = this.value || '';
			//多选需要特殊处理
			if($('#'+this.name).attr('type') == 'multipleSelect'){
				var selectedArray = $('#'+this.name).multipleSelect('getSelects');
				var selected = ''
				for (var i = 0; i < selectedArray.length; i++) {
					selected += selectedArray[i];
					if(i != selectedArray.length - 1){
						selected += '、';
					}
				}
				o[this.name] = selected;
			}
		}
	});
	return o;
};

/**
 * 初始化验证表单。
 * @param formId
 */
function initValidForm(formId){
    var form = $('#'+formId);
    //因为jQuery对象永远都有返回值
    if(form.length > 0){
        form.Validform({
            tiptype:4,
            btnSubmit:".ajaxPost",
            callback:function(form){
                //验证通过不直接提交表单，而通过ajax自己处理
                return false;
            }
        });
    }
}
