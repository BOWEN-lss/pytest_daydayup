""""
单选/复选框操作
一、复选框勾选
二、单选框勾选
三、判断是否勾选
"""

from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
# from webdriver_manager.chrome import ChromeDriverManager  # 导入ChromeDriverManager模块
import time  # 导入time模块
from selenium.webdriver.common.by import By  # 必须导入 By 类
service = Service(executable_path=r"D:\software\Chrome\Google\Chrome\Application\chromedriver.exe") # 创建Service对象并指定驱动程序路径

option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.add_experimental_option("detach", True)    # 设置浏览器不自动关闭  detach 在这里的意思是：分离/脱离：让浏览器进程与自动化脚本进程分离，即使脚本执行结束或异常退出，浏览器也不会被自动关闭
option.binary_location = r"D:\software\Chrome\Google\Chrome\Application\chrome.exe"   # 指定浏览器路径
# service = Service(ChromeDriverManager().install())  # 创建Service对象

driver = webdriver.Chrome(service=service,options=option)  # 创建浏览器对象
time.sleep(0.2)   # 等待0.5秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get(r'D:\python_learn\seleniumlearn\单选复选框练习.html')  # 打开鼠标点击测试网站
# driver.get('http://sahitest.com/demo/selectTest.htm')

# 一、复选框勾选  有多个选项框时，多个选项框为同一级，可用 xpath  加上位置索引定位
# 方式一：
el1=driver.find_element(By.XPATH,".//input[@id='vscode']")  # id定位第一个复选框位置
from selenium.webdriver.common.keys import Keys  # 新增导入 Keys 类  
el1.send_keys(Keys.SPACE) #  按空格键勾选

time.sleep(2)
# 方式二：
el2=driver.find_element(By.XPATH,"//label[@for='pycharm']") # 按唯一标识定位第二个复选框位置
el2.click()

time.sleep(2) 


# 二、单选框勾选
el3=driver.find_element(By.XPATH,"//label[@for='python']")   # 使用唯一标识定位  方法：标识所在行的标签加上固定格式
el3.click()
time.sleep(2)

# # 方式二
el4=driver.find_element(By.XPATH,"//input[@value='C++']")   # 使用精确文本内容定位 方法：文本所在行的标签加上固定格式
from selenium.webdriver.common.keys import Keys  # 新增导入 Keys 类  
el4.send_keys(Keys.SPACE) 

time.sleep(2)

# el5=driver.find_element(By.XPATH,'//label[contains(text(), "JavaScr")]') # 使用文本内容模糊匹配定位 方法：文本所在行的标签加上固定格式
# el5.click()


# 三、判断是否勾选  注意只有input元素的is_selected()方法才能正确返回选中状态。

res1=el4.is_selected()   # 判断是否勾选
print(res1)
