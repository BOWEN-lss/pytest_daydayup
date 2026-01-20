# 模拟浏览器相关操作
# 1.创建浏览器对象
from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
import time  # 导入time模块

option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.binary_location = r"E:\chrome\Chrome\Application\chrome.exe"   # 指定浏览器路径
driver = webdriver.Chrome(options=option)  # 创建浏览器对象

driver.get('https://www.baidu.com')  # 打开百度首页
driver.maximize_window()            # 最大化浏览器窗口
driver.set_window_size(800,400)  # 设置浏览器窗口大小
p = driver.get_window_position()  # 获取浏览器窗口位置
print(p, 666666666666666666)  # 打印浏览器窗口位置
driver.set_window_position(100,100) # 设置浏览器窗口位置

time.sleep(2)  # 暂停2秒
driver.quit()  # 关闭浏览器

# chrome 浏览器驱动国内华为云下载地址：  https://mirrors.huaweicloud.com/chromedriver/