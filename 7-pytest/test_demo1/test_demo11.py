# inderict 参数用法
import pytest

# 1. 单fixture  单值 的传参
# user = ['张三','李四']
# @pytest.mark.parametrize('inderict_fixture',user,indirect=True)
# def test_case01(inderict_fixture):
#     print(f'测试方法的用户名：{inderict_fixture}')




# 2. 单fixture  多值 的传参
# userinfo = [{'user':'张三','pwd':'123456'},{'user':'李四','pwd':'654321'}]
# @pytest.mark.parametrize('inderict_fixture',userinfo,indirect=True)
# def test_case01(inderict_fixture):
#     print(f'测试方法的用户名：{inderict_fixture['user']}')
#     print(f'测试方法的用户名：{inderict_fixture['pwd']}')


# 3. 多fixture  多值 的传参（通过嵌套元组的列表）
# usermsg = [('张三','123456'),('李四','654321')]
# @pytest.mark.parametrize('inderict_fixture1,inderict_fixture2',usermsg,indirect=True)
# def test_case01(inderict_fixture1,inderict_fixture2):
#     print('这是测试用例')
 

# 4.叠加使用
user = ['张三','李四']
pwd = ['123456','654321']
@pytest.mark.parametrize('inderict_fixture2',pwd,indirect=True)
@pytest.mark.parametrize('inderict_fixture1',user,indirect=True)
def test_case01(inderict_fixture1,inderict_fixture2):
    print('这是测试用例')


