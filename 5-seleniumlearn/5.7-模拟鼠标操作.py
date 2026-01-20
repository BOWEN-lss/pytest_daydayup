# 模拟鼠标操作   模拟鼠标点击、拖拽、悬停 操作
from selenium.webdriver.common.action_chains import ActionChains

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
driver.get(r'D:\python_learn\seleniumlearn\鼠标-键盘操作测试.html')  # 打开鼠标点击测试网站

"""
鼠标点击   跟 click 效果一样，区别在于 
1.click()：直接在元素上执行点击操作 ；ActionChains 先构建一个动作链，然后通过 perform() 方法执行
2.click()：只能执行简单的点击操作  ；ActionChains：支持复杂的鼠标操作序列，如：拖拽 (drag_and_drop)，右键点击 (context_click)，
双击 (double_click) ，鼠标悬停 (move_to_element) ，组合操作链 ActionChains(driver).click(el1).perform() 等。
更适用于需要模拟真实用户复杂交互的场景
"""



# 定位元素
el1= driver.find_element(By.XPATH, '//button[@id="btnC"]')   # 获取单击按钮元素 el1
ActionChains(driver).click(el1).perform()   # 鼠标单击

time.sleep(2)



el2= driver.find_element(By.XPATH,"//*[@id='rightBtn']")  # 获取鼠标右键点击按钮元素 el2        
ActionChains(driver).context_click(el2).perform()  # 鼠标右键点击

time.sleep(2)

el11= driver.find_element(By.XPATH,"//*[@id='btnD']")    #  获取双击按钮元素 el11

ActionChains(driver).double_click(el11).perform() # 鼠标双击
time.sleep(2)

el6= driver.find_element(By.XPATH,"//button[contains(text(),'悬停 A')]")  # 获取悬停按钮A的元素定位
el7= driver.find_element(By.XPATH,"//button[contains(text(),'悬停 B')]")  # 获取悬停按钮B的元素定位

ActionChains(driver).move_to_element(el6).perform()  # 鼠标悬停在按钮A
time.sleep(1)
ActionChains(driver).move_to_element(el7).perform() # 鼠标悬停在按钮B
time.sleep(1)


el4= driver.find_element(By.XPATH,"//*[@id='dragA']")  # 拖拽起点
el5= driver.find_element(By.XPATH,"//*[@id='dropB']") # 拖拽终点
ActionChains(driver).drag_and_drop(el4,el5).perform()  # 鼠标拖拽
# ActionChains(driver).click_and_hold(el4).release(el5).perform()     # 用按下松开的方式拖拽
time.sleep(2)









