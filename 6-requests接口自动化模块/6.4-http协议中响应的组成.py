# http协议中响应的组成
# 响应报文的组成 ： 响应行 + 响应头 + 响应体
# 响应行: 包括 协议版本：HTTP/1.1 、响应状态码:200 、原因短语:OK
# 响应头: 包括响应头字段:Content-Type:text/html;charset=utf-8
# 响应体: 响应内容

# 响应数据的几种格式:
# 与请求体一样，响应头中content-type字段可以指定响应体的数据格式,requests模块中对不同的响应数据的获取方式是不同的
# 1.json类型的响应数据: 响应头中content-type字段的值为application/json；charset=utf-8 时，响应体中是{}形式的json类型
# 2.html类型的响应数据: 响应头中content-type字段的值为text/html;charset=utf-8 时，响应体中是html类型的数据
# 3.xml类型的响应数据: 响应头中content-type字段的值为application/xml;charset=utf-8 时，响应体中是xml类型的数据
# 4.图片类型的响应数据: 响应头中content-type字段的值为image/png/jpeg 等的时候，响应体中是图片、音乐、视频等静态资源的数据
