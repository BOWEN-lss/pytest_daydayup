"""
解析text/html响应
当看到响应体的格式为content-type:text/html;charset=utf-8'时，则可以通过res.text 来获取响应体的全部内容，然后用正则表达式提取出需要的数据
"""
import requests
url  = 'http://httpbin.org/html'
res =  requests.get(url)
# print(res.status_code)  # 获取响应状态码

# 响应状态码为200只能保证接口是通过的，不能保证接口返回的数据是正确的

# 获取响应体的内容
content = res.text
# print(content)
# 解析响应体内容 用正则表达式提取想要的数据
import re   # 导入正则表达式模块
res2=re.findall(r'<h1>(.*?)</h1>',content)[0]   # fiandall()方法用于查找正则表达式匹配到的所有文本的值，返回的是一个列表
print(res2)

# 正则表达式的写法：
# 1.单独查找指定的值
res3=re.findall(r'\btimely\b',content)[0]   # \b 表示单词边界, \btimely\b 确保匹配的是timely这个完整单词
print(res3)

# 2.查找包含指定内容的完整句子
res4=re.findall(r'[^.]timely[^.]*\.',content)[0]
print(res4)

# 3.获取指定内容及周围指定范围的文本
res5=re.findall(r'.{0,10}timely.{0,10}',content)[0]  # 匹配 timely 及前后的10个字符
print(res5)

# 之所以再每个res后面加上 [0] 是因为 findall() 函数返回的是一个列表，而列表的索引从0开始，这样取出来的就是列表中第一个值，而不是列表本身
