# 1.打开请求地址
from selenium import webdriver # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
import time  # 导入time模块
option = webdriver.ChromeOptions() # 创建ChromeOptions对象
option.binary_location = r"D:\software\Chrome\Google\Chrome\Application\chrome.exe" # 指定浏览器路径

# 使用Service管理ChromeDriver
service = Service(ChromeDriverManager().install()) # 创建Service对象
driver = webdriver.Chrome(service=service, options=option) # 创建浏览器对象

# 使用chromewebdriver.exe打开chrome浏览器   chromewebdriver.exe 的下载地址如下：（113-142版本）
# https://www.cnblogs.com/aiyablog/articles/17948703

# 使用driver实例调用get方法
driver.get('https://www.baidu.com') # 打开指定网址

# 2.driver 的常用属性
# 获取当前页面的标题
# t= driver.title
# print(t)

# # 获取当前页面的地址（URL）
# U =driver.current_url
# print(U)

# # 获取当前页面的源代码 (需要对页面进行抓取时使用)
# s = driver.page_source
# print(s)



# 3.页面的其他方法 

# 页面的刷新
# time.sleep(2) # 暂停2秒
# driver.refresh() # 刷新页面

# # 页面的回退
# time.sleep(2) # 暂停2秒
# driver.back()

# # 页面的前进
# time.sleep(2) # 暂停2秒
# driver.forward()

# # 获取当前页面的cookies
# cookies = driver.get_cookies()

# # 设置cookies
# driver.add_cookie({'name':'username','value':'admin'})

# # 删除cookies
# driver.delete_cookie('username')

# 页面截图
# 方式一：
# data = driver.get_screenshot_as_png()
# with open('baidu.png','wb') as f:  # 保存图片
#     f.write(driver.data()) 
# 方式二：
driver.get_screenshot_as_file('baidu2.png')

# 设置浏览器打开后不自动关闭
time.sleep(5)  
driver.quit()

