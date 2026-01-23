#接口响应：静态文件解析

import requests
url = 'http://httpbin.org/robots.txt'
res = requests.get(url)
print(res.status_code) #获取状态码

#获取请求中响应体的内容
c = res.content
print(c,type(c))

#写入文件
with open('robots.txt','wb') as f:
    f.write(c)

 