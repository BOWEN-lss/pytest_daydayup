"""
解析application/json响应
可以通过res.json()的方式获取json格式的响应数据，python会自动把json格式的数据认为是字典格式，所以可以用字典取值的方式来提取需要的数据
"""
import requests
url = 'http://httpbin.org/json'
res = requests.get(url)
print(res.status_code)   # 获取状态码

# 获取响应体的内容
content = res.json()
print(content)

# 解析接口响应
content1=content['slideshow']['author']    # 获取响应体中 author 的值
print(content1)

content2 = content['slideshow']['slides'][0]['title']  # 获取json响应体数据中第三层 title 的值
print(content2)
