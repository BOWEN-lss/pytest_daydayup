
# parametrize 传单组数据
# import pytest
# class Test_demo9():
#     test_date = [{"username":"admin","password":"123456"}]
#     @pytest.mark.parametrize("ceshishuju",test_date)   
#     def test_login(self,ceshishuju):
#         print("请输入用户名:{}".format(ceshishuju["username"]))
#         print("请输入密码:{}".format(ceshishuju["password"]))
#         assert 1==1

# parametrize 传多组数据 当数据有两组时,用例 运行两次,有多组时,用例运行多次

import pytest
class Test_demo9():
    test_date = [{"username":"admin","password":"123456"},{"username":"admin2","password":"654321"}
                 ,{"username":"admin3","password":"543210"}]
    @pytest.mark.parametrize("ceshishuju",test_date)   
    def test_login(self,ceshishuju):
        print("请输入用户名:{}".format(ceshishuju["username"]))
        print("请输入密码:{}".format(ceshishuju["password"]))
        assert 1==1