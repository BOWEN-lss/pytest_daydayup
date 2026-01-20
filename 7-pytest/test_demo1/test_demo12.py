# ids 参数
# import pytest

# userinfo = [('张三', '123'),('李四', '456')]
# @pytest.mark.parametrize('arg', userinfo)
# def test_case01(arg):
#     print(f"用户数据：{arg}")

# 输出结果为
# test_demo12.py::test_case01[arg0] 用户数据：('张三', '123')
# PASSED
# test_demo12.py::test_case01[arg1] 用户数据：('李四', '456')
# PASSED
# 可以看出用例执行了两次，打印的arg就是userinfo中的元组，
# 现在是没有加ids参数的情况，pytest会以元组的索引作为用例名字，即 arg0，arg1

import pytest

userinfo = [('张三', '123'),('李四', '456')]
@pytest.mark.parametrize('arg', userinfo,ids=['one', 'two'])
def test_case01(arg):
    print(f"用户数据：{arg}")

# 这是加了ids参数的情况，pytest会以ids参数中的值作为用例名字，即 one，two  结果如下：
# test_demo12.py::test_case01[one] 用户数据：('张三', '123')
# PASSED
# test_demo12.py::test_case01[two] 用户数据：('李四', '456')
# PASSED
# 注意，ids参数必须和参数化的用例数量一致，否则会报错


