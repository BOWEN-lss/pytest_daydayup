"""
pytest自定义前置后置-fixture的简单应用
如果在某个脚本中有多条案例，但是只想对某一条案例执行前置和后置，那么可以在脚本中定义fixture，然后调用fixture
"""
# 1.conftest.py 文件介绍
# 2.fixture 的简单应用
# 3.fixture的前置传参

# fixture  的实际应用要结合conftest.py 文件，我们将前置函数写在conftest.py 文件中，可以跨文件调用前置
# conftest.py 是fixture函数的一个集合 我们可以把所有用例的的前置和后置都写在conftest.py 文件中，供其他功能模块调用
# conftest.py 文件是不需要导入的，pytest 会自动寻找conftest.py 文件
# conftest.py 特点：
# 1.文件名必须是conftest.py
# 2.不需要import导入，pytest会自动寻找conftest.py文件
# 3.文件放到项目的根目录下可以全局调用，放到某个文件夹下则只能供该文件夹下的测试案例调用

# conftest.py 文件的使用场景：
# 1.接口自动化公用的session或token
# 2.web自动化时driver实例化




# fixture 的简单应用
# 实例参考test_demo7.py 与conftest.py 文件 



# fixture的前置传参
# 当前置操作中产生的返回值需要被用例使用，需要用到前置传参。如在web自动化中可以将driver浏览器对象写入前置并传入测试用例中使用
# 我们在定义前置函数时可以用yield关键字（相当于return）返回参数，供测试用例方法使用

# 实例参考test_demo7.py 与conftest.py 文件