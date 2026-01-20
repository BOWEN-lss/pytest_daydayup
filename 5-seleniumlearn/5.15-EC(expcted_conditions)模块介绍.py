"""
seleniumlearn.EC(expcted_conditions)模块介绍 

expected_conditions(简称 EC)是 Selenium WebDriver 中的一个重要模块，提供了预定义的条件判断函数，主要用于配合 WebDriverWait 实现显式等待。

 主要作用
 **显式等待**:等待特定条件满足后再继续执行测试
 **提高稳定性**:避免因页面加载延迟导致的测试失败
 **精确控制**:可以等待各种具体条件，如元素可见、可点击等

 常用的 Expected Conditions

# 元素相关条件
 presence_of_element_located:等待元素出现在DOM中
 visibility_of_element_located:等待元素可见
 element_to_be_clickable:等待元素可点击
 text_to_be_present_in_element:等待元素包含特定文本

# 页面相关条件
 title_is:等待页面标题完全匹配
 title_contains:等待页面标题包含指定文本
 url_to_be:等待URL完全匹配
 url_contains:等待URL包含指定内容

 使用示例
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 等待元素可见
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "myElement")))

# 等待页面标题包含特定文本
wait.until(EC.title_contains("登录"))

 优势
相比隐式等待和强制等待,EC 模块提供了更加灵活和可靠的等待机制，能够显著提升自动化测试的稳定性和执行效率。
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
# driver.get('http://www.baidu.com') # 从网页的head里面招到title  此处为‘百度一下，你就知道’
from selenium.webdriver.support import expected_conditions as EC  # 导入expected_conditions模块
# EC判定方法：
# 1.判断页面的title是否完全等于（==）预期字符串，返回结果为布尔值
# title_is = EC.title_is("百度一下，你就知道")
# print(title_is(driver))  # 与预期字符串完全一致，返回为True
# # 2.判断title是否包含预期字符串，返回结果为布尔值
# title_contains = EC.title_contains("知道")
# print(title_contains(driver)) # 预期字符串包含在title中，返回为True
"""
# 判断元素是否可见 
driver.get('http://sahitest.com/demo/visible.htm')
el1=driver.find_element(By.ID,'uv')  # 定位元素
locate = (By.ID,'uv')  
res1=EC.visibility_of_element_located(locate)  # 创建判定方法判断元素是否可见
print(res1(driver))   # 当前结果为可见，输出结果为元素值

el2=driver.find_element(By.XPATH,".//input[@value='Visibility hidden']")  # 定位隐藏按钮
el2.click() # 点击隐藏按钮，使上一个可见的元素el1隐藏，变为不可见

print(res1(driver))   # 当前结果为不可见，输出结果为false

dom树的理解 :DOM树是网页的"结构图"
当你打开一个网页时，浏览器会做两件事：
构建DOM树:解析HTML代码,建立网页的"结构图"
渲染页面：根据这个"结构图"显示内容

# 判断元素是否在dom树里 
RES2 = EC.presence_of_element_located(locate) # 创建判定方法判断元素是否在dom树里
print(RES2(driver))  # 当前元素不可见，但是还是在dom树里，输出结果为元素值

"""

# 判断弹窗是否出现
driver.get('http://sahitest.com/demo/alertTest.htm')  # 打开测试网页
el4=driver.find_element(By.XPATH,".//input[@value='Click For Multiline Alert']") # 定位弹窗按钮
el4.click() # 点击弹窗按钮

res3=EC.alert_is_present() # 创建判定方法判断弹窗是否出现
print(res3(driver)) # 弹窗出现，输出结果为弹窗对象
time.sleep(1.5)
driver.switch_to.alert.accept() # 点击确定，关闭弹窗