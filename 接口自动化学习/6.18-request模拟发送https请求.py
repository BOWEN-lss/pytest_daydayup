#https请求

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning#导入消除告警信息
urllib3.disable_warnings(InsecureRequestWarning)#消除告警
url = 'https://www.httpbin.org/post'
res = requests.post(url,verify=False)#关闭SSL认证
print(res.json())
