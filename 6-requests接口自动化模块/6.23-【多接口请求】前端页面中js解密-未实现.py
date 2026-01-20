"""
【多接口请求】前端页面中js解密
"""
import requests
url = 'https://zentaobiz.demo.qucheng.cc/index.php'
data = {'account':'demo','password':'54964daf1d933f62c45a25c49991d349'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
           'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryCR9w8kMMMVAU4lk0'}
res = requests.post(url,data=data,headers=headers)
print(res.text)  # 响应报文中没有包含 result=success 字样，所以算是失败了，原因是登录密码为动态加密，需要先进行解密操作

#破解前端js加密，实现登录接口的调用

# 这个加密的js代码，需要自己写一个解密函数，然后调用这个函数，将解密后的密码传入接口中，进行登录  太复杂，未实现