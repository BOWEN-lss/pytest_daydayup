import pytest
@pytest.fixture(scope="session") 
def init_session():
    print("开始执行会话级别的前置")
    yield
    print("开始执行会话级别的后置")
@pytest.fixture(scope="module",name='mdl')
def init_module():
    print("开始执行模块级别的前置02")
    yield
    print("开始执行，模块级别的后置02")

@pytest.fixture(scope="class")
def init_class():
    print("开始执行类级别的前置03")
    num = 1+1
    yield num
    print("开始执行类级别的后置03")

@pytest.fixture(scope="function")
def init_function():
    print("开始执行方法级别的前置04")
    num = 1+1
    yield num
    print("开始执行方法级别的后置04")

@pytest.fixture(params=['a',2,'b',{'name':'user1'},{'name':'user2'}],ids=['one','two','three','four','five'])
def init_params(request):
    res = request.param
    yield res
    print("开始执行参数化后置05")
