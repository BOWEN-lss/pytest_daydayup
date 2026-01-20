"""
seleniumlearn.模拟系统弹窗操作  系统弹窗无法通过元素定位的方法来获取元素 无法定位
系统弹窗类型：
1. Alert   警告弹窗 包含提示信息和确认按钮 
2. confirm 确认框   包含提示信息和确认和取消按钮
3. promopt 提示框   包含提示信息和输入框和确认和取消按钮
4. File Upload        文件上传框       包含提示信息和上传文件按钮
5. 窗口框           弹出多个窗口
"""

# 模拟系统弹窗操作
#  1.Alert  警告弹窗
#  获取弹窗文本

from selenium import webdriver  # 导入selenium模块
from selenium.webdriver.chrome.service import Service  # 导入Service模块
import time  # 导入time模块
from selenium.webdriver.common.by import By  # 必须导入 By 类
service = Service(executable_path=r"D:\software\Chrome\Google\Chrome\Application\chromedriver.exe") # 创建Service对象并指定驱动程序路径

option = webdriver.ChromeOptions()  # 创建ChromeOptions对象
option.add_experimental_option("detach", True)    # 设置浏览器不自动关闭  detach 在这里的意思是：分离/脱离：让浏览器进程与自动化脚本进程分离，即使脚本执行结束或异常退出，浏览器也不会被自动关闭
option.binary_location = r"D:\software\Chrome\Google\Chrome\Application\chrome.exe"   # 指定浏览器路径

driver = webdriver.Chrome(service=service,options=option)  # 创建浏览器对象
time.sleep(0.1)   # 等待0.1秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get(r'D:\python_learn\seleniumlearn\原生弹窗练习.html')  # 打开鼠标点击测试网站

# 生成 Alert 弹窗
# el1=driver.find_element(By.XPATH,"//button[contains(text(),'测试Alert')]")
# el1.click()
# time.sleep(1)

# # 获取弹窗文本
# alert = driver.switch_to.alert  # 获取弹窗对象 
# alert_text=alert.text

# # 点击弹窗确定
# alert.accept() 
# time.sleep(5)


# 2.confirm 确认框
# 获取弹窗文本
# el2=driver.find_element(By.XPATH,"//button[contains(text(),'测试Confirm')]") # 获取按钮元素 el2
# el2.click()
# time.sleep(1)
# # 获取弹窗对象
# confirm = driver.switch_to.alert
# b=confirm.text
# print(b)
# 点击确定按钮
# confirm.accept()  
# 点击取消按钮
# confirm.dismiss()

# 3.prompt 提示框
el3=driver.find_element(By.XPATH,"//button[contains(text(),'测试Prompt')]")
el3.click()
time.sleep(1)
prompt = driver.switch_to.alert # 获取弹窗对象
prompt.text # 获取弹窗文本
prompt.send_keys("试试能不能输进去")
# time.sleep(1)
# prompt.accept()  # 点击确定按钮
prompt.dismiss() # 点击取消按钮


