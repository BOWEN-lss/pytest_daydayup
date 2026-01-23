import requests

#获取cookie
url_cookie = 'https://ztbowen.chandao.net/user-refreshRandom.html'
header_cookie = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
    "Referer":"https://ztbowen.chandao.net/user-login.html"
}
res_cookie = requests.get(url_cookie,headers=header_cookie)
d = requests.utils.dict_from_cookiejar(res_cookie.cookies)
print(d)

#密码的加密
#1.获取rand
url_rand = 'https://ztbowen.chandao.net/user-login.html'
header_rand = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
    "X-Requested-With":"XMLHttpRequest",
    "Referer":"https://ztbowen.chandao.net/user-login.html"
}
res_rand = requests.get(url_rand,headers=header_rand,cookies=d)
print(res_rand.text)

#2.python实现调用js文件中的md5方法
password = '123456'
from encrypt import ExecJs
e = ExecJs()
step1 = e.get_encrypt_pwd('md5',password)
step2 = e.get_encrypt_pwd('md5',step1 + res_rand.text)
print(step2)


#禅道登录
url = 'https://ztbowen.chandao.net/user-login.html'
data = {
    "account":"7sgub1al7j",
    "password":step2,
    "passwordStrength":"0",
    "referer":"/",
    "verifyRand":res_rand.text,
    "keepLogin":"1",
    "captcha":""
}
header = {
    "Host":"ztbowen.chandao.net",
    "Connection": "keep-alive",
    "Content-Length":"133",
    "sec-ch-ua-platform":"Windows",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://ztbowen.chandao.net/user-login.html",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6",
    "Cookie": "zentaosid=f8v5bvi8h3ited3pr5ha11good; lang=zh-cn; device=desktop; theme=default; windowWidth=1912; windowHeight=914"

}
res =requests.post(url,data=data,headers=header,cookies=d)
print(res.text)