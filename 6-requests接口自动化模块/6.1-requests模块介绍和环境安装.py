"""
requests模块介绍和环境安装
requests模块介绍:
requests模块是一个用于发送http请求的库,使用requests模块,可以非常方便的发送http请求,并且可以自动处理http请求的响应。
requests库的7个主要方法:

requests.request(method, url, **kwargs) # 发送http请求
requests.get(url, **kwargs) # 发送get请求
requests.head(url, **kwargs) # 发送head请求
requests.post(url, **kwargs) # 发送post请求
requests.put(url, **kwargs) # 发送put请求
requests.patch(url, **kwargs) # 发送patch请求
requests.delete(url, **kwargs) # 删除请求

reseponse 对象属性:
response.status_code # 响应状态码  200 表示请求成功  404 表示请求失败
response.text # 响应内容
response.content # 响应内容 bytes类型
response.encodin # 响应编码
response.headers # 响应头

requests 安装
在线安装:
pip install requests

离线安装:
在 https://pypi.org/project/ 找到requests的安装包
下载.whl文件 到本地任意位置
在whl文件所在位置进入cmd  执行 pip install requests-2.26.0-py2.py3-none-any.whl 
即可完成离线安装 
"""

