"""
request模拟发送认证接口
认证接口种类有：
http Basic Auth 基本身份认证   当请求体的 Authorization 值为 Basic 时，可以确定接口为基本身份认证接口
Degist Authentication   摘要式身份认证   当请求体的 Authorization 值为 Degist 时，可以确定接口为摘要式身份认证接口
token 认证  当请求体的 Authorization 值为Bearer 时，可以确定接口为  token 认证接口
"""

# http Basic Auth 基本身份认证  
import requests
# from requests.auth import HTTPBasicAuth  # 从requests模块的auth包中导入HTTPBasicAuth类
# url = 'http://httpbin.org/basic-auth/user/pass'
# res = requests.get (url,auth=HTTPBasicAuth('user','pass'))  # user 和 pass是认证接口的账号和密码，实际工作中可以向开发确认
# print(res.json())
"""
 认证接口返回结果：
 {
  "authenticated": true,
  "user": "user"
}
"""
# 如果不传 HTTPBasicAuth 类的参数，则返回 401 错误


# 摘要式身份认证
from requests.auth import HTTPDigestAuth  # 引入摘要式认证模块
url1 = 'http://httpbin.org/digest-auth/auth/user/pass'
res1 = requests.get(url1,auth=HTTPDigestAuth('user','pass'))
print(res1.json())

# 认证接口返回结果：
{
  "authenticated": true,
  "user": "user"
}


# token 认证 
# token 是服务端生成的一个字符串，作为客户端请求的一个令牌，当第一次登陆后，服务端会返回一个 token，后续的请求中，
# 客户端会带上这个 token，而无需再次携带用户名和密码。服务端会验证这个 token 是否有效，如果有效，则返回数据，否则返回错误。

# token值一般通过请求头中的authorization 字段传递，登录成功后会返回token值，将token值传入登录后的接口的请求头即可请求成功
# token是登录后返回的，所以抓取token需要事先模拟登录成功
import requests
url = 'http://httpbin.org/post'
header = {'authorization': 'token'}
res = requests.post(url, headers=header) 
print(res.text)