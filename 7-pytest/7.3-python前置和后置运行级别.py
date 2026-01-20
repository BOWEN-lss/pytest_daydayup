"""
python前置和后置运行级别
python 前置运行指的是在测试用例执行之前的动作。比如查看个人信息的测试用例，需要把登录的动作在查看信息之前完成
python 后置运行指的是在测试用例执行之后的动作。比如查看个人信息的测试用例，在查看信息之后，需要把退出的动作执行

根据前置和后置的使用场景划分为3种级别
1.在类的内部和外部都可以执行的前置和后置  （方法级别） ：
setup/teardown     setup 是在类的开始执行，teardown是在类的结束执行
2.在类外执行：
setup_module/teardown_module  setup_module是在模块开始执行(针对某个py文件的前置)，teardown_module是在模块结束执行(针对某个py文件的后置)
setup_function/teardown_function setup_function是在函数开始执行(针对某个函数的前置)，teardown_function是在函数结束执行(针对某个函数的后置)
3.在类内执行：
setup_class/teardown_class  setup_class是在类开始执行(针对某个类的前置)，teardown_class是在类结束执行(针对某个类的后置)
setup_method/teardown_method  setup_method是在方法开始执行(针对某个方法前的前置)，teardown_method是在方法结束执行(针对某个方法后的后置) 
"""

# 1.在类的内部和外部都可以执行的前置和后置  （方法级别）不区分测试用例是在类中还是不在类中 ，均可使用
# setup/teardown：无论是类内还是类外，每个方法（用例）都会执行一次
# setup：方法运行前执行
# teardown：方法运行后执行



# 实践结果：python3.0版本后pytest已经不会识别setup和teardown了需要使用 fixtures 来代替
# 案例参考：test_demo3.py


# 在类中的前置和后置

# 案例参考：test_demo4.py

# 2.在类外执行：
# setup_module/teardown_module  (针对某个py文件的前置/后置) 只有在class 外部时才会被执行。整个py文件只执行一次
# setup_module 在文件执行前执行   teardown_module 在文件执行后执行

# setup_function/teardown_function  只有在类的外部的方法才会执行，每个方法（函数）执行一次
# setup_function 类外部的方法执行前执行  teardown_function 类外部的方法（函数）执行后执行
# 案例参考：test_demo5.py


# 3.在类内执行：
# setup_class/teardown_class  (针对某个类内的前置/后置) 仅在类内部时才会被执行。整个类只执行一次
# setup_class 类内部执行前执行   teardown_class 类内部执行后执行

# setup_method/teardown_method  (针对某个方法内的前置/后置) 仅在类内部方法时才会被执行。每个方法（函数）只执行一次

# 案例参考：test_demo6.py