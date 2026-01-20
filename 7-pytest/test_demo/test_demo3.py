"""不在类中的前置和后置"""
# def test_case01():
#     """验证 1+1=2"""
#     num = 1+1
#     assert num == 2,'断言失败，1+1不等于2'
#     print(f'num,断言成功，1+1=2') 


# def test_case02():
#     """验证 1+2=3"""
#     num = 1+2
#     assert num == 3,'断言失败，1+2不等于3'
#     print(f'num,断言成功，1+2=3') 
# 如果这两条测试案例为查看用户信息的功能，那么就需要添加登录前置和退出后置

# 不在类中的前置
# def setup():
#     """用例前置"""
#     print('这是登录接口(不在类中的用例前置)')

# def teardown():
#     """用例后置"""
#     print('这是退出接口(不在类中的用例后置)')

# def test_case01():
#     """验证 1+1=2"""
#     num = 1+1
#     assert num == 2,'断言失败，1+1不等于2'
#     print(f'num,断言成功，1+1=2') 


# def test_case02():
#     """验证 1+2=3"""
#     num = 1+2
#     assert num == 3,'断言失败，1+2不等于3'
#     print(f'num,断言成功，1+2=3') 




"""以上方法已经不适用与python3.0以后的版本助，下面为python3.0以后的方法"""
# 前置后置都执行：
# import pytest

# @pytest.fixture
# def login():
#     print('这是登录接口（fixture 前置）')
#     yield  # yield 
#     print('这是退出接口（fixture 后置）')


# def test_case01(login):
#     num = 1 + 1
#     assert num == 2
#     print('test_case01 执行')


# def test_case02(login):
#     num = 1 + 2
#     assert num == 3
#     print('test_case02 执行')

# 只要前置，不要后置
# import pytest

# @pytest.fixture
# def login():
#     print('这是登录接口（fixture 前置）')
#     # yield  # yield 
#     # print('这是退出接口（fixture 后置）')


# def test_case01(login):
#     num = 1 + 1
#     assert num == 2
#     print('test_case01 执行')


# def test_case02(login):
#     num = 1 + 2
#     assert num == 3
#     print('test_case02 执行')



# 只要后置 ，不要前置
import pytest
@pytest.fixture(autouse=True)
def login():
    pass
    yield  # yield 
    print('这是退出接口（fixture 后置）')

def test_case01(login):
    num = 1 + 1
    assert num == 2
    print('test_case01 执行')


def test_case02(login):
    num = 1 + 2
    assert num == 3
    print('test_case02 执行')