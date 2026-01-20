# 面向对象的__new__方法
"""
__new__ 方法是 Python 中的一个特殊方法，它被用来创建对象并返回它。
__new__ 方法是在对象创建之前被调用的，而 __init__ 方法是在对象创建之后被调用的。
__new__ 方法返回的对象是 __init__ 方法创建的对象。
"""
"""
1.语法：
class 类名:
    def __new__(cls, *args, **kwargs):
        函数体
# 如果不自己定义__new__方法，那么Python会自动生成如下的__new__方法：
def __new__(cls, *args, **kwargs):
    return super().__new__(cls, *args, **kwargs)
目的：
__init__负责将类实例化，而在__init__()执行之前，__new__()负责创建这样一个实例对象
时机：
__new__()方法在__init__()方法之前执行
返回值：
__new__()方法返回的对象是__init__()方法创建的对象、

"""


# __new__方法的实际应用
# 1.创建实例对象
# __new__方法实在类中定义的一个方法，所以我们先创建一个类
# class A:
#     def __new__(cls, *args, **kwargs):
#         print ('这是一个__new__()方法')
#         return super().__new__(cls, *args, **kwargs)
#     def __init__(self):
#         print ('这是一个__init__()方法')
#     def hello(self):   # 定义一个方法
#         print('hello,everyone')
# A = A()
# # print(A)
# A.hello()

# 2.单例模式
# 多次实例化只创建一个对象
class A:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = super().__new__(cls, *args, **kwargs)
            cls.__instance=  obj
        return super().__new__(cls, *args, **kwargs)
    def hello(self):
        print('hello,everyone')
d = A()
A.age = 8
print(d)
f = A()
print(f)
print(d.age)
# 以上单例模式下创建的对象的内存地址一模一样，说明是同一个对象，这样的话给这个对象添加属性后，所有对象都会添加这个属性
