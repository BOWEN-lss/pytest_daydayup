# 163邮箱自动化登录实现

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
driver.get('https://mail.163.com/')

# 输入用户名

el1= driver.find_element(By.XPATH,".//div[@id='loginDiv']/iframe")
driver.switch_to.frame(el1)
el2= driver.find_element(By.XPATH,".//div[@id='account-box']/div[2]/input[@name='email']")
el2.send_keys("lfy827241")

    # 此处执行或报错为’nosuchelementexception‘ 没有这个元素 ，排查没有这个元素的原因可以从一下三个方面考虑
    # 1.元素未加载出来  解决方法为设置等待时间  time.sleep(2.5)
    # 2.未切进/切出iframe  解决方法为：driver.switch_to.frame('x-URS-iframe1765771239539.3657')
    # 3.元素为动态生成的，每次刷新都会变。 解决方法为：使用更通用的定位方式来找到iframe元素，如找到iframe上一层，利用层级关系
# 输入密码
el3= driver.find_element(By.XPATH,".//div[@class='inputbox']/div[2]/input[@name='password']")
el3.send_keys("lfy123++")

time.sleep(1)
# 点击登录按钮
el4=driver.find_element(By.XPATH,".//div[@class='j-power-btn f-cb loginbox']/a[@id='dologin']")
el4.click()
# time.sleep(1)
#     # 首次登录需要点击本人验证
# el5=driver.find_element(By.XPATH,".//p[@class='m-ismyphone-p1']/input[@id='ismyphonebox']")
# el5.click()
#     # 点击确定
# time.sleep(1)
# el6=driver.find_element(By.XPATH,".//div[@class='btnbox']/a[1]")
# el6.click()