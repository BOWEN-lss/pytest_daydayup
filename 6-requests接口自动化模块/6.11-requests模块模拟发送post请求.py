"""
requests模块模拟发送post请求
语法：
requests.post(url, data=None, json=None, **kwargs)
url: 接口的请求地址，必填项
params: 请求的参数（选填，填入url后面的查询字符串，如?name=xiaobai&age=98。 可以是data格式，也可以时json格式。）
**kwargs: 其他的参数(选填,代表还可以传其他参数，如headers，cookies等)
返回值: Response对象
"""
import requests
res1=requests.post('https://httpbin.org/post', data={'key': 'value'})
print(res1.json())