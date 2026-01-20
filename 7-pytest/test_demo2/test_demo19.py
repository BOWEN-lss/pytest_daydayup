# pytest-ordering调整用例执行顺序  需要注意的是要想让py文件中的所有用例排好序，那么就必须给所有用例
# 都加上@pytest.mark.run(order=数字)，否则排序不生效

import pytest
@pytest.mark.run(order=2)
def test_case1():
    print("用例1执行完了")

class TestDemo:
    @pytest.mark.run(order=3)
    def test_case2(self):
        print("用例2执行完了")
    @pytest.mark.run(order=1)
    def test_case3(self):
        print("用例3执行完了")

# 执行结果为
# test_demo19.py::TestDemo::test_case3 用例3执行完了
# PASSED
# test_demo19.py::test_case1 用例1执行完了
# PASSED
# test_demo19.py::TestDemo::test_case2 用例2执行完了
# PASSED
# 符合排序顺序

# 如果把排序装饰器放到类上面，那么类中的所有测试用例都会按照顺序执行