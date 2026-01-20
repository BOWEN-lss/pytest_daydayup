"""
测试网站:http://sahitest.com/demo/ 
模拟 seleniumlearn中下拉框操作的操作  （适用于 select 标签）
一、会选择下拉项的下拉 （单选）
二、会取消已选择的下拉框里的下拉项  （多选） 适用于select 标签后带 multiple 属性
三、会获取下拉项的值
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
driver.get(r'D:\python_learn\seleniumlearn\下拉框练习.html')  # 打开鼠标点击测试网站
# driver.get('http://sahitest.com/demo/selectTest.htm')

# 一、 选择下拉项的方法： 单选
# 1.按照索引选择下拉项  索引从0开始 第一个选项为0
from selenium.webdriver.support.ui import Select  # 正确的导入select模块
el1= driver.find_element(By.ID, 'basicSelect')
# s= Select(el1)  # 实例化一个select对象
# s.select_by_index(2)  # 按照索引选择下拉项

# 2.按照value的属性值选择下拉项
# s= Select(el1)  # 实例化一个select对象
# s.select_by_value('grape')  # 按照value的属性值选择下拉项

# 3.按照文本内容选择下拉项
s= Select(el1)  # 创建一个select对象
s.select_by_visible_text('🍎 苹果')  # 按照文本内容选择下拉项

# 二 、取消已选择的下拉框里的下拉项  （多选）

# 1.按索引值取消选择
el2=driver.find_element(By.ID,'multiSelect') # 获取元素对象
s= Select(el2) # 实例化一个select对象
# s.select_by_index(3) # 按索引值选择
# time.sleep(2)
# s.deselect_by_index(3) # 按索引值取消选择

# 2.按value属性值取消选择
# s.select_by_value('python')  # 按value属性值选择
# time.sleep(2)
# s.deselect_by_value('python')  # 按value属性值取消选择

# 3.按文本内容取消选择
# s.select_by_visible_text('🐍 Python')
# time.sleep(2)
# s.deselect_by_visible_text('🐍 Python') 

# 4.取消所有已选择的下拉项
# s.select_by_index(1)
# time.sleep(1)
# s.select_by_value('java')
# time.sleep(1)
# s.select_by_visible_text('⚙️ C++')
# time.sleep(2)
# s.deselect_all()

# 三、获取所有下拉项的值
a=s.options # 获取所有下拉项的值

s.select_by_index(1)
s.select_by_value('java')
b=s.all_selected_options[-1]  # 获取所有已选择的下拉项的值
print(b.text)

c=s.first_selected_option # 获取第一个已选择的下拉项的值

d=s.all_selected_options[-1]  # 获取所有已选择的最后一个下拉项的值
print('最后一个下拉项',d.text)





