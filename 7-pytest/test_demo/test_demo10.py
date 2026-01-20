# 1.argnames 和 argvalues 参数的具体用法
# 单参数 单值的情况
# import pytest
# class TestDemo():
#     @pytest.mark.parametrize("arg1",["参数1"])
#     def test_case01(self,arg1):
#         print("传入的值是：{}".format(arg1))


# 单参数 多值的情况
# import pytest
# class TestDemo():
#     @pytest.mark.parametrize("arg1",[1,'abc',{"a":"1","b":2},(1,2,3)])
#     def test_case01(self,arg1):
#         print("传入的值是：{}".format(arg1))

# 执行结果为用例被执行了四次，传入的值依次为：1,abc,{'a': '1', 'b': 2},(1, 2, 3)


# 多参数 多值 的情况
# argnames参数的个数必须和argvalues参数的每一组的个数一致，否则报错
# import pytest 
# class TestDemo():  # 定义测试类，类名以Test开头
#     @pytest.mark.parametrize("arg1,arg2",[(1+1,2),(2+2,4)])  # 参数化装饰器，定义两个参数arg1和arg2，传入两组测试数据
#     def test_case01(self,arg1,arg2):  # 定义测试方法，接收两个参数arg1和arg2
#         print(f"原值是：{arg1},预期是{arg2}")  # 打印当前测试用例的输入值，用于调试和查看测试执行过程
#         assert arg1 == arg2  # 断言验证，检查arg1是否等于arg2，验证测试结果是否符合预期



# parametrize 叠加使用
import pytest
@pytest.mark.parametrize("arg2",['a','b','c'])
@pytest.mark.parametrize("arg1",['1','2','3'])
def test_case04(arg1, arg2):
    all = arg1 + arg2
    print(f'叠加结果：{all}')

# 执行结果为 collected 9 items                                                                                                                   

# test_demo10.py::test_case04[1-a] 叠加结果：1a
# PASSED
# test_demo10.py::test_case04[1-b] 叠加结果：1b
# PASSED
# test_demo10.py::test_case04[1-c] 叠加结果：1c
# PASSED
# test_demo10.py::test_case04[2-a] 叠加结果：2a
# PASSED
# test_demo10.py::test_case04[2-b] 叠加结果：2b
# PASSED
# test_demo10.py::test_case04[2-c] 叠加结果：2c
# PASSED
# test_demo10.py::test_case04[3-a] 叠加结果：3a
# PASSED
# test_demo10.py::test_case04[3-b] 叠加结果：3b
# PASSED
# test_demo10.py::test_case04[3-c] 叠加结果：3c
# PASSED