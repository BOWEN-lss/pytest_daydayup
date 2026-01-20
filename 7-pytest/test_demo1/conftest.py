import pytest
@pytest.fixture()
def inderict_fixture(request):
    user = request.param
    print(f"传入的用户名：{user}")
    yield user

@pytest.fixture()
def inderict_fixture(request):
    userinfo = request.param
    print(f"传入的用户名：{userinfo['user']}")
    print(f"传入的密码：{userinfo['pwd']}")
    yield userinfo


@pytest.fixture()
def inderict_fixture1(request):
    user = request.param
    print(f"传入的用户名：{user}")

@pytest.fixture()
def inderict_fixture2(request):
    pwd = request.param
    print(f"传入的密码：{pwd}")

@pytest.fixture()
def inderict_fixture3(request):
    userinfo = request.param
    print(f"传入的元组：{userinfo}")