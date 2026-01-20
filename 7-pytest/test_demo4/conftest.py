
# import platform
# import pytest
# from pytest_metadata.plugin import metadata_key  # 引入 metadata_key
# from datetime import datetime
# from py.xml import html
# from  selenium import webdriver
# # 自定义测试报告标题
# def pytest_html_report_title(report):
#     report.title = "自定义测试报告标题"

# # 用例运行前,自定义环境信息
# def pytest_metadata(metadata,config):
#     """直接通过 metadata 字典添加环境信息"""
#     metadata.update({ 
#         "测试项目": "zzy_exercise",
#         "测试环境": "STAGING",
#         "执行节点": "Jenkins Slave-02",
#         "操作系统": platform.platform(),
#         "执行时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "测试人员": "张三"
# })
# # 用例运行后，自定义环境信息 

# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config.stash[metadata_key]["测试结果"] = "OJBK"

# # 自定义修改摘要信息（summary部分）
# def pytest_html_results_summary(prefix,summary, postfix):
#     """prefix 参数是一个列表，用于存储摘要信息"""
#     prefix.extend(["测试项目：lfy_exercise"])

# # 自定义修改测试结果详情（results部分）
# # 可以通过为标题和行实施自定义挂钩来修改报告的列。
# # 以下为对表中中的标题进行修改
# def pytest_html_results_table_header(cells):  # 通过cells.insert() 参数添加列  1就是列的索引  从0开始
#     cells.insert(1, html.th('用例描述'))  # 在第2列增加一个叫 ’用例描述’的列  thh' 标签表示标题
#     cells.insert(2, html.th('用例作者'))
#     cells.pop(-1) # 删除最后一列 

# # 以下为对表格中的内容进行修改
# def pytest_html_results_table_row(report, cells): # 
#     if hasattr(report, 'description') and hasattr(report, "zuozhe"):
#         cells.insert(1, html.td(report.description)) # 在第2列增加一个用例描述的内容  td 标签表示内容
#         cells.insert(2, html.td(report.zuozhe))
#         cells.pop(-1)

# # 使上面的修改生效
# # @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# # def pytest_runtest_makereport(item, call):  # item 是测试用例，call 是测试结果
# #     """通过 yield 获取钩子函数的返回值"""
# #     outcome = yield  # 获取钩子函数的返回值
# #     report = outcome.get_result() # 获取测试结果
# #     report.description = str(item.function.__doc__) # 修改描述信息
# #     report.zuozhe = 'author'
# driver = webdriver.Chrome(excutable_path=r"D:\software\Chrome\Application\chromedriver.exe")
# def _captuyre_screenshot(name):
#     """浏览器截图功能"""
#     driver.get_screenshot_as_base64()  # 实现浏览器截图  需要导入 driver对象
#     return driver.get_screenshot_as_base64()
# # 自定义添加测试截图
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield # 获取钩子函数的返回值 固定写法，上面是执行用例之前的钩子函数，下面是执行用例之后
#     report = outcome.get_result() # 获取测试报告对象
#     extras = getattr(report, "extras", [])  # 获取测试报告对象中的extras属性  下面的代码是对报告内容的修改 
#     """"when=setup时，获取的是前置的结果，when=call时，获取的是用例执行的结果，when=teardown时，获取的是后置的结果"""
#     if report.when == "call" or report.when == "setup":
#         # 失败后添加截图，生成下面的链接 ，可通过链接访问图片
#         # extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail") # 判断用例是否被标记为 xfail
#         if (report.skipped and xfail) or (report.failed and not xfail): # 判断用例的执行状态
#             """自定义增加失败截图"""
#             file_name= item.nodeid.replace("::", "_") + ".png"
#             """截图"""
#             screen_pic=_captuyre_screenshot()  # 自定义截图功能  需要在外部实现
#             """测试报告 增加失败截图"""
#             if file_name:  # 判断截图文件名是否为空
#                 """测试报告 添加截图"""
#                 html = '<div><img src="data:image/png;base64,{}" alt="screenshot"style="width:600px;height:300px;" ''οnclick="window.open(this.src)" align="right"/></div>'.format(screen_pic)
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra


import platform
import pytest
from datetime import datetime
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytest_metadata.plugin import metadata_key


# ================= 浏览器 fixture =================
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)

    service = Service(r"D:\software\Chrome\Application\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


# ================= HTML 报告配置 =================
def pytest_html_report_title(report):
    report.title = "自动化测试报告（Selenium + Pytest）"


def pytest_metadata(metadata, config):
    metadata.clear()
    metadata.update({
        "测试项目": "zzy_exercise",
        "测试环境": "STAGING",
        "执行节点": "Jenkins Slave-02",
        "操作系统": platform.platform(),
        "执行时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "测试人员": "张三"
    })


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["测试结果"] = "OJBK"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["测试项目：zzy_exercise"])


# ================= 表格列定制 =================
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("用例描述"))
    cells.insert(2, html.th("用例作者"))
    cells.pop(-1)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(getattr(report, "description", "")))
    cells.insert(2, html.td(getattr(report, "author", "")))
    cells.pop(-1)


# ================= 失败截图 =================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    report.description = str(item.function.__doc__)
    report.author = "author"

    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_base64()
            html_content = f"""
            <div>
                <img src="data:image/png;base64,{screenshot}"
                     style="width:600px;height:300px;"
                     onclick="window.open(this.src)"
                     align="right"/>
            </div>
            """
            extras.append(pytest_html.extras.html(html_content))

    report.extras = extras





