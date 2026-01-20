"""
pytest中用mark模块标记用例标签
一、使用@pytest.mark 进行自定义标签
语法：@pytest.mark.标签名
可以标记测试方法，测试类，标记名可以自定义，最好是有意义的名字   同一个测试方法，测试类可同时拥有多个标记
运行语法：pytest -m 标签名 py文件名

案例参考 test_demo2文件夹下的  test_demo18.py

二、组合运行用例
运行语法：pytest -m "标签名1 or/and/not 标签名2" py文件名 -v -s
三、注册、管理mark标记
方式一:在conftest.py文件中,通过hock注册
在conftest.py文件中添加以下内容
def pytest_configure(config):
    config.addinivalue_line('markers', 'success: 自定义标签，用于标记成功的用例')
    config.addinivalue_line('markers', 'failed: 自定义标签，用于标记失败的用例')
    config.addinivalue_line('markers', 'smoke: 自定义标签，用于标记冒烟测试的用例')
    config.addinivalue_line('markers', 'Login: 自定义标签，用于标记登录模块的用例')
    config.addinivalue_line('markers', 'Logout: 自定义标签，用于标记退出模块的用例')
方式二:在ini文件中注册
在ini文件中写入以以下内容
[pytest]
markers =
    success: 自定义标签，用于标记成功的用例
    failed: 自定义标签，用于标记失败的用例  # 修正拼写
    smoke: 冒烟测试
    Login: 登录模块
    Logout: 退出模块
保存并再次执行  pytest -m smoke test_demo18.py -v -s  命令   告警信息就会消失
"""  