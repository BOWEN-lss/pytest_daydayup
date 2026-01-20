# pytest-xdist分布式执行用例  一般用于案例数量较大时 
# 使用 pytest -n 3 test_demo23.py -v -s 指定核心线程数量    n 表示同时执行的线程数量，一般为CPU核心数量的一半，防止电脑卡顿
# 也可以使用 pytest -n auto test_demo23.py -v -s  自动获取CPU核心数量且自动分配合适的线程数

# 当py文件中有多个测试类时，可以用 pytest -n 2 --dist=loadscope test_demo23.py -v -s 命令分别执行多个测试类
# 当一个项目下有多个测试文件时，可以使用 pytest -n 3 --dist=loadfile test_demo23.py test_demo24.py test_demo25.py -v -s
# 来同时运行多个测试文件

# 将每个用例，分别给所有的worker，相当于开了几个线程，同一个用例就执行多少遍
# pytest -n 3 --dist=each  test_demo23.py  -v -s

# 默认使用的模式为随机，将待运行的用例随机发给可用的worker，用例执行顺序为随机
# pytest -n 3 --dist=load test_demo23.py -v -s
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # 导入 Chrome 服务类，用于管理 ChromeDriver
from selenium.webdriver.chrome.options import Options  # 导入 Chrome 选项类，用于配置浏览器选项
from selenium.webdriver.common.by import By     # 导入定位元素的 By 类，用于定位页面元素
import time  # 导入 time 模块

@pytest.fixture(scope="session")  # 定义 session 级别的 fixture
def driver():
    options = Options()       # 创建 Chrome 选项对象
    options.add_experimental_option("detach", True) # 设置浏览器不自动关闭

    service = Service(r"D:\software\Chrome\Application\chromedriver.exe")  # 创建 ChromeDriver 服务对象，指定 ChromeDriver 的路径
    driver = webdriver.Chrome(service=service, options=options)       # 创建 Chrome 浏览器实例，传入服务和选项参数
    driver.maximize_window()  # 最大化浏览器窗口
    yield driver      # 暂停并返回 driver 实例，供测试函数使用
    # driver.quit()  # 添加清理

class TestBing01:
    def test_bing01(self, driver):      # 定义测试方法，用于测试搜索 python
        driver.get("https://cn.bing.com/")          # 打开必应搜索页面
        search_box = driver.find_element(By.ID, "sb_form_q")          # 定位搜索框元素，通过 ID "sb_form_q"
        search_box.click()  # 点击搜索框
        search_box.send_keys("python")  # 输入搜索内容 "python"
        driver.find_element(By.ID, "search_icon").click()  # 点击搜索按钮

    def test_bing02(self, driver):
        driver.get("https://cn.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.click()
        search_box.send_keys("Java")
        driver.find_element(By.ID, "search_icon").click()

    def test_bing03(self, driver):
        driver.get("https://cn.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.click()
        search_box.send_keys("Google")
        driver.find_element(By.ID, "search_icon").click()

    def test_bing04(self, driver):
        driver.get("https://cn.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.click()
        search_box.send_keys("suibian")
        driver.find_element(By.ID, "search_icon").click()

    def test_bing05(self, driver):
        driver.get("https://cn.bing.com/")
        search_box = driver.find_element(By.ID, "sb_form_q")
        search_box.click()
        search_box.send_keys("aishasha")
        driver.find_element(By.ID, "search_icon").click()


# class TestBing02:
#     def test_bing06(self, driver):     
#         driver.get("https://cn.bing.com/")       
#         search_box = driver.find_element(By.ID, "sb_form_q")         
#         search_box.click() 
#         search_box.send_keys("iosofoi") 
#         driver.find_element(By.ID, "search_icon").click() 

#     def test_bing07(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("dsfd")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing08(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("wieuro")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing09(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("xcnvdc")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing10(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("weir")
#         driver.find_element(By.ID, "search_icon").click()