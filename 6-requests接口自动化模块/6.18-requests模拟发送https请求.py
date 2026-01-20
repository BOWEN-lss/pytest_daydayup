"""
requests模拟发送https请求
"""
import requests
url = 'https://www.httpbin.org/post'
res = requests.post(url) # 获取响应体信息
print(res.json())  # 输出响应结果

# 如果运行以上代码报错时，可以尝试关闭fiddler抓包软件再试一次 ,操作方法如下
import requests
url = 'https://www.httpbin.org/post'
res = requests.post(url,verify=False) # 获取响应体信息   添加参数verify=False，意思是关闭SSL验证
print(res.json())  # 输出响应结果

# 到这一步如果存告警信息时，可以引入urllib3模块消除告警信息
import urllib3  # 引入urllib3模块
from urllib3.exceptions import InsecureRequestWarning  # 从urllib3模块中导入InsecureRequestWarning类
urllib3.disable_warnings(InsecureRequestWarning) # 禁用告警信息
import requests
url = 'https://www.httpbin.org/post'
res = requests.post(url,verify=False) # 获取响应体信息   添加参数verify=False，意思是关闭SSL验证
print(res.json())  # 输出响应结果