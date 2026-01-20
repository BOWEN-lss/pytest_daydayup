"""
alluer-pytest生成精美的测试报告

1. 安装 allure-pytest 插件
pip install allure-pytest

安装 aluuer-commandline命令工具
在 https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/ 中下载最新版本 allure-commandline 的zip包
解压并放置到任意目录下，把该目录下的bin 目录加入到系统环境变量 PATH 中   E:\python\allure-2.36.0\allure-2.36.0\bin

2. 运行测试用例
pytest test_demo.py --alluredir ./result

3. 生成测试报告
allure generate ./report/result -o ./report/html --clean

4. 运行测试报告
allure open ./report/html

实例参考 test_demo_allure测试报告文件夹下的 test_demo_allure.py
"""