"""
requests模拟headers传参
headers传参:（非必选项，可以传也可以不传，最好还是传下面两个重要的请求头信息）

user-agent:浏览器的用户代理字符串，告诉http服务器，客户端使用的操作系统和浏览器的名称及版本
content-type:告诉http服务器，客户端发送的请求消息携带的数据类型，方便服务器接收后以合适的方式处理
"""

# post  请求中的 headers 传参
import requests
url = 'http://httpbin.org/post?name=xiaomomg&age=18'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      'content-type':'application/json'}

res = requests.post(url,headers=headers) # 发送post请求
print(res.json())# 输出结果
# 如果不能请求成功，可以多添加几个请求头信息，甚至全部添加进去

# get 请求中的 headers 传参
import requests
url = 'http://httpbin.org/get?name=xiaomomg&age=18'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
 }
res = requests.get(url,headers=headers)
print(res.json())