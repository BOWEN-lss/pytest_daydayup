"""
pytest执行用例的多种运行方式
一、通过IDE运行
直接点击测试用例左侧的绿色三角运行


二、通过命令行运行
pytest test_demo19.py -s -v -n

pytest -s test_demo.py  #显示代码中的print或日志打印
pytest -v test_demo.py  #显示用例详情
pytest -q test_demo.py  #简化显示，与-v相反
pytest --collect-only test_demo.py       #检查哪些测试用例会被运行
pytest -k "not 02" test_demo.py        #选择用例运行,可以用not,or
pytest -x test_demo.py           #遇到失败用例自动停止运行
pytest --maxfail=2 test_demo.py        #达到最大失败数自动停止运行

pytest --tb=short test_demo.py         #失败信息的显示方式,三个固定值
short: 仅输出assert 的一行以及系统判定的内容；
line : 只使用一行输出显示所有的错误信息；
no : 屏蔽所有的回溯信息

pytest -m "markname" test_demo.py     #指定标签名运行，配合前面讲的mark标签装饰器
pytest -n 3 test_demo.py           #分布式运行，指定3个进程，配合前面讲的xdist插件
pytest --reruns 3 --reruns-delay 1 test_demo.py    #失败重复运行3次，每次1s间隔，配合前面讲的pytest-rerunfailures插件
pytest --html=report.html --self-contained-html test_demo.py  #输出测试报告，配合前面讲的pytest-html插件
pytest --alluredir ./result/ test_demo.py      #输出allure报告数据到result目录，配合前面讲的allure-pytest插件

指定用例运行
pytesty -s testsuit   # 指定文件夹下所有用例运行
pytesty -s testsuit/test_demo02.py   # 运行指定文件下所有用例
pytest -s test_demo.py::Test_case  # # 运行指定文件下指定测试类下的用例
pytest -s test_demo.py::Test_case：：Test_case01  # 运行指定文件下指定测试类下的指定测试案例


三、通过pytest.main()函数运行
pytest.main(['-s', '-v', 'test_demo.py'])

四、通过pytest.ini运行
pytest.ini 运行是优先级最高的一种运行方式，可以改变pytest 的默认运行方式
存放位置：一般在项目的根目录下
编码格式：必须是ANSI编码格式，可以使用notepad++修改编码格式
pytest.ini文件中尽量不要有中文，容易出问题
配置了ini文件后，不管哪种方法运行测试用例，都会在运行前去读取ini文件中的配置信息
可以使用  pytest -h 查看pytest的帮助信息
常用参数：
addopts = -s -v    命令行参数，用空格分隔
testpath = ./   测试路径，默认为当前目录
markers 标记参数  赋值方式为key:value

markers = 
smoke: 冒烟用例
login: 登录用例

python_files = *.py  模块的命名规则
pyhton_classes = Test*   类的命名规则
python_functions = test*   方法的命名规则
"""


import pytest
class Test_case01:
    def test_case01(self):
        print("用例01")

    def test_case02(self):
        print("用例02")

    def test_case03(self):
        print("用例03")

    def test_case04(self):
        print("用例04")
if __name__ == '__main__':
    pytest.main(['-s', '-v', '7.19pytest执行用例的多种运行方式.py'])

