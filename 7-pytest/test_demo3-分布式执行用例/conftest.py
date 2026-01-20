# import pytest
# import uuid
# @pytest.fixture(scope="session")
# def login():
#     session_id = str(uuid.uuid1())    # 通过uuid模块生成随机的session_id并转为字符串
#     yield session_id   # 返回session_id




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