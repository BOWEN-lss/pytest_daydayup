# 只能在类的外部使用的前置后置函数
import pytest
def setup_module(module):   # 模块级别 ,每个py文件中只执行一次
    print('setup_module 执行完毕')

def teardown_module(module):  # 模块级别,每个py文件中只执行一次
    print('teardown_module 执行完毕')

def setup_function(function):  # 函数级别，每个用例中都执行一次
    print('setup_function 执行完毕')

def teardown_function(function):  # 函数级别，每个用例中都执行一次
    print('teardown_function 执行完毕')
def test_case01():
    num = 1 + 1
    assert num == 2
    print('test_case01 执行')


def test_case02():
    num = 1 + 2
    assert num == 3
    print('test_case02 执行')