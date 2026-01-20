#   lambda 匿名函数   有些时候，我们只需要一个 很短小、临时用一次的函数，用 def 显得太啰嗦了。
#   这时就可以用 lambda 表达式，也叫 匿名函数（没有名字的函数）
"""
语法:
lambda 参数列表: 表达式
特点：
没有名字（匿名）
只能写一行表达式（不能有多行语句）
会返回表达式的计算结果
例子：
add = lambda x, y: x + y
print(add(3, 5))  # 8
等价于
def add(x, y):
    return x + y
c=add(3,5)
print(c)
"""
# 例子：
add_number = lambda x,y :x*y
print(add_number(3,6))
# 等于
add_number= lambda x,y :x*y
c= add_number(5,9)
print(c)
# 等价于
def add_number(x,y):
    return x*y
c=add_number(4,6)
print(c)

