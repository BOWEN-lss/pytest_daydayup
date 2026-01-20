"""
xpath 定位方法：
1.xpath 结合基本属性定位元素
2.xpath结合文本定位
3.xpath层级定位
4.xpath索引定位
5.xpath模糊匹配定位
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
time.sleep(2)   # 等待两秒
driver.maximize_window()       # 最大化浏览器窗口
driver.get('https://www.baidu.com')  # 打开百度首页
# option.add_argument('--headless')  # 无头模式，不显示浏览器界面，提高速度
# 1.xpath 结合基本属性定位元素  .//表示当前节点下的所有子节点  []表示要根据属性找元素  @后面跟属性的值，表示要通过哪个属性定位 
# el1= driver.find_element(By.XPATH,".//li[@class='hotsearch-item even']")  # 通过xpath结合属性定位元素
# print('el1:',el1.text)

# el11= driver.find_element(By.XPATH,".//li[@class='hotsearch-item even' and @data-index= '6']")  # 多属性定位时，多个属性之间用and连接
# print('el11:',el11.text) 
#   通过文本内容定位  在网页中><中间的为文本值，这样的文本值可用文本定位
# el2 = driver.find_element(By.XPATH, "//a[text()='更多']")
# print('el2:',el2.text)
 
# 定位第一个热搜项
# el3 = driver.find_element(By.XPATH, "//li[1]//span[@class='title-content-title']")
# print(el3.text)

# # 通过层级关系定位
# el4 = driver.find_element(By.XPATH, "//div[@class='chat-input-container']/div/textarea")    # 从上到下定位
# print('el4',el4.text) 
# el5 =  driver.find_element(By.XPATH,"//div[@id= 'input-root']/parent::div")   # 从下到上定位
# print('el5:',el5.text)
# el6 = driver.find_element(By.XPATH, "//input[@class='s_ipt']/preceding-sibling::span")   # 从当前节点向前找兄弟节点
# print('el6:',el6.text)

# el7 = driver.find_element(By.XPATH, "//input[@class='s_ipt']/following-sibling::span")   # 从当前节点向后找兄弟节点
# print('el7:',el7.text)

# 索引定位
# el8 = driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[1]")   # 索引定位第一个a标签   索引从1开始
# print('el8:',el8.text)

# el9 = driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[last()]")   # 索引定位最后一个a标签   last()表示索引最后一个元素
# print('el9:',el9.text)

# el10 = driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[last()-1]")   # 索引定位倒数第二个a标签   last()-1表示索引倒数第二个元素
# print('el10:',el10.text)

# 模糊匹配定位
el11 = driver.find_element(By.XPATH, "//div[contains(@aria-label,'热')]")   # 包含匹配
print('el11:',el11.text)

el12 = driver.find_element(By.XPATH, "//div[starts-with(@aria-label,'百度')]")   # 前缀匹配
print('el12:',el12.text)

# el13 = driver.find_element(By.XPATH, "//div[ends-with(@aria-label,'热搜')]")   # 后缀匹配
# print('el13:',el13.text)   # 不支持XPath 2.0的ends-with()函数  所以这里执行会报错

# el14 = driver.find_element(By.XPATH, "//div[matches(@aria-label,'百度一下')]")   # 正则匹配
# print('el14:',el14.text)   # 不支持XPath 2.0的matches函数  所以这里执行会报错
