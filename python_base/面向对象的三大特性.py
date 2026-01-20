# 1.封装
# 2.继承  分为单继承和多继承
# class Person:
#     eat = '吃吃吃'
#     sleep = '睡觉睡觉'
# class kids(Person):
#     print('cry')
#     print(Person.eat)
#     print(Person.sleep)
# k = kids()


# 单继承
# class Person():
#     eat = '吃吃吃'
#     sleep = '睡觉睡觉'
#
# class kids(Person):
#     eat = 'chifan'
#     sleep  = 'shuijiao'
#
# class child(kids):
#     eat = 'chi-fan'
# print(child.eat)

# 以上代码的输出结果为 chi-fan 继承了kids类中的属性，
# 如果child中没有属性，那么输出结果就是kids中的属性，即 chifan
# class Person():
#     eat = '吃吃吃'
#     sleep = '睡觉睡觉'
#
# class kids(Person):
#     eat = 'chifan'
#     sleep  = 'shuijiao'
#
# class child(kids):
#     pass
# print(child.eat)
# 如果kids中也没有属性，那么输出结果就是 Person 中的属性，即 吃吃吃
# class Person():
#     eat = '吃吃吃'
#     sleep = '睡觉睡觉'
#
# class kids(Person):
#     pass
#
# class child(kids):
#     pass
# print(child.eat)

# 以上可以看出单继承的执行顺序为优先取子中的属性，子类中没有的话会取父类中的属性，就这样一层层的往上取值



# 多继承 分为无重复多继承链和有重复多继承链
# 无重复多继承链
# class Person():
#     age = 18
#
# class animal():
#     feet = 4
# class mation():
#     worktime = 24
#
# class slary():
#     pationte = 1800
#
# class programer(Person, animal, mation):
#     pass
# print(Person.age)
"""
无重复继承顺序规则：
从左到右：按照类定义时括号中父类的书写顺序
深度优先：先沿着第一个父类的继承链向上查找，再依次处理后续父类
如果访问 programer.age，Python会按照上述顺序查找，直到找到 age 属性为止
"""


# 有重复多继承链

# class D():
#     age= 17
#
# class C(D):
#      age= 18
#
# class B(D):
#     age= 19
#
# class A(B,C):
#      age= 20
# print (A.age)   # 资源的执行顺序：首先是自身，如果自身没有，那就会从父类中查找，如果父类中没有，就会从父类的父类中查找，依次类推
                # 因此本段代码中的查找顺序为：A.age -> B.age -> C.age -> D.age


# 3.多态
# 多态指的是一类事务有多种形态，多态性是在继承中体现的
# 多态：不同的子类调用相同的方法，产生不同的结果。关注点在于‘对象的行为和属性’而非类型

class Animal():
    # def talk(self):
    #     print('动物在叫')  # 默认实现
    # def move(self):
    #     print('动物在移动')
    pass

class Dog(Animal):
    def talk(self):  # 重写父类方法
        print('汪汪汪')
    def move(self):   # 重写移动方式
        print('狗在跑步')

class Cat(Animal):
    def talk(self):   # 重写父类方法
        print('喵喵喵')
    def move(self):   # 重写移动方式
        print('猫在悄悄走')

class Bird(Animal):
    def talk(self):   # 重写父类方法
        print('叽叽喳喳')
    def move(self):   # 重写移动方式
        print('鸟在飞翔')

# 多态的应用函数
def make_animal_talk(animal):
    animal.talk()  # 统一接口，不同行为

def show_animal_move(animal):
    animal.move()  # 统一接口，不同行为

# 创建不同动物对象
animals = [Dog(), Cat(), Bird()]

# 多态的体现：同一个函数处理不同类型对象
print("动物们都在说话：")
for animal in animals:
    make_animal_talk(animal)  # 根据实际类型调用对应方法

print("\n动物们的移动方式：")
for animal in animals:
    show_animal_move(animal)  # 根据实际类型调用对应方法