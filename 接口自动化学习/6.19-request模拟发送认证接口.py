#auth 认证接口

import requests
#1.基本身份认证

# from requests.auth import HTTPBasicAuth
# url = 'http://www.httpbin.org/basic-auth/user/pass'
# res = requests.get(url,auth=HTTPBasicAuth('user','pass'))
# print(res.json())

#2.摘要式身份认证
# import requests
# from requests.auth import HTTPDigestAuth
# url = 'http://httpbin.org/digest-auth/undefined/user/pass'
# res = requests.get(url,auth=HTTPDigestAuth('user','pass'))
# print(res.json())

#3.token认证
#事先模拟登陆
url = 'http://httpbin.org/post'
heater = {'authorization':'dasdasdasdasdasd'}
res = requests.post(url,headers= heater)
print(res.text)
