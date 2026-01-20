"""
requests模块模拟发送get请求
语法: requests.get(url, params, **kwargs)
url: 接口的请求地址，必填项
params: 请求的参数（选填，填入url后面的查询字符串，如?name=xiaobai&age=98）
**kwargs: 其他的参数(选填,代表还可以传其他参数，如headers，cookies等)
返回值: Response对象
"""
# 简单的get请求
import requests
# res1=requests.get('http://httpbin.org/get')
# print(res1.text)

# 2.拆分服务器地址和接口路径
from urllib.parse import urljoin  # 从 urllib.parse 库中导入 urljoin 方法
service_url = 'http://httpbin.org'  # 服务器地址
api_url = '/get'  # 接口路径  
url=urljoin(service_url,api_url)  # 拼接服务器地址和接口路径
print(url)
# 拼接服务器地址和接口路径的目的是以后的工作中只需要替换服务器地址即可测试不同的项目
res2=requests.get(url)  # 发送get请求
print(res2.json())   # 获取响应结果