# 面向对象的__init__方法(也叫构造方法)
# 语法结构
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('这是构造方法')   # __init__方法没有返回值，且在类中只能有一个

# 目的：初始化对象属性
# 时机：每个对象创建时，都会调用

# 通过__init__方法来初始化实例属性和方法
# class Person:
#     def __init__(self):  # 初始化实例属性，不传实参
#         self.name = '张三'
#         self.age = 18
#
#     def imagenation(self):
#         print('我是{}，我今年{}'.format(self.name,self.age))
#
# D=Person()    # 当__init__中没有实参时，D对象属性name和age会自动初始化为'张三'和18
# D.imagenation()
#
# # 通过__init__方法（包含实参时）
# class Person:
#     def __init__(self,name,age):  # 初始化实例属性，不传实参
#         self.name = name
#         self.age = age
#
#     def imagenation(self):
#         print('我是{}，我今年{}'.format(self.name,self.age))
#
# D=Person('张三',18)    # 当__init__中有实参时，此处也必须传入实参
# D.imagenation()

# 子类调用父类的构造方法
# 子类继承父类，父类有__init__方法，子类也继承__init__方法，子类对象创建时，会调用父类的__init__方法
# 首先定义一个父类
class Animal:
    def __init__(self):
        self.eyes = 2
        self.legs = 4
# 定义一个子类来继承父类
class Dog(Animal):
    def __init__(self):
        super().__init__()  # 加上这句代码才可以调用父类中的属性
        self.kind = '金毛'
        self.name = '旺财'
        self.age = 5
        print('这是子类的构造方法')
    def bark(self):
        print('我是动物类，我有{}只眼睛{}条腿'.format(self.eyes,self.legs)) 
        print('我是{}狗，我叫{}，我今年{}岁'.format(self.kind,self.name,self.age))
d = Dog()
d.bark()
