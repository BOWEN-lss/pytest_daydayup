# 使用try_exvcept_finally 关键字来捕获异常
# try: 1/0   # 分母为0异常
# except ZeroDivisionError as e:
#     print(e)

# try: 1/0   # 分母不为0则不会抛出异常
# except ZeroDivisionError as e:
#     print(e)
#     raise ZeroDivisionError('分母为0')   # 手动抛出异常（异常信息为自定义）
# # 如果raise后面没有带参数，则异常信息原样抛出

# assert 进行断言（对于不确定正确与否的代码可使用assert进行断言，方便排查问题）：断言为真则继续执行，断言为假则抛出异常
# print('start')
# nunmerber = int(input('请输入1-9的数字：'))
# assert  0< nunmerber <= 9, '让你在1-9之间输入，你看你输入的啥勾八玩意，重新来'
# print('end')


# 自定义异常
# 自定义异常的类必须继承于父类Exception或者BaseException
"""
步骤：
1.在自定义异常的构造函数中，调用父类的构造函数
2.重写父类中的__str__方法输出自定义异常信息
3.编写异常处理方法处理异常（可省略）
"""

class customerror(BaseException):
    def __init__(self,msg):
        super().__init__()   # --> 调用父类的构造函数
        self.msg = msg
    def __str__(self):
        self.handle_exception()
        return self.msg
    def handle_exception(self):  # handle 的作用：处理异常
        print('处理自定义异常')

try:
    raise customerror('自定义异常5555555555555')
except customerror as e:
    print(f'自定义异常：,sdfsd')