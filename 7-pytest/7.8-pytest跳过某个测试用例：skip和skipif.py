"""
pytest跳过某个测试用例：skip和skipif
使用场景：
1.当功能还未开发完成，但是用例已经写完，没有必要测试，此时就可以使用skip跳过该用例
2.新增功能测试，旧的功能没有改动，没有必要测试，此时就可以使用skipif跳过该用例
"""

# 1.skip 跳过执行测试函数
# 语法：@pytest.mark.skip(reason="")  # reason非必填，为跳过原因

# 2.skipif 当满足某个条件时，跳过执行测试函数 如果多个标签一起使用，则满足任意一个条件即可跳过
# 语法：@pytest.mark.skipif(condition, reason="")

# 3.自定义@pytest.mark.skip()标签
# 语法：myskip = pytest.mark.skip(reason="")  或者 myyskip = pytest.mark.skipif(condition, reason="")

# 4.使用 pytest.skip()方法跳过测试函数
# 语法：pytest.skip("这里写原因")  # 写在函数内部，括号内非必填，为跳过原因

# 5.跳过测试类
# 语法：@pytest.mark.skip() 或者 @pytest.mark.skipif(condition, reason="")
# 其实和跳过测试方法一样，用它装饰类就好 

# 6.跳过测试模块
# 语法：pytestmark=pytest.mark.skip(condition, reason="")
# 注意：pytestmark不能改名，就必须叫pytestmark

# 7.pytest.importorskip()模块导入失败时跳过
# 当引入某个模块失败时，跳过测试用例
# 语法：pytest.importorskip('模块名')  # 引入某个模块失败时，跳过测试用例
# pytest.importorskip('模块名', minversion="1.0.3")  # 引入某个模块失败时，跳过测试用例，并且指定模块的版本

# 实例参考test_demo2文件夹下的  test_demo15.py