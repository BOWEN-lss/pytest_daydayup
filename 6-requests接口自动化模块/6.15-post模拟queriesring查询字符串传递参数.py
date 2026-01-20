"""
post模拟queriesring查询字符串传递参数
在url中存在？等一系列参数，这些参数就是查询字符串，也可以在fiddler的webforms中查看
"""
import requests
url = 'http://httpbin.org/post'
dict = {'name':'xiaoming','age':'18'}
# webforms 中有 body ，说明有请求体，有请求体的情况下需要添加请求体
dict2= {'say':'hello python!'}
res= requests.post(url,dict,data=dict2)
print(res.json())


# get 请求中中也存在查询字符串
url = 'http://httpbin.org/get'
dict3t = {'name':'xiaoming','age':'18'}
res = requests.get(url,params=dict3t) # get请求中没有请求体，所以直接传入url和查询字符串就可以了
print(res.json())


