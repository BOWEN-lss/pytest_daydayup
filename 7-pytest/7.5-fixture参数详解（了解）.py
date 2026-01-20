"""
7.5-fixture参数详解（了解）
fixture参数包括：
1.scope参数：用来控制fixture的作用范围，类似于pytest的setup和teardown，默认取值为function，即方法（函数）级别
控制范围的排序为：
function > class > module > session
function：函数（方法）级别  每个函数或方法都会调用
class：类级别  每个类只运行一次
module：模块级别  每个模块（.py文件）只运行一次
session：会话级别  （每次会话）整个测试用例只运行一次，会话内所有方法，类，模块都共享这个方法
实例参考：test_demo8.py

2.params参数：用来给fixture添加参数，参数值会作为fixture的返回值
fixture的可选形参列表,支持列表传入   默认为none  列表中的每个params的值,fixture都会调用一次,类似for循环
可与参数idshuld参数一起使用,作为每个参数的标识   用request.param来获取params列表  (固定写法)
实例参考：test_demo8.py



3.ids参数：与params配合使用.用来给params参数的参数值添加标识，标识会作为测试用例的标识
使用方法:在confetst.py中定义fixture参数时，添加ids参数

4.autouse参数：用来设置fixture是否自动运行，默认为false
# 如果autouse=true,则fixture会自动调用，且其他fixture会等待fixture运行完成，再运行
实例参考：test_demo8.py  conftest.py

5.name参数：用来给fixture重命名
实例参考：test_demo8.py  conftest.py
"""
