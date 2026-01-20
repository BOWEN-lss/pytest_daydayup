"""
pytest中用xfail标记预计失败的用例
使用场景：功能未开发完成，但是测试用例已经完成。可以很明确的知道用例执行一定失败。这种情况可以用xfail标记
用例执行结果中的XFAIL指的是符合预期的失败   XPASS指的是不符合预期的通过

"""
# 语法：@pytest.mark.xfail(condition=none, reason="失败原因",raises=True,run=True,strict=True)
# 参数 condition 指的是符合某个条件时，会标记用例为失败  ；
 
# reason ：失败原因 ，默认为 none  可以在这里指定原因

# raises ：默认为none 可以指定为一个异常类或者多个异常类的元组，表明我们期望用例上报指定的异常
# 如果用例的失败不是期望的异常导致的，pytest会把测试结果标记为failed

# run ： 默认为true，表示用例执行失败时，xfail标记的用例会继续执行，并把结果标记为xfail
# 当run=false时，xfail标记的用例会跳过执行，并把结果标记为xfail

# strict ： 默认为false,当srict为false时，如果用例执行失败，结果标记为xfail，表示符合预期的失败，
# 如果用例执行成功，结果标记为xpass，表示不符合预期的通过
# 当 strict=true时，如果用例执行失败，结果标记为xfail，表示不符合预期的失败，
# 如果用例执行成功，结果标记为faild

# 也可以在pytest.ini文件中配置xfail参数,使得所有不符合预期的成功都被标记为faild   用例中的strict = true只针对该条用例，
# ini文件中的strict = true 则针对模块下所有用例
# ini文件在项目根目录下新建即可 ，建完后会自动进入_pycache_路径下 
# 案例参考test_demo2文件夹下的  test_demo16.py



# 运行时忽略xfail标记
# 可以通过pytest --runxfail参数忽略xfail标记,使案例变成正常的案例，同时 pytest.xfail()也将会失效
# 但是运行忽略xfail时，需要先把Ini文件中的strict = true改为false 或者删除。因为Ini文件中的strict = true这个命令的权限最大，会优先执行

# 在用例函数内部使用pytest.xfail()方法
# 案例参考test_demo2文件夹下的  test_demo17.py


