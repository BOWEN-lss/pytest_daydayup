"""
parametrize参数详解（了解）

一、argnames 和 argvalues 参数的具体用法
二 、inderict 参数用法
三、ids参数用法
四、scope参数用法
五、与其他mark一起使用
"""

# 一、argnames 和 argvalues 参数的具体用法
# 单参数 单值的情况

# 单参数 多值的情况
# arg values 可以传入多样的python数据类型：列表，嵌套了元组的列表 ，字典，字符串等 
# 传入多个值时，用例会被执行多次，每次取一个值去执行

# parametrize参数叠加使用

# 实例参考test_demo10.py


# 二、inderict 参数用法
# inderict参数一般与pytest的request、fixture一起使用
# 当inderict参数为True时，argnames则要传入fixture函数名称，不再是一个普通参数，二十要被调用的fixture参数，argvalues则是要给这个函数传的值
# 做法其实与@pytest.fixture(params)一样，但使用了@pytest.mark.parametrize相当于参数化了fixture，而不是只有固定的一套数据传入使用

# 示例参考：test_demo1文件夹下的 test_demo11.py


# 三、ids参数用法
# ids参数的作用是标记子用例执行名称，增加可读性 ，中文需要转码
# ids参数可以给参数化的用例起名字，参数化的用例会以列表的方式返回，列表的每个元素是一个元组,
# 元组中第一个元素是参数化的用例名字，第二个元素是参数化的用例返回值
# ids参数可以和argnames参数一起使用，也可以单独使用
# ids参数可以和argvalues参数一起使用，也可以单独使用

# 示例参考：test_demo1文件夹下的 test_demo12.py

# 四、scope参数用法  给传入的前置后置函数的作用域进行重新定义
# scope参数的作用范围与fixture一致，当inderict参数为True时，scope参数作用域为函数级别，当inderict参数为False时，scope参数作用域为模块级别
# scope 的范围会覆盖fixture的scope范围，如果同一个被调用的fixture有多个parametrize定义了scope，取第一条的范围

# 实例参考：test_demo1文件夹下的 test_demo13.py

# 五、parametrize 与其他mark一起使用
# 参数化与其他mark一起使用，参数化的用例会以列表的方式返回，列表的每个元素是一个元组 
# 实例参考：test_demo1文件夹下的 test_demo14.py

