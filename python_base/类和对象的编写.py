# 定义一个类
# class Person:
#     pass  # 空类体，占位用的
#
# # 创建一个对象 对象的创建过程也称为对象的实例化过程。类通过实例化创建出来的就是对象
# 张三 = Person()   # 类的实例化
# print(张三)
# print(Person)
from PIL.ImImagePlugin import number


# 类(class)属性(attribute)和实例(instance)属性
# 给类添加的属性就是类属性，给对象(object)添加的属性就是对象属性（实例属性）。类属性是所有对象共享的，对象属性是每个对象单独的
# 类属性可以被类和实例访问，但对象属性只能被对象（实例）访问

# class Person:
#     age = 18  # 类属性
#     sex = '男'
# zhangsan = Person()
# address='北京'
# number=10086
# print(Person.age)   # 访问的类属性
# print(Person.sex)   # 访问的类属性
#
# print(address) # 访问的实例属性
# print(number)  # 访问的实例属性
# print(zhangsan.age) # 对象可以访问实例（类）属性
# print(Person.zhagnsan.address)  #类不能访问对象属性

# 类方法、实例方法、静态方法
# 类方法、实例方法、静态方法都是类对象和实例对象都可以访问的，但类方法、实例方法只能通过类对象和实例对象访问，静态方法只能通过类对象访问
# 实例方法就是类的实例能够使用的方法
# 第一个参数必须是实例对象，该参数一般命名为self，通过它来传递实例的属性和方法，只能由实例对象调用，不需要传值（会自动传值）
# class Person:
#     def kaiche(self):
#         print('这是一个实例方法',self)
#
# zhangsan = Person()   # 这个步骤就是实例化
# print(zhangsan)  # 等价于上一行
# zhangsan.kaiche() #

"""
类方法是将类本身做为对象进行操作的方法   使用装饰器@clsmethod.第一个参数必须是当前类，该参数名一般约定为cls，通过它来传递类的属性和方法  类和实例对象都可以调用
"""
# class Person:
#     @classmethod
#     def eat(cls):
#         print('这是一个类方法',cls)
# Person.eat()   # 通过类调用类方法
# print(Person)  # 打印一下这个类
# zhangsan = Person()  # 实例化
# zhangsan.eat()  # 通过实例对象调用类方法

"""
静态方法:
用 @staticmethod 装饰器声明。
没有 self 或 cls 参数。
本质上就是放在类里的普通函数，逻辑上与类有关联
类和实例对象都可以调用
"""
class Person:
    @staticmethod
    def sleep():
        print('这是一个静态方法')
Person.sleep() # 通过类对象调用静态方法
zhangsan = Person()
zhangsan.sleep() # 通过实例对象调用静态方法