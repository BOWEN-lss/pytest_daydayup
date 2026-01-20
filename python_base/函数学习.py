# 1.定义函数
# def add_number(a,b):    # 形参
#     print('结果:{}'.format(a+b))
# add_number(1,2)    # 实参
from click import argument


# 2.位置参数   数量和位置必须一致
# def say_hello(name,age,address):
#     print(f'hello,我的名字是{name},我今年{age},我来自{address}')
#
# say_hello('xiaoming',20,'bejijg')

# 3.关键字参数   位置可以不一致
# def say_hello(name,age,address):
#     print(f'hello,我的名字是{name},我今年{age},我来自{address}')
#
# say_hello(name='xiaoming',address='bejijg',age=20)

# 4.默认值参数 (defult_arguments)
# def default_arguments(name,age,address='beijing'):
#     print(f'hello,老子是新来的，老子叫{name},老子今年芳龄{age},来自{address}')
# default_arguments(name='你大爷',age=28)
#
# # 5.可变参数
# def demo1(my,*name):
#     print(f'大家好，我叫{my}，下面这些人，我都不认识')
#     for i in name:
#         print(f'{i}')
# demo1('小明','张三','李四','李武')

def demo2(my,**name):
    print(f'大家好，我叫{my}，下面这些人，我都不认识')
    for i in name.values():
        print(f'{i}')
demo2(my='小明',name='张三',name1='李四',name2='王五')






