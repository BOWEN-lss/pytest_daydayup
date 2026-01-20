# 元素的三种等待方式

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
driver.get('http://sahitest.com/demo/waitFor.htm')

# 一、强制等待：time.sleep()  不管元素有没有加载出来，都必须强制等待指定的时间。缺点是严重影响程序执行速度
# time.sleep(5)

el2=driver.find_element(By.XPATH,".//input[@value='Click me']")  # 获取点击按钮的是元素定位
el2.click()   # 点击按钮
# time.sleep(1)  # 强制等待0.5秒
# print(el1.text)  # 查看0.5秒后能否获取到元素文本（结果为获取不到 原因是元素加载时间大于0.5秒）

# time.sleep(2)  # 强制等待2秒 
# el1=driver.find_element(By.ID,'id2')   # 获取元素文本（暂未显现）
# print(el1.text)  # 查看2秒后能否获取到元素文本（结果为获取到）

# 二、隐式等待：设置一个最长等待时间，当元素加载出来时，立即返回元素对象，当元素没有加载出来时，等待指定的时间，直到元素加载出来。
# 缺点是如果元素没有加载出来，就会一直等待，直到超时为止。
# driver.implicitly_wait(5)
# el1=driver.find_element(By.ID,'id2')   # 获取元素文本（暂未显现）
# print(el1.text) 

# 三、显式等待：设置一个最长等待时间，然后设置时间间隔，让程序每个XX秒看一次有没有加载出来，
# 当元素加载出来时，立即返回元素对象，当元素没有加载出来时，等待指定的时间，直到元素加载出来。
# 优点是如果元素没有加载出来，就会一直等待，直到元素加载出来。
from selenium.webdriver.support.ui import WebDriverWait  # 导入WebDriverWait模块
from selenium.webdriver.support import expected_conditions as EC # 导入expected_conditions模块
locat= (By.ID,'id2')
wait = WebDriverWait(driver, 10,0.1).until(EC.presence_of_element_located((locat)))
print(wait.text)
