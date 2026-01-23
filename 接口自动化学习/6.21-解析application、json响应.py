#接口响应：json解析

import requests
url = 'http://httpbin.org/json'
res = requests.get(url)
print(res.status_code)

#获取响应体的内容
content = res.json()
print(content,type(content))

#解析接口响应
author = content['slideshow']['author']
print(author)