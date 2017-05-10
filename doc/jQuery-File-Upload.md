## jQuery File Upload

> File Upload widget with multiple file selection, drag&drop support, progress bar, validation and preview images, audio and video for jQuery.

[https://github.com/blueimp/jQuery-File-Upload](https://github.com/blueimp/jQuery-File-Upload)

[jQuery File Upload Demo](https://blueimp.github.io/jQuery-File-Upload/)


### Requirements

#### Mandatory requirements

- [jQuery](https://jquery.com/)
- [jQuery UI widget factory](https://api.jqueryui.com/jQuery.widget/)
- [jQuery Iframe Transport plugin](https://github.com/blueimp/jQuery-File-Upload/blob/master/js/jquery.iframe-transport.js)

#### Optional requirements

- [Bootstrap](http://getbootstrap.com/)
- [Glyphicons](http://glyphicons.com/)
- [JavaScript Templates engine](https://github.com/blueimp/JavaScript-Templates)


### JSON Response

[https://github.com/blueimp/jQuery-File-Upload/wiki/JSON-Response](https://github.com/blueimp/jQuery-File-Upload/wiki/JSON-Response)

[The newer response is documented](https://github.com/blueimp/jQuery-File-Upload/wiki/Setup#using-jquery-file-upload-ui-version-with-a-custom-server-side-upload-handler)


### Basic plugin

[Basic plugin](https://github.com/blueimp/jQuery-File-Upload/wiki/Basic-plugin)


### Server Code

[server/php/UploadHandler.php](https://github.com/blueimp/jQuery-File-Upload/blob/master/server/php/UploadHandler.php)


### Usage

初始化
```
$('#fileupload').fileupload();
```

也可以带参数
```
$('#fileupload').fileupload({
    url: '/path/to/upload/handler.json',
    sequentialUploads: true
});
```

也可以使用下面的方式设置参数
```
<input id="fileupload" type="file" name="files[]" multiple
    data-url="/path/to/upload/handler.json"
    data-sequential-uploads="true"
    data-form-data='{"script": "true"}'>
```


### Other Example

不想使用模板引擎，可以如下操作：
```
<script>
    $(function () {
        //文件上传地址
        var url = '{{ url_for('uploads') }}';
        //初始化，主要是设置上传参数，以及事件处理方法(回调函数)
        $('#fileupload').fileupload({
            autoUpload: true,//是否自动上传
            url: url,//上传地址
            dataType: 'json',
            done: function (e, data) {//设置文件上传完毕事件的回调函数
                console.log(data);

                $.each(data.files, function (index, file) {
                    //$('<p/>').text(file.name).appendTo($('#upload_list'));
                    var html_text = '<tr class="template-upload fade in">';
                    html_text += '<td><p class="name">'+file.name+'</p></td>';
                    html_text += '<td><span class="size">'+file.size+'</span></td>';
                    html_text += '<td>' +
                            '<button class="btn btn-primary start"><i class="glyphicon glyphicon-upload"></i><span>Start</span></button> ' +
                            '<button class="btn btn-warning cancel"><i class="glyphicon glyphicon-ban-circle"></i><span>Cancel</span></button>' +
                            '</td>';
                    html_text += '</tr>';
                    $(html_text).appendTo($('tbody.files'));
                });

            },
            progressall: function (e, data) {//设置上传进度事件的回调函数
                var progress = parseInt(data.loaded / data.total * 100, 10);
                $('#progress .bar').css(
                    'width',
                    progress + '%'
                );
            }
        });
    });
</script>
```


python html页面变量替换

```
thumbnailUrl    thumbnail_url
deleteUrl       delete_url
deleteType      delete_type
```
