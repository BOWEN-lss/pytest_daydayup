"""
import 语句导入模块
from ...import 语句导入模块

"""
from http.client import responses

# import requests
# # 调用 requestes 模块的 get 方法
# responses=requests.get('https://www.baidu.com')
# print(responses.status_code)

# 导入自定义的模块
import my_function
my_function.print_name('张三')

# 导入模块中指定的一部分
from my_function import print_name
print_name('李四')

# 导入模块中所有部分
from my_function import *
print('wangwu')
