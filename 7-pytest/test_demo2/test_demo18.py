# pytest中用xfail标记预计失败的用例
# 既可以给测试类添加标签 ，也可以给测试方法添加标签
import pytest
@pytest.mark.Login     # 给登录测试类添加登录标签
class TestLogin():
    @pytest.mark.smoke  # 给登录成功打上冒烟测试的标签
    @pytest.mark.success   # 给登录成功打上成功的标签
    def test_login_success(self):
        """登录成功"""
        print("用例1：登录成功")
    @pytest.mark.faild   # 给登录失败打上失败的标签
    def test_login_faild(self):
        """登录失败"""
        print("用例2：登录失败")

@pytest.mark.Logout   # 给退出测试类添加退出标签
class  TestLogout():
    @pytest.mark.smoke   # 给退出成功打上冒烟测试的标签
    @pytest.mark.success  # 给退出成功打上成功的标签
    def test_logout_success(self):
        """退出成功"""
        print("用例3：退出成功")
    @pytest.mark.faild    # 给退出失败打上失败的标签
    def test_logout_faild(self):
        """退出失败"""
        print("用例4：退出失败")

# 使用 pytest -m success  test_demo18.py -v -s 命令运行标签为success的用例
# 需要注意的是 用pytest5.0及 更高版本时，标签必须加在 ini文件中说明，否则执行以上命令的结果会是0个用例执行
# ini文件中配置后，执行pytest -m success  test_demo18.py -v -s 命令结果为：
# collected 4 items / 2 deselected / 2 selected                                                                                       
# test_demo18.py::TestLogin::test_login_success 用例1：登录成功
# PASSED
# test_demo18.py::TestLogout::test_logout_success 用例3：退出成功
# 另外执行结果中还会有以下告警信息
#  d:\python_learn\7-pytest单元测试框架模块\test_demo2\test_demo18.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.Login 
# - is this a typo?  You can register custom marks to avoid this warning - for details, 
# see https://docs.pytest.org/en/stable/how-to/mark.html    @pytest.mark.Login     # 给登录测试类添加登录标签
# 以上告警信息的意思是没有对标签进行注册，需要我们 自行注册标签

# 如果想运行longin标签下的用例，但是不想运行login中faild的用例，那么可以这样运行：
# pytest -m "Login and not faild" test_demo18.py -v -s  