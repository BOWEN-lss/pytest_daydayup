"""
6.14-post请求体的file传参
当请求体中的content-type为multipart/form-data时，请求体中的参数会以文件形式传递给服务器。
"""
import requests 
url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}  # 创建文件对象
res = requests.post(url, files=files) # 发送POST请求
print(res.json()) # 输出响应结果