#接口响应：text/html解析
import re
import requests
url = 'http://httpbin.org/html'
res = requests.get(url)
print(res.status_code) #接口的状态码

#响应体内容
content = res.text  #获取响应体内容
print(content)

#解析响应体内容
res2 = re.findall('<h1>(.*?)</h1>',content)[0]
print(res2)