"""
元素的id属性定位
"""
# # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# from playwright.sync_api import sync_playwright
# # 导入 time 模块，用于添加延时等功能
# import time

# # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
# with sync_playwright() as playwright:
#     # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     browser = playwright.chromium.launch(headless=False)
#     # 创建一个新的浏览器页面标签页
#     page = browser.new_page()
#     # 导航到百度首页 URL
#     page.goto('https://www.baidu.com')
#     # 设置浏览器窗口视口大小为 1920x1080 分辨率
#     page.set_viewport_size({'width':1920,'height':1080})

#     # 使用 CSS 选择器定位 ID 为 'chat-input-main' 的元素
#     element = page.locator('#chat-input-main')
#     # 打印找到的元素对象信息
#     print(f'元素标签：{element}')

#     # 等待用户输入任意键后继续执行，防止程序立即结束
#     input('按任意键结束')

"""
元素的name属性定位
"""

# from playwright.sync_api import sync_playwright  # 导入导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time   # 导入 time 模块，用于添加延时等功能
# with sync_playwright() as pl:   # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
#     browser = pl.chromium.launch(headless = False)   # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     page = browser.new_page()   # 创建一个新的浏览器页面标签页
#     page.goto('https://www.bing.com')   # 导航到bing首页 URL
#     page.set_viewport_size({'width':1920,'height':1080})    # 设置浏览器窗口视口大小为 1920x1080 分辨率
#     element = page.locator("[name='q']")   # 使用 CSS 选择器定位 name 为 'q' 的元素  注意这里的引号区分单双引号
#     print(f'元素标签：{element}')   # 打印找到的元素对象信息
#     input('按任意键结束')  # 等待用户输入任意键后继续执行，防止程序立即结束


"""
元素的class属性定位
"""

# from playwright.sync_api import sync_playwright  # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time  # 导入 time 模块，用于添加延时等功能

# with sync_playwright() as pl2:   # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
#     browser = pl2.chromium.launch(headless=False)  # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     page = browser.new_page() # 创建一个新的浏览器页面标签页
#     page.goto('https://www.bing.com') # 导航到bing首页
#     page.set_viewport_size({'width':1920,'height':1080})  # 设置浏览器窗口视口大小为 1920x1080 分辨率
#     elment = page.locator("[class = 'sb_form_c   ']")  # 使用 CSS 选择器定位 class 为 'sb_form_c   ' 的元素
#     print(f'元素标签：{elment}') # 打印找到的元素对象信息
#     input('按任意键结束') # 等待用户输入任意键后继续执行，防止程序立即结束


"""
元素的标签页属性定位
"""
# 标签唯一时
# from playwright.sync_api import sync_playwright # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time # 导入 time 模块，用于添加延时等功能
# with sync_playwright()as pl3:
#     browser = pl3.chromium.launch(headless = False)
#     page = browser.new_page()
#     page.goto('https://www.bing.com')
#     page.set_viewport_size({'width':1920,'height':1080})
#     element = page.locator("form")  # 当标签唯一时可以使用这种方式，当标签不唯一时，可以结合其他属性精确定位
#     print(f'元素标签：{element}')

# 标签不唯一时
# from playwright.sync_api import sync_playwright # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time # 导入 time 模块，用于添加延时等功能
# with sync_playwright()as pl3:  # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
#     browser = pl3.chromium.launch(headless = False) # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     page = browser.new_page() # 创建一个新的浏览器页面标签页
#     page.goto('https://www.bing.com') # 导航到bing首页
#     page.set_viewport_size({'width':1920,'height':1080}) # 设置浏览器窗口视口大小为 1920x1080 分辨率
#     element = page.locator("input[type = 'submit']")  # 当标签不唯一时，可以结合其他属性精确定位
#     print(f'元素标签：{element}')

# 标签不唯一时，可以获取所有匹配元素
# from playwright.sync_api import sync_playwright # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time # 导入 time 模块，用于添加延时等功能
# with sync_playwright()as pl3: # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
#     browser = pl3.chromium.launch(headless = False) # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     page = browser.new_page() # 创建一个新的浏览器页面标签页
#     page.goto('https://www.bing.com') # 导航到bing首页
#     page.set_viewport_size({'width':1920,'height':1080}) # 设置浏览器窗口视口大小为 1920x1080 分辨率
#     elements = page.locator("input").all()  # 获取所有input元素列表
#     print(f'元素标签：{elements}')
#     count = page.locator("input").count()   # 获取匹配元素的数量
#     print(f'元素数量：{count}')
    
#     first_input = page.locator("input").first  # 定位第一个input元素
#     print(f'第一个元素标签：{first_input}')
#     second_input = page.locator("input").nth(1)  # 定位第二个input元素
#     print(f'第二个元素标签：{second_input}')

"""
页面中的链接文本定位
"""
# from playwright.sync_api import sync_playwright   # 导入 playwright 库中的 sync_playwright 函数，用于同步方式操作浏览器
# import time # 导入 time 模块，用于添加延时等功能
# with sync_playwright() as pl4:   # 使用 with 语句创建 playwright 上下文管理器，确保资源正确释放
#     browser = pl4.chromium.launch(headless = False)   # 启动 Chromium 浏览器，设置 headless=False 使浏览器窗口可见
#     page = browser.new_page()   # 创建一个新的浏览器页面标签页
#     page.goto('https://www.bing.com')   # 导航到bing首页
#     page.set_viewport_size({'width':1920,'height':1080}) # 设置浏览器窗口视口大小为 1920x1080 分辨率
    # element = page.locator("a.href('/images?FORM=Z9LH')")  # 精确匹配链接的文本内容  推荐使用
    # print(f'元素标签：{element}')
    # element = page.locator("a >> text=图片") # 使用 text() 函数匹配链接文本
    # print(f'元素标签：{element}')
    # element = page.locator("a:href('Images')")  # 模糊匹配链接的文本内容(包含指定文本的链接)
    # print(f'元素标签：{element}')
    # element = page.locator("a:text('*=图片')")  # 模糊匹配链接的文本内容(使用 *= 操作符)
    # print(f'元素标签：{element}')
 

# from playwright.sync_api import sync_playwright 
# 启动playwright driver进程
# p = sync_playwright().start()
# browser = p.chromium.launch(headless = False)
# executable_path=r"D:\software\Google\Chrome\Application\chrome.exe"
# page = browser.new_page()
# page.goto('https://www.bing.com')   # 导航到bing首页
# page.set_viewport_size({'width':1920,'height':1080}) # 设置浏览器窗口视口大小为 1920x1080 分辨率

# print(page.title())  # 打印页面标题
# # 设置打开浏览器后等待5秒
# page.wait_for_timeout(5000)
# # 查询
# page.locator('#sb_form_q').fill('随便')
# page.wait_for_timeout(2000)
# page.locator("a[href*='images']").click()  # 点击图片   不会点击，暂时未找到原因

"""
页面中的CSS选择器定位
"""

# 1.CSS结合基本属性定位（如：id，class，name，tagName等）
# CSS选择器结合id属性定位元素  CSS语法中 # 代表id属性      . 代表class属性
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
time.sleep(2)   # 等待两秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get('https://www.baidu.com')  # 打开百度首页
# el1 = driver.find_element(By.CSS_SELECTOR, '#chat-textarea')   # 通过CSS选择器结合id属性定位元素
# print(el1)


# CSS选择器结合class属性定位元素
# el2 = driver.find_element(By.CSS_SELECTOR,'.chat-input-textarea.chat-input-scroll-style')
# print(el2)

# CSS选择器结合标签名属性定位元素
# el3 = driver.find_element(By.CSS_SELECTOR,'textarea')  # 通过CSS选择器结合标签名（尽可能找唯一的标签名）属性定位元素
# print('el3',el3)


# # CSS结合其他属性定位元素
# el4 = driver.find_element(By.CSS_SELECTOR,'[name="tj_briicon"]')
# print('el4',el4)


# CSS标签结合其他属性定位元素   

# el5=driver.find_element(By.CSS_SELECTOR,'form#form')   # 通过CSS标签结合id属性定位元素
# print('el5',el5)

# el6=driver.find_element(By.CSS_SELECTOR,'form.fm')   # 通过CSS标签结合class属性定位元素
# print('el6',el6) 

# el7=driver.find_element(By.CSS_SELECTOR,"form[name='f']") 
# print('el7',el7)

# CSS层级定位
el8=driver.find_element(By.CSS_SELECTOR,"a[id='result_logo']>img[class='index-logo-src']")  # 通过CSS层级定位元素
print('el8',el8)

# CSS索引定位   索引从1开始
el9=driver.find_element(By.CSS_SELECTOR,"a:nth-child(1)")  # 选择正数第一个元素
print('el9',el9)

el10=driver.find_element(By.CSS_SELECTOR,"div[id='s-top-left']>a:nth-last-child(4)")  # 选择倒数第四个元素
print(el10.text) # 获取元素文本

# CSS 模糊匹配
"""
在Playwright或Selenium等自动化测试框架中，使用CSS选择器进行模糊匹配适用于以下几种情况：
1. **动态内容定位**
   - 当页面元素的属性值部分固定、部分变化时（例如动态ID或class）
   - 示例：`[class*='button']` 可以匹配所有包含"button"字符串的class属性

2. **局部文本匹配**
   - 需要根据部分文本内容定位元素，而非精确匹配全部文本
   - 示例：`a:text('*=图片')` 可以匹配所有包含"图片"二字的链接文本

3. **不确定完整属性值**
   - 当无法预知元素属性的完整值，只知道其中一部分关键字时
   - 示例：`[href*='images']` 可以匹配所有href属性包含"images"子串的元素

4. **批量选择相似元素**
   - 需要选取具有相同特征前缀或后缀的一组元素
   - 示例：`[id^='user']` 匹配所有以"user"开头的ID元素

5. **避免频繁更新选择器**
   - 当前端组件库自动生成的类名有变动部分时，使用模糊匹配可提高稳定性
   - 示例：`[class*='ant-btn']` 可以适配Ant Design按钮组件的各种变体

模糊匹配能够增强选择器的灵活性和健壮性，在面对动态网页内容时特别有用。
"""

el11 = driver.find_element(By.CSS_SELECTOR, "a[class^='hot']") # 模糊匹配以"hot"开头的class属性的元素
print(el11.text) 


