"""
request模拟 cookie传参
"""

# get 请求中的 cookie 传参
import requests
url = 'http://httpbin.org/cookies'

query_data = {'name':'xiaoming','age':18}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
               ,'Content-Type':'application/json'}

cookies={'__itrace_wid':'ffe7b6cb-b2b7-45f2-08db-f55fdf5710f1'}
res = requests.get(url,params=query_data,headers=headers,cookies=cookies)   # post 传参也是一样，只要把这里的gett 换成 post 就可以了
print(res.json())