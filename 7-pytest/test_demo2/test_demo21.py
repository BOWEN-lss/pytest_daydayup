# pytest-repeat重复运行用例
import pytest
def test_case0():
    print('用例0开始执行')
    


class TestDemo:
    def test_case1(self):
        print('用例1开始执行')

    def test_case2(self):
        print('用例2开始执行')
        assert 1==2   # 用例2断言失败
    @pytest.mark.repeat(3)  # 用装饰器方式重复执行用例3，执行3次
    def test_case3(self):
        print('用例3开始执行')

# 可以用命令行的方式执行 pytest --count=3 --repeat-scope=module test_demo21.py -s -v 让整个py文件下的用例重复执行3次
# 执行顺序依次为test_case00 -> test_case.1 -> test_case.2 -> test_case.3  重复3次

# pytest --count=3 --repeat-scope=class test_demo21.py -s -v
# 执行顺序为先执行3次class外面的test_case0，再执行class里面的test_case1，test_case2，test_case3，重复3次

# 也可以用装饰器的方式执行