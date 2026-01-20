"""
pytest-html生成简介的测试报告

1. 安装pytest-html模块
pip install pytest-html==2.1.1

2. 运行测试用例
pytest --html=report/auto_reports.html --self-contained-html test_demo25.py
--self-contained-html 生成单文件报告
--html=report/auto_reports.html 生成报告文件的路径和文件名

生成测试报告的方式：
1. 命令行运行
pytest --html=report/auto_reports.html --self-contained-html test_demo25.py

2. 新建配置文件pytest.ini 在ini配置文件中添加如下内容：
[pytest]
addopts = --html=report.html --self-contained-html
然后运行 pytest

实例参考 test_demo4文件夹下的  test_demo25.py


3.自定义报告展示
修改报告标题：可以在conftest.py文件里使用钩子函数 pytest_html_report_title 来实现测试报告标题的修改
在conftest.py 文件中添加如下代码
def pytest_html_report_title(report):
    report.title = "测试报告"

添加 完成后再次执行并生成测试报告，可以看出标题已经修改为 "测试报告"

修改环境信息:环境信息是由pytest-metadata 插件提供的，该插件在安装pytest-html模块时默认安装，
并且可以通过访问pytest_configuer和pytest_sessionfinish钩子函数来修改环境信息



要在运行测试之前添加环境信息，使用 pytest_configure 钩子函数
def pytest_configure(config):
    config._metadata['Project Name'] = '测试项目'
    config._metadata['Module Name'] = '测试模块'
    config._metadata['QA'] = '测试人员'
    
实际测试后，并未添加成功 ，暂时未找到原因
降低pytest-html版本后修改成功（并不是添加），但是修改的标题或者环境信息中有中文的话会乱码
    

    


要在运行测试之后添加环境信息，使用 pytest_sessionfinish 钩子函数
import pytest
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata['测试时间'] = '2026-01-16 10:00:00'





"""
# 在D:\python_learn\7-pytest单元测试框架模块\test_demo4 路径下执行 pytest .\test_demo25.py  --html=./report.html --self-contained-html -v 命令
# 会在当前目录生成一个 report.html 文件，可以用浏览器打开查看测试报告   但是测试报告只显示结果，没有详细信息

# 如果是在项目根目录（D:\python_learn>）下执行命令
# pytest D:\python_learn\7-pytest单元测试框架模块\test_demo4\test_demo25.py  --html=./report.html --self-contained-html -v
# 生成的html文件会保存在根目录下，打开之后可以看到详细信息  不太理解