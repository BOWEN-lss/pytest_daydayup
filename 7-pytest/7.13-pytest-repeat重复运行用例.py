"""
pytest-repeat重复运行用例

插件安装：pip install pytest-repeat
插件使用：方式：
1.用命令行执行  
pytest --count=3 --repeat-scope=class test_demo19.py -s -v
--count=3 是重复运行次数
-s 是显示用例执行过程  -v 是显示详细日志
--repeat-scope的参数有funnction'、'class'、'module'、'session' 默认为function  用来控制用例重复执行时机
2.用装饰器执行
语法：@pytest.mark.repeat(3)


案例参考test_demo2文件夹下的test_demo21.py
"""