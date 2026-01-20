"""
pytest-xdist分布式执行用例
当测试用例数量很多时，一条条执行的速度会很慢，这时可以使用pytest-xdist插件进行分布式执行
一、分布式执行用例的设计原则
1.用例之间是独立的，用例与用例之间没有依赖关系，用例可以完全独立运行
2.用例执行没有顺序要求，随机顺序都能正常执行
3.每个用例都可以重复运行，运行结果不会影响其他用例的执行

二、pytest-xdist插件安装
pip install pytest-xdist

三 、pytest-xdist插件使用
原理：xdist会产生一个或者多个workers，workers通过master来控制；每个workers负责执行完整的用例集，
然后按照master的要求运行测试，而master不执行测试任务
执行方法：
# 使用 pytest -n 3 test_demo23.py -v -s 指定核心线程数量    n 表示同时执行的线程数量，一般为CPU核心数量的一半，防止电脑卡顿
# 也可以使用 pytest -n auto test_demo23.py -v -s  自动获取CPU核心数量且自动分配合适的线程数

# 自定义执行模式
# 按照同一个作用域方法来分组，然后将每个作用域方法分配给不同的worker，确保同一个组的测试用例在同一个进程中执行
# pytest -n 3 --dist=loadscope test_demo23.py -v -s

# 按照同一个文件名来分组，然后将每个测试组分配给不同的worker，确保同一个组的测试用例在同一个进程中执行
pytest -n 3 --dist=loadfile test_demo23.py test_demo24.py test_demo25.py -v -s

# 将每个用例，分别给所有的worker，相当于开了几个线程，同一个用例就执行多少遍
pytest -n 3 --dist=each  test_demo23.py  -v -s



使用分布式运行有个问题是会导致 session 级别及以上的案例执行多次，所以我们可以通过文件锁的方式进行进程间的通信
文件锁在os中很常见，如果有多个程序同步访问或者修改同一个文件，很容易因为文件数据不同步而出现问题
通过给文件加锁的操作可以实现让scope=session的fixture在test session中只执行一次 
给文件加锁（filelock）后，同一时间只能有一个程序修改此文件，或者程序都只能读取文件 
文件锁的作用就是第一次在conftest.py 文件中生成session_id后给它加锁，后面的函数调用sessio_id时，会先判断加锁文件中是否存在session_id
如果存在就直接拿取，而不是重新生成

案例参考：test_demo3-分布式执行用例文件夹下的test_demo24.py  和conftest.py 文件

""" 