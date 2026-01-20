"""
Cookies、Session 和 Token 的区别

一、Cookies 解释
Cookies 是存储在用户浏览器中的小型文本文件，用于：
- 记住用户的登录状态
- 存储用户偏好设置
- 跟踪用户行为
- 维持会话状态

二、Cookies、Session 和 Token 的区别

Cookies：
- 存储位置：客户端浏览器
- 生命周期：可设置过期时间
- 大小限制：每个 Cookie 约 4KB
- 用途：存储简单数据，如用户 ID、偏好设置等

Session：
- 存储位置：服务器端
- 生命周期：通常在用户关闭浏览器或超时后失效
- 安全性：较高，数据存储在服务器
- 用途：存储敏感信息和临时数据

Token：
- 存储位置：客户端（通常在 localStorage 或 sessionStorage 中）
- 生命周期：可自定义过期时间
- 传输方式：通常在 HTTP 请求头中传递
- 用途：API 认证和授权

三、主要区别对比表
特性        Cookies     Session     Token
存储位置    客户端      服务器      客户端
自动发送    是          否          否
安全性      较低        高          中等
大小限制    有          无          无
跨域支持    有限制      无          有
"""
from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
import time  # 导入time模块
from selenium.webdriver.common.by import By  # 必须导入 By 类
service = Service(executable_path=r"D:\software\Chrome\Google\Chrome\Application\chromedriver.exe") # 创建Service对象并指定驱动程序路径
option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.add_experimental_option("detach", True)    # 设置浏览器不自动关闭  detach 在这里的意思是：分离/脱离：让浏览器进程与自动化脚本进程分离，即使脚本执行结束或异常退出，浏览器也不会被自动关闭
option.binary_location = r"D:\software\Chrome\Google\Chrome\Application\chrome.exe"   # 指定浏览器路径
driver = webdriver.Chrome(service=service,options=option)  # 创建浏览器对象
time.sleep(0.2)   # 等待0.5秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get('https://aiso.jikeyunsou.com/')
# Selenium 中操作 Cookies 示例



# 获取单个 cookie
# cookie = driver.get_cookie('_clck') # _clck 为cookie里name的值
# print(cookie)

# 添加 cookie
cookie={'name': '你瞅啥', 'value': '瞅你咋地'}
driver.add_cookie({'name': '你瞅啥', 'value': '瞅你咋地'})

# time.sleep(2)
# 获取所有 cookies
# cookies = driver.get_cookies()
# print(cookies)
time.sleep(2)
# 删除 cookie
# driver.delete_cookie('你瞅啥')
# time.sleep(2)



# # 清除所有 cookies
driver.delete_all_cookies()

cookies = driver.get_cookies()
print(cookies)

