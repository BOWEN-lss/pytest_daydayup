# pytest-rerunfailures失败用例重跑
import pytest
class TestDemo:
    @pytest.mark.flaky(reruns=3, reruns_delay=1)  # 用装饰器的方式添加重跑，效果跟下面的命令行一样
    def test_case1(self):
        print("用例1开始执行")
        assert False  # 断言失败

# 但是用装饰器的方式不可以与类，模块还有包级别的fixtrue装饰器一起使用  尽量避免使用，可以用命令行添加重跑




# 用 pytest --reruns 3 --reruns-delay 1 test_demo20.py -s -v 命令让这个failed用例重跑3次，每次间隔1秒
# 或者用 pytest --reruns 3 --reruns-delay 1 --only-rerun AssertionError  test_demo20.py -v -s 让脚本中指定错误类型的用例重跑3次，间隔1秒
# 如果想指定多个错误类型可以直接加在 --only-rerun AssertionError 后面，多个错误类型之间用空格隔开