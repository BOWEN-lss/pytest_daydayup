# http协议中请求的组成
# 一、请求报文的构成
# 请求报文由请求行、请求头和请求体组成。
#   1. 请求行（Request Line）
#   作用：告诉服务器要做什么   包含内容：请求方法（如 GET、POST 等） 、请求的URL路径  、 使用的HTTP版本
    # 2. 请求头（Request Headers）
    # 作用：提供关于请求的附加信息
    # 常见头部字段： Host：目标服务器的主机名 、 User-Agent：客户端的信息（浏览器类型等） 
    #  Content-Type：发送内容的格式 、 Authorization：身份验证信息
    #  content-type  规定了请求体的数据格式，如果是json数据，则Content-Type为application/json；
    #  如果是表单数据，则Content-Type为application/x-www-form-urlencoded；如果为txt数据，则Content-Type为text/plain
    # 3. 空行（Empty Line）
    # 作用：分隔请求头和请求体
    # 特点：必须存在，是一个完全空白的行
    # 4. 请求体（Request Body）
    # 作用：实际要发送给服务器的数据
    # 使用场景：POST请求中提交表单数据、PUT请求中更新资源 、文件上传等操作
# 二、模拟请求需要准备哪些参数？
    # 1. 请求方法  GET POST PUT DELETE 等
    # 2. 请求URL  http://www.baidu.com 等
    # 3. 请求头  包含内容很多，重点传以下几个即可
    # Host    目标服务器的主机名
    # User-Agent   产生请求的浏览器类型，用于区分该请求是浏览器发的还是脚本发的
    # Content-Type  发送端发送的数据格式
    # cookie  登录信息

 
