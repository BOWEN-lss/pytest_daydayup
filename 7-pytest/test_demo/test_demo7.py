# 先创建conftest.py 文件，文件中设置fixture的作用域为方法级别
# import pytest
# class TestDemo7: # 创建测试类
#     def test_demo7_1(self): # 创建测试方法
#         num = 1+1
#         assert num == 2,'断言失败，1+1不等于2'
#         print(f'num,断言成功，1+1=2') 
#     @pytest.mark.usefixtures('init_function')  # 使用fixture  方法1 
#     def test_demo7_2(self): # 创建测试方法
#         num = 1+2
#         assert num == 3,'断言失败，1+2不等于3'
#         print(f'num,断言成功，1+2=3') 

# 加上fixture 后实现了只针对一个案例的前置和后置  
# conftest.py 文件定义前置函数，在测试用例方法调用，调用方式有两种，一是直接往用例方法中传入前置函数的函数名，如下所示 

# import pytest
# class TestDemo7: # 创建测试类
#     def test_demo7_1(self): # 创建测试方法
#         num = 1+1
#         assert num == 2,'断言失败，1+1不等于2'
#         print(f'num,断言成功，1+1=2') 
#     # @pytest.mark.usefixtures('init_function')  # 使用fixture  方法1 
#     def test_demo7_2(self,init_function): # 创建测试方法
#         num = 1+2
#         assert num == 3,'断言失败，1+2不等于3'
#         print(f'num,断言成功，1+2=3') 

# 一种是通过usefixtures 调用，这种方式可以传多个前置，也可以叠加调用前置（遵循就近原则执行前置）
# import pytest
# class TestDemo7: # 创建测试类
#     def test_demo7_1(self): # 创建测试方法
#         num = 1+1
#         assert num == 2,'断言失败，1+1不等于2'
#         print(f'num,断言成功，1+1=2') 
#     @pytest.mark.usefixtures('init_function','init_function02')  # 使用fixture  方法1 
#     def test_demo7_2(self): # 创建测试方法
#         num = 1+2
#         assert num == 3,'断言失败，1+2不等于3'
#         print(f'num,断言成功，1+2=3') 

# 运行结果如下：

# test_demo7.py::TestDemo7::test_demo7_1 num,断言成功，1+1=2
# PASSED
# test_demo7.py::TestDemo7::test_demo7_2 开始执行方法级别的前置
# 开始执行方法级别的前置02
# num,断言成功，1+2=3
# PASSED开始执行方法级别的后置02
# 开始执行方法级别的后置

# 后置函数执行顺序：先执行方法级别的后置，再执行类级别的后置，最后执行模块级别的后置，遵循后进先出原则，所以会先执行后置02
# 如果想想执行后置01，在执行后置02，可以叠加装饰器，如下：

# import pytest
# class TestDemo7: # 创建测试类
#     def test_demo7_1(self): # 创建测试方法
#         num = 1+1
#         assert num == 2,'断言失败，1+1不等于2'
#         print(f'num,断言成功，1+1=2') 
#     @pytest.mark.usefixtures('init_function')
#     @pytest.mark.usefixtures('init_function02')  # 使用fixture  方法1 
#     def test_demo7_2(self): # 创建测试方法
#         num = 1+2
#         assert num == 3,'断言失败，1+2不等于3'
#         print(f'num,断言成功，1+2=3') 

# 叠加后的执行结果如下：
# test_demo7.py::TestDemo7::test_demo7_1 num,断言成功，1+1=2
# PASSED
# test_demo7.py::TestDemo7::test_demo7_2 开始执行方法级别的前置02
# 开始执行方法级别的前置
# num,断言成功，1+2=3
# PASSED开始执行方法级别的后置
# 开始执行方法级别的后置02
# 这里前置02被先执行，原因是叠加了前置，执行顺序遵循就近原则，
# 先执行方法级别的后置，再执行类级别的后置，最后执行模块级别的后置


# fixture的前置传参
# 创建conftest.py 文件，并定义参数化函数，如下：
# @pytest.fixture(scope="function")
# def init_function03():
#     print("开始执行方法级别的前置03")
#     num = 1+1
#     yield num
#     print("开始执行方法级别的后置03")

# 创建测试类，并定义测试方法，如下：
import pytest
class TestDemo7: # 创建测试类
    @pytest.mark.usefixtures('init_function03')
    def test_demo7_1(self,init_function03): # 创建测试方法
        assert init_function03 == 2,'断言失败，1+1不等于2'
        print(f'num,断言成功，1+1=2') 
  # 使用fixture 
