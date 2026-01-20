# 在类中的前置和后置  课程中的方法已经 不适用，以下方为准
import pytest
class TestCase:
    @pytest.fixture
    def login(self):
        print('这是登录接口（fixture 前置）')
        yield
        print('这是退出接口（fixture 后置）')
    def test_case01(self,login):
        num = 1 + 1
        assert num == 2
        print('test_case01 执行')


    def test_case02(self,login):
        num = 1 + 2
        assert num == 3
        print('test_case02 执行')