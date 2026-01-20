"""
模拟操作页面元素
1. 模拟按钮点击操作
2. 文本框操作 
3. 获取元素文本
4. 获取元素属性
"""

# 1. 模拟按钮点击操作
# 语法：element.click()   参数值 ：无   返回值：无
from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
import time  # 导入time模块
from selenium.webdriver.common.by import By  # 必须导入 By 类
# service = Service(executable_path=r"D:\software\Chrome\Google\Chrome\Application\chromedriver.exe") # 创建Service对象并指定驱动程序路径
from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.add_experimental_option("detach", True)    # 设置浏览器不自动关闭  detach 在这里的意思是：分离/脱离：让浏览器进程与自动化脚本进程分离，即使脚本执行结束或异常退出，浏览器也不会被自动关闭
option.binary_location = r"E:\chrome\Chrome\Application\chrome.exe"   # 指定浏览器路径
# driver = webdriver.Chrome(service=service,options=option)  # 创建浏览器对象
driver = webdriver.Chrome(options=option)  # 创建浏览器对象
time.sleep(0.2)   # 等待0.5秒
driver.maximize_window()       # 最大化浏览器窗口

driver.get('https://www.baidu.com')  # 打开百度首页

# 进行元素定位   返回元素对象
# el1 = driver.find_element(By.XPATH,".//*[@id='chat-submit-button']")   # 通过xpath结合文本内容定位元素

# 针对元素对象进行模拟操作
# el1.click()   # 点击元素

# 2. 文本框操作  包含清空和输入操作
# 语法： 清空：element.clear()   输入：element.send_keys('hello')
el2 = driver.find_element(By.XPATH,"//*[@id='chat-textarea']")  # 定位输入框
el2.clear()  # 清空输入框
el2.send_keys('hello') # 输入框中输入文本
time.sleep(1)  # 暂停1秒
el1 = driver.find_element(By.XPATH,".//*[@id='chat-submit-button']")  # 定位提交按钮
print(el1.text)   # 3. 获取元素文本
a=el1.get_attribute('id')  # 4. 获取元素属性
print(a)
el1.click()  # 点击提交按钮




