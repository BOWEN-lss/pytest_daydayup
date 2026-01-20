# 函数的返回值    return 语句：中止函数执行，并返回一个值，后续代码将不再执行 如果没有return语句，那么函数默认返回值为none
# return 语句可以返回一个值，也可以返回多个值，也可以是一个元组或者字典
# def add_number(a,b):
#     c = a+b
#     c1 = a+1
#     c2 = b+1
#     return c,c1,c2     #如果没有return语句，那么函数默认返回值为none   多个值用一个变量接收的话结果会是一个元组
# #    print('111')       # 函数执行到此，return语句中止函数执行，后续代码将不再执行
# total = add_number(1,2)
# print(total)


# def add_number(a,b):
#     c = a+b
#     c1 = a+1
#     c2 = b+1
#     return c,c1,c2     #如果没有return语句，那么函数默认返回值为none   多个值用一个变量接收的话结果会是一个元组
# #    print('111')       # 函数执行到此，return语句中止函数执行，后续代码将不再执行
# total1,total2,total3 = add_number(1,2)
# print(total1)
# print(total2)
# print(total3)                              # 多个值用多个变量接收的话结果会是单独呈现

# 返回值为字典时的情况
# 1.当函数需要返回 多个值，且这些值有名字 → 用字典。
def get_user_info():
    return {
        "name": "Alice",
        "age": 25,
        "email": "alice@example.com"
    }

info = get_user_info()
print(info["name"])   # Alice

# 2.当返回结果本身就是 键值对关系 → 用字典。
def add_number(a,b):
    c = a+b
    c1 = a+1
    c2 = b+1
    return {"c":c,"c1":c1,"c2":c2}     #如果没有return语句，那么函数默认返回值为none   多个值用一个变量接收的话结果会是一个元组
#    print('111')       # 函数执行到此，return语句中止函数执行，后续代码将不再执行
result = add_number(3, 5)
print(result)           # {'c': 8, 'c1': 4, 'c2': 6}
print(result["c"])      # 8
print(result["c1"])     # 4
print(result["c2"])     # 6

# 3.当要和 JSON / 配置 / API 对接 → 用字典。
import json

def get_config():
    return {
        "host": "localhost",
        "port": 8080,
        "debug": True
    }

print(json.dumps(get_config()))     # json.dumps() 是Python标准库中的一个函数，它的作用是将Python对象（如字典、列表等）转换为JSON格式的字符串


