"""
parametrize简单应用
"""
# 语法:@pytest.mark.parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
# 参数说明:
# argnames:参数名称，必传项   参数名称为字符串，多个参数用逗号隔开
# argvalues:参数值，必传项   参数值为列表，多个参数值用逗号隔开
# indirect:参数值是否为函数，默认为False
# ids:参数值对应的名称，默认为None
# scope:参数作用域，默认为function
# 实例参考：test_demo9.py



