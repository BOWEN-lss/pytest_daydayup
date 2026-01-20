# scope 参数使用
import pytest
userinfo = [('张三', '123'),('李四', '456')]  # 定义数据驱动
class TestCase():
    @pytest.mark.parametrize('inderict_fixture3',userinfo,indirect = True,scope='class')
    def test_case01(self,inderict_fixture3):
        print("这是第一个测试方法")
    @pytest.mark.parametrize('inderict_fixture3',userinfo,indirect = True,scope='class')
    def test_case02(self,inderict_fixture3):
        print("这是第二个测试方法")

# 运行结果如下：
# test_demo13.py::TestCase::test_case01[inderict_fixture30] 传入的元组：('张三', '123')
# 这是第一个测试方法
# PASSED
# test_demo13.py::TestCase::test_case02[inderict_fixture30] 这是第二个测试方法
# PASSED
# test_demo13.py::TestCase::test_case01[inderict_fixture31] 传入的元组：('李四', '456')
# 这是第一个测试方法
# PASSED
# test_demo13.py::TestCase::test_case02[inderict_fixture31] 这是第二个测试方法
# PASSED
# 运行结果说明：
# 测试方法test_case01和test_case02，两个方法都使用了同一个参数，参数的值为userinfo列表中的元组，
# 实际执行模式是：每个参数值 × 每个测试方法 = 2 × 2 = 4 个测试用例
