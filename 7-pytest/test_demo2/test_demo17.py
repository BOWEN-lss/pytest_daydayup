# 在函数内部使用pytest.xfail()方法，表示用例失败
import pytest
def test_xfail():
    pytest.xfail(reason='试试能不能通过')
    print("用例1执行完毕")
    assert True

class TestDemo():
    def test_xfail1(self):
        print("用例2执行完毕")
        # assert False 
    
    def test_xfail2(self):
        pytest.xfail(reason='试试能不能通过')
        print("用例3执行完毕")


# 使用 pytest --runxfail .\test_demo17.py -v -s 可以忽略掉xfial，把案例变成普通案例执行，执行结果为全部pass