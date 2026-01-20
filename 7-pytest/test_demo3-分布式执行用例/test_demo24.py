class TestCase:
    def test_demo1(self,login):
        with open(r"D:\python_learn\7-pytest单元测试框架模块\test_demo3-分布式执行用例\session-id01.txt", "w") as f:
            f.write(login)
        print("用例1开始执行")
    
    def test_demo2(self,login):
        with open(r"D:\python_learn\7-pytest单元测试框架模块\test_demo3-分布式执行用例\session-id02.txt", "w") as f:
            f.write(login)
        print("用例2开始执行")

    def test_demo3(self,login):
        with open(r"D:\python_learn\7-pytest单元测试框架模块\test_demo3-分布式执行用例\session-id03.txt", "w") as f:
            f.write(login)
        print("用例3开始执行")

    def test_demo4(self,login):
        with open(r"D:\python_learn\7-pytest单元测试框架模块\test_demo3-分布式执行用例\session-id04.txt", "w") as f:
            f.write(login)
        print("用例4开始执行")

# 以上为conftest.py文件中的fixture作用域为session时，不使用分布式执行案例，生成的四个文件中的session-id都是一样的，
# 说明整个过程中的session_id只生成了一次

# 但是使用 pytest -n 3 .\test_demo24.py -v 命令进行分布式执行案例时，session_id会生成4次，分别生成在四个文件中
# 这并不符合我们的预期，我们可以考虑使用filelock模块来实现session_id只生成一次
# 1.安装filelock模块
# pip install filelock

# 2.修改conftest.py文件
import pytest
import uuid
from filelock import FileLock   # 导入filelock模块
import os
import json
@pytest.fixture(scope="session")  
def login(tmp_path_factory,worker_id):  # worker_id参数是pytest内置的参数，用于获取当前worker的编号
    if worker_id == "master":  # 如果是主进程，则生成session_id
        """使用伪代码获取登录token，实际工作中要用真实token"""
        token = str(uuid.uuid1())    # 通过uuid模块生成随机token并转为字符串
        print(f'fixtrue,获取token:{token}')
        os.environ["TOKEN"] = token  # 将token保存到环境变量(全局变量)中
        return token  # 返回token
    root_tmp_dir = tmp_path_factory.getbasetemp().parent  # 获取临时目录
    fn = root_tmp_dir / "data.json"  # 拼接文件锁的路径
    with FileLock(str(fn)+'.lock'):  # 使用filelock模块创建文件锁 
        if fn.is_file():  # 判断文件是否存在
            token = json.loads(fn.read_text())  # 存在则读取文件
            print(f'读取文件的token:{token}')
        else:   # 当文件不存在时
            token = str(uuid.uuid1())    # 通过uuid模块生成随机token并转为字符串
            print(f'fixtrue,获取token:{token}')
            fn.write_text(json.dumps(token))  # 将token写入文件
            print(f'首次运行，token的值为:{token}')
            os.environ["TOKEN"] = token
    return token

# 修改完后再次运行可以看出4个txt文件中的内容一致，说明session_id只生成了一次
# 即使是使用 pytest -n 3 .\test_demo24.py -v 命令进行分布式执行案例时，session_id也只生成了一次