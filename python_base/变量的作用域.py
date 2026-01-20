# 函数（function）变量（variable）的作用域
"""
1. 什么是作用域？
作用域 (Scope) 就是变量能被访问到的范围。
在 Python 中，变量是否能被访问，取决于它定义的位置。

2. Python 的作用域规则 —— LEGB
Python 遵循 LEGB 原则（从内到外查找变量）：
L (Local)：局部作用域，函数内部定义的变量,出了内部就不能使用了
E (Enclosing)：嵌套作用域，内函数能访问外层函数的变量。
G (Global)：全局作用域，模块级别定义的变量。
B (Built-in)：内置作用域，Python 内置的名字，比如 len, print。
📌 查找变量时，Python 会按照 L → E → G → B 的顺序查找。
"""

# python 的局部变量
# def demo1():
#      a = 1
#      print('函数的内部:{}'.format(a))
# demo1()
# # print('函数的外部:{}'.format(a))    # 如果在外部打印变量a的话会直接报错，因为局部变量a只在函数内部有效，出了函数就无效了

# python的全局变量
# var2='变量2'              # 变量写在函数的外部，因此为全局变量
# def demo2():
#     print('函数的内部变量:{}'.format(var2))
# demo2()
# # 上面的写法就成功的把外部的变量2赋值给了内层函数的变量2
# print('函数的外部变量:{}'.format(var2))
# # 全局变量在外部也可以成功赋值

# 如果想在函数内部定义一个变量，但是在外部调用这个变量的话，就需要用到global关键字来定义全局变量
def demo3():
    global var3
    var3 = '变量3'   # 内部定义变量3
    print('函数内部变量：{}'.format(var3))
demo3()   # 内部调用变量3   调用成功
print('函数外部变量：{}'.format(var3))   # 外部调用变量3  调用成功


