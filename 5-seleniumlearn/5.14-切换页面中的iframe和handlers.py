"""
切换页面中的iframe和handlers
### 定义
iframe 是 HTML 中的一个元素，允许在一个网页中嵌入另一个独立的 HTML 文档。

### 用途
- 在当前页面中显示其他网站的内容
- 嵌入广告、视频播放器等第三方内容
- 创建页面内的独立滚动区域
- 避免页面跳转，在同一页面内加载不同内容

## Handlers（处理器）

在 Selenium 自动化测试的语境下：

### Window Handlers
- 用于标识和管理浏览器中不同的窗口或标签页
- 每个打开的浏览器窗口都有唯一的句柄（handle）
- 通过 handlers 可以在多个窗口之间进行切换

### Frame Handlers
- 用于管理和切换不同的 iframe
- Selenium 需要先切换到特定的 iframe 才能操作其中的元素

## 在自动化测试中的重要性

- iframe 操作：需要使用 `driver.switch_to.frame()` 来进入 iframe 上下文
- 窗口切换：需要使用 `driver.window_handles` 获取所有窗口句柄，然后用 `driver.switch_to.window()` 进行切换

这些概念在复杂的 Web 应用程序测试中非常重要，因为现代网站经常使用 iframe 和多窗口来组织内容。
"""

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

driver.get('http://sahitest.com/demo/iframesTest.htm')  # 打开测试网站
 
# 一、切换 iframe：
# 1. 通过 id
driver.switch_to.frame('frame1')  # 如果iframe标签中有id属性，可以通过id属性的值进行切换 此示例网址不适用id切换

# 2. 通过出入元素对象切换
el2 = driver.find_element(By.XPATH, './/a[text()="Link Test"]')
print(el2)   # 直接定位这个元素会报错，因为此元素在iframe中，所以需要先切换 iframe 才能定位
driver.switch_to.frame(el1)

# 正确定位方法：
el1 = driver.find_element(By.XPATH, '//iframe[@src="index.htm"]')  # 先定位到iframe标签，用 标签后面的属性进行定位 
driver.switch_to.frame(el1) # 切换进 iframe
# 再 定位 iframe 中的元素
el2 = driver.find_element(By.XPATH, './/a[text()="Link Test"]')
el2.click()

# 二、切出iframe 如果 此时元素在 iframe 中，我们需要点击iframe外面的元素，那么就需要先切出 iframe，否则无法点击
driver.switch_to.parent_frame()   # 切到 iframe 父级（上一层）
driver.switch_to.default_content()  # 切回默认的页面(最外层)
el3=driver.find_element(By.XPATH,".//input[@value='Click me']")  # 此时我们已经进入到iframe中，定位的是iframe外面的元素
el3.click()



# # 三、窗口切换 （handler）
# driver.get('http://www.baidu.com')
# driver.execute_script("window.open('http://www.bing.com','_blank');")  # 在第二个标签页中打开百度 
# # 1.获取当前所有窗体
# handles = driver.window_handles
# print(handles)  # 以列表形式输出所有窗体的句柄（每个窗口/标签页都有唯一的句柄值，因此可认为一个句柄代表一个标签页/窗口）

# # 2.切换到其他标签页
# driver.switch_to.window(handles[0])  # 切换到第一个标签页(从0开始)

# # 3.获取当前窗体的句柄
# handle = driver.current_window_handle
# print(handle)
