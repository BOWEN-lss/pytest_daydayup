# 不在类中的自动化用例 
import pytest
def test_demo1():
    """验证 1+1=2"""
    num = 1+1
    assert num == 2,'断言失败，1+1不等于2'
    print(f'num,断言成功，1+1=2') 


# 运行方法：终端中cd到当前文件所在目录，输入pytest test_demo1.py  -v -s  