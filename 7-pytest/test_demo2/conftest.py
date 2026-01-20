def pytest_configure(config):
    config.addinivalue_line('markers', 'success: 自定义标签，用于标记成功的用例')
    config.addinivalue_line('markers', 'faild: 自定义标签，用于标记失败的用例')
    config.addinivalue_line('markers', 'smoke: 自定义标签，用于标记冒烟测试的用例')
    config.addinivalue_line('markers', 'Login: 自定义标签，用于标记登录模块的用例')
    config.addinivalue_line('markers', 'Logout: 自定义标签，用于标记退出模块的用例')