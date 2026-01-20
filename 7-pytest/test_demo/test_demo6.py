# 在类的内部执行的前置和后置：
# setup_class/teardown_class  (针对某个类内的前置/后置) 仅在类内部时才会被执行。整个类只执行一次
# setup_class 类内部执行前执行   teardown_class 类内部执行后执行

# setup_method/teardown_method  (针对某个方法内的前置/后置) 仅在类内部方法时才会被执行。每个方法（函数）只执行一次

import pytest

class TestCase:
    @classmethod
    def setup_class(cls):
        print('setup_class 类内部执行前执行，整个测试类只执行一次')
    @classmethod
    def teardown_class(cls):
        print('teardown_class 类内部执行后执行，整个测试类只执行一次')

    def setup_method(self):
        print('setup_method：每个测试方法(用例)前执行')

    def teardown_method(self):
        print('teardown_method 每个测试方法（用例）后执行')

    def test_case01(slef):
        num = 1 + 1
        assert num == 2
        print('test_case01 执行')


    def test_case02(slef):
        num = 1 + 2
        assert num == 3
        print('test_case02 执行')
