"""
7.2-pytest用例设计
"""
# pytest用例设计规则
# 1. 测试用例文件必须以test_开头或者以_test.py结尾
# 2. 用例的函数必须以test_开头
# 3. 用例的类必须以Test开头
# 4. 类中的方法必须以test_开头
# 5.所有的包（package）中都必须包含一个__init__.py文件

"""
不在类中的测试用例
"""
# 首先用例名称必须为test_开头  如 test_demo 中的 test_demo1.py


""""在类中的测试用例"""
# 如 test_demo 中的 test_demo2.py

# pytest 在vscode中的执行方法：
# 新建power shell终端，cd 到项目目录下，输入 pytest 运行 或者在任意位置输入案例所在路径 
# pytest D:\python_learn\7-pytest单元测试框架模块\test_demo\test_demo4.py -v -s
# 只执行脚本中的某条案例：pytest test_demo4.py::TestCase::test_case01 -v -s