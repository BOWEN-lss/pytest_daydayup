"""
post请求体的data格式传参
什么情况下可以用data格式传参：
请求体(content-type)格式为 application/x-www-form-urlencoded 时，可以用data格式进行传参
传参的格式可以是字符串，也可以是字典

"""
import requests
url='http://httpbin.org/post'
# data参数的两种传递方式
# 字典格式
# dict_data = {'key1':'value1','key2':'value2'}
# res = requests.post(url,data='dict_data')
# print(res.json())

# 字符串格式
str_data = 'key1=value1&key2=value2'
res = requests.post(url,data='str_data')
print(res.json())

