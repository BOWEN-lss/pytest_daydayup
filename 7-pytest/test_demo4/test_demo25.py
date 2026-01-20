# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service  # 导入 Chrome 服务类，用于管理 ChromeDriver
# from selenium.webdriver.chrome.options import Options  # 导入 Chrome 选项类，用于配置浏览器选项
# from selenium.webdriver.common.by import By     # 导入定位元素的 By 类，用于定位页面元素
# import time  # 导入 time 模块
# # from conftest import driver

# @pytest.fixture(scope="session")  # 定义 session 级别的 fixture
# def driver():
#     options = Options()       # 创建 Chrome 选项对象
#     options.add_experimental_option("detach", True) # 设置浏览器不自动关闭

#     service = Service(r"D:\software\Chrome\Application\chromedriver.exe")  # 创建 ChromeDriver 服务对象，指定 ChromeDriver 的路径
#     driver = webdriver.Chrome(service=service, options=options)       # 创建 Chrome 浏览器实例，传入服务和选项参数
#     driver.maximize_window()  # 最大化浏览器窗口
#     yield driver      # 暂停并返回 driver 实例，供测试函数使用
#     # driver.quit()  # 添加清理

# class TestBing01:

#     def test_bing01(self, driver):      # 定义测试方法，用于测试搜索 python
#         """注释1"""
#         driver.get("https://cn.bing.com/")          # 打开必应搜索页面
#         search_box = driver.find_element(By.ID, "sb_form_q")          # 定位搜索框元素，通过 ID "sb_form_q"
#         search_box.click()  # 点击搜索框
#         search_box.send_keys("python")  # 输入搜索内容 "python"
#         driver.find_element(By.ID, "search_icon").click()  # 点击搜索按钮

#     def test_bing02(self, driver):
#         """注释2"""
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("Java")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing03(self, driver):
#         """注释3"""
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("Google")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing04(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("suibian")
#         driver.find_element(By.ID, "search_icon").click()

#     def test_bing05(self, driver):
#         driver.get("https://cn.bing.com/")
#         search_box = driver.find_element(By.ID, "sb_form_q")
#         search_box.click()
#         search_box.send_keys("aishasha")
#         driver.find_element(By.ID, "search_icon").click()

# # 在D:\python_learn\7-pytest单元测试框架模块\test_demo4 路径下执行 pytest .\test_demo25.py  --html=./report.html --self-contained-html -v 命令
# # 会在当前目录生成一个 report.html 文件，可以用浏览器打开查看测试报告   但是测试报告只显示结果，没有详细信息

# # 如果是在项目根目录（D:\python_learn>）下执行命令
# # pytest D:\python_learn\7-pytest单元测试框架模块\test_demo4\test_demo25.py  --html=./report.html --self-contained-html -v
# # 生成的html文件会保存在根目录下，打开之后可以看到详细信息  不太理解

# # 原因：路径设计的层数太深，实际上是没有问题的



import pytest
from selenium.webdriver.common.by import By


class TestBingSearch:

    def test_bing_01(self, driver):
        """搜索 Python"""
        driver.get("https://cn.bing.com/")
        driver.find_element(By.ID, "sb_form_q").send_keys("Python")
        driver.find_element(By.ID, "search_icon").click()
        assert "Python" in driver.title

    def test_bing_02(self, driver):
        """搜索 Java"""
        driver.get("https://cn.bing.com/")
        driver.find_element(By.ID, "sb_form_q").send_keys("Java")
        driver.find_element(By.ID, "search_icon").click()
        assert "Java" in driver.title

    def test_bing_03(self, driver):
        """搜索 Google（故意失败，测试截图）"""
        driver.get("https://cn.bing.com/")
        driver.find_element(By.ID, "sb_form_q").send_keys("Google")
        driver.find_element(By.ID, "search_icon").click()
        assert "不存在的标题" in driver.title
