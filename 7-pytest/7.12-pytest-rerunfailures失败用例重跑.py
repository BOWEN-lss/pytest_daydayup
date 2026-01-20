"""
pytest-rerunfailures失败用例重跑
当项目中存在偶发错误时，可以使用pytest-rerunfailures失败用例重跑

插件安装：pip install pytest-rerunfailures

使用方式：
1.用命令行执行  
pytest --reruns 3 --reruns-delay 1 test_demo19.py -s -v -n
--reruns 3 是重跑的次数    --reruns-delay 1 是重跑的间隔时间
-s 是显示用例执行过程  -v 是显示详细日志  -n 是多线程执行

也可以指定异常类型重跑，其中多个  --only-rerun 之间是或的关系
pytest --reruns 3 --only-rerun AssertionError --only-rerun ValueError test_demo19.py -s -v -n

2.用装饰器执行
语法：@pytest.mark.flaky(reruns=3,reruns_delay=1)  # 重跑次数，重跑间隔时间



案例参考 test_demo2文件夹下的  test_demo20.py
"""