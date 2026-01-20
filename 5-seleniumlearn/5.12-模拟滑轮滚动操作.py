# 模拟滑轮滚动操作
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
driver.get('https://aiso.jikeyunsou.com/')
time.sleep(2)
# 滑动至页面底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(2)

# 滑动到页面顶部
# driver.execute_script("window.scrollTo(0, 0)")
# time.sleep(2)

# 滑动到页面的某个具体位置
# driver.execute_script("window.scrollTo(0, 1000)") # 向下滑动1000个像素
# time.sleep(10)
# driver.execute_script("window.scrollTo(0, -1000)") # 向上滑动1000个像素
# time.sleep(10)
# driver.execute_script("window.scrollTo(1000, 0)")  # 向右滑动1000个像素
# time.sleep(10)
# driver.execute_script("window.scrollTo(-1000, 0)") # 向左滑动1000个像素

# 滑动到某个元素出现的位置

el1= driver.find_element(By.XPATH,".//a[contains(@title,'无损音质')]")

driver.execute_script("arguments[0].scrollIntoView();", el1)  # 向下滑动到元素  ‘酷我音乐’出现的位置

time.sleep(2)


# 向上滚动至指定元素可见
el2= driver.find_element(By.XPATH,".//a[contains(@title,'Devv')]")

driver.execute_script("arguments[0].scrollIntoView(false);", el2) # 向上滑动到元素  ‘Devv’出现的位置
