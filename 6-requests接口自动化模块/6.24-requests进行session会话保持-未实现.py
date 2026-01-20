"""
requests进行session会话保持
session会话保持是将登录成功后的cookies传递给登录后的接口，来告知后台当前接口是有请求权限的
"""
未找到合适的网址，未实现
# import requests
# url = 'https://zentaobiz.demo.qucheng.cc/index.php?m=my&f=profile&onlybody=yes'
# headers = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 QuarkPC/6.1.0.653'}
# res1=requests.get(url,headers=headers)
# print(res1.text)  # 结果显示与抓包显示结果不一致，说明接口是通的，但是cookies没有传递成功，因此需要先登录成功，抓取cookies，创建会话保持器，再进行登录后的接口请求

# 先登录成功，抓取cookies
import requests
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 创建session对象
session = requests.Session()

# 目标URL
url = 'https://hardware.demo.qucheng.cc/index.php?m=user&f=login'

# 请求体数据
request_data = {
"account":'demo',
"password":'8f904ec3dae031b8438c4a1c2641c3a2',
"passwordStrength":'1',
"referer":'/',
"verifyRand":'1708603301',
"keepLogin":'0'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 QuarkPC/6.1.0.653',
    'Content-Type': 'text/html; Language=UTF-8;charset=UTF-8'
}

# 发送登录请求
res = session.post(url, data=request_data, headers=headers, verify=False)

print("登录响应状态码:", res.status_code)
print("登录响应内容:", res.text)

# 登录成功后，session会自动保持cookies，可以访问其他需要登录的页面
# 例如访问用户信息页面
# profile_url = 'https://passport.bilibili.com/x/passport-login/web/profile'
# profile_res = session.get(profile_url, verify=False)
# print("用户信息:", profile_res.text)

