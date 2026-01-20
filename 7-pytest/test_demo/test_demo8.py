# fixture scope参数的四个作用范围
# 执行级别:对于前置来说,作用范围大的会先执行，作用范围小的会后执行,对于后置来说，作用范围小的会先执行，作用范围大的会后执行
# 作用于方法上
# import pytest
# class TestDemo8():
#     def test_case1(self):
#         num = 2+2
#         assert num == 4 ,'断言失败，2+2不等于4'
#         print("断言成功，2+2等于4")

#     @pytest.mark.usefixtures('init_session','init_module','init_class','init_function')
#     def test_case2(self):
#         num = 2+3
#         assert num == 5,'断言失败，2+3不等于5'
#         print("断言成功，2+3等于5")

# 作用于类上
# import pytest
# @pytest.mark.usefixtures('init_function')
# class TestDemo8():
#     def test_case1(self):
#         num = 2+2
#         assert num == 4 ,'断言失败，2+2不等于4'
#         print("断言成功，2+2等于4")

#     @pytest.mark.usefixtures('init_session','init_module','init_class')
#     def test_case2(self):
#         num = 2+3
#         assert num == 5,'断言失败，2+3不等于5'
#         print("断言成功，2+3等于5")


# ==========================params参数================================
# 在conftest.py文件中定义params的值   用例中新增用例调用params参数

# import pytest
# @pytest.mark.usefixtures('init_params')
# def test_case3(init_params):
#     print('获取的params参数为：{}'.format(init_params))

# 执行结果如下:
"""
======================================================= test session starts =======================================================
platform win32 -- Python 3.13.9, pytest-9.0.2, pluggy-1.6.0 -- D:\software\python-3.13.9\program\python.exe
cachedir: .pytest_cache
rootdir: D:\python_learn\7-pytest单元测试框架模块\test_demo
collected 5 items                                                                                                                   

test_demo8.py::test_case3[a] 获取的params参数为：a
PASSED开始执行参数化后置05

test_demo8.py::test_case3[2] 获取的params参数为：2
PASSED开始执行参数化后置05

test_demo8.py::test_case3[b] 获取的params参数为：b
PASSED开始执行参数化后置05

test_demo8.py::test_case3[init_params3] 获取的params参数为：{'name': 'user1'}
PASSED开始执行参数化后置05

test_demo8.py::test_case3[init_params4] 获取的params参数为：{'name': 'user2'}
PASSED开始执行参数化后置05
======================================================== 5 passed in 0.02s ======================================================== 
fixture 对每个params的值都单独执行了一遍用例


ids 参数
ids参数用来给params参数指定名称，这样在用例中就可以通过名称来调用params参数
在conftest.py文件中定义params的值后,写上ids的值,再次执行用例
结果如下:

PS D:\python_learn\7-pytest单元测试框架模块\test_demo> pytest .\test_demo8.py -v -s
======================================================= test session starts =======================================================
platform win32 -- Python 3.13.9, pytest-9.0.2, pluggy-1.6.0 -- D:\software\python-3.13.9\program\python.exe
cachedir: .pytest_cache
rootdir: D:\python_learn\7-pytest单元测试框架模块\test_demo
collected 5 items                                                                                                                   

test_demo8.py::test_case3[one] 获取的params参数为：a
PASSED开始执行参数化后置05

test_demo8.py::test_case3[two] 获取的params参数为：2
PASSED开始执行参数化后置05

test_demo8.py::test_case3[three] 获取的params参数为：b
PASSED开始执行参数化后置05

test_demo8.py::test_case3[four] 获取的params参数为：{'name': 'user1'}
PASSED开始执行参数化后置05

test_demo8.py::test_case3[five] 获取的params参数为：{'name': 'user2'}
PASSED开始执行参数化后置05

可以看出,ids参数给每次params的取值都进行了了标记 




#=================autouse参数===================
autouse参数:autouse参数默认为False,如果为True,则表示自动执行,不需要在用例中调用
在conftest.py文件中设置会话级别前置的 autouse=True   在用例中去掉会话级别前置的调用
代码如下:
"""
# import pytest
# class TestDemo8():
#     def test_case1(self):
#         num = 2+2
#         assert num == 4 ,'断言失败，2+2不等于4'
#         print("断言成功，2+2等于4")

#     @pytest.mark.usefixtures('init_module','init_class','init_function')
#     def test_case2(self):
#         num = 2+3
#         assert num == 5,'断言失败，2+3不等于5'
#         print("断言成功，2+3等于5")

# 执行结果如下:
"""
test_demo8.py::TestDemo8::test_case1 开始执行会话级别的前置
断言成功，2+2等于4
PASSED
test_demo8.py::TestDemo8::test_case2 开始执行模块级别的前置02
开始执行类级别的前置03
开始执行方法级别的前置04
断言成功，2+3等于5
PASSED开始执行方法级别的后置04
开始执行类级别的后置03
开始执行，模块级别的后置02
开始执行会话级别的后置

可以看出,autouse参数为True时,会话级别前置被自动执行,不需要在用例中调用
"""

# =====================name参数=========================
# name参数:name参数用来给fixture起一个别名,这样在用例中就可以通过别名来调用fixture
import pytest
class TestDemo8():
    def test_case1(self):
        num = 2+2
        assert num == 4 ,'断言失败，2+2不等于4'
        print("断言成功，2+2等于4")

    # @pytest.mark.usefixtures('mdl','init_class','init_function')
    def test_case2(self,mdl):
        num = 2+3
        assert num == 5,'断言失败，2+3不等于5'
        print("断言成功，2+3等于5")