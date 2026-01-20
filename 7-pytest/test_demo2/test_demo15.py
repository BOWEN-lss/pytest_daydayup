# 1.skip 跳过执行测试函数
import pytest
# # 类外的测试用例
# @pytest.mark.skip(reason="没原因，就是不想执行这个用例") # 把skip装饰器放到类外的测试函数上，表示跳过这个测试用例，结果中该条用例显示为skipped
# def test_case01():
#     print("这是测试用例01")


# # 类内的测试用例
# class TestCase():
#     @pytest.mark.skip(reason="有原因，懒得执行这个用例")
#     def test_case02(self):
#         print("这是测试用例02")
#     @pytest.mark.skip(reason="有原因，领导不让执行这个用例")
#     def test_case03(self):
#         print("这是测试用例03")





# 2.skipif 跳过执行测试函数 当满足某个条件时，跳过执行测试函数 如果多个标签一起使用，则满足任意一个条件即可跳过
# 类外的测试用例
# @pytest.mark.skipif(condition=1>2,reason="开发完了，所以这个要测试") 
# @pytest.mark.skipif(condition=2>1,reason="没开发完呢，测个der啊")     # 这里有两个条件，满足第二个条件，所以跳过这个用例
# def test_case01():
#     print("这是测试用例01")


# 类内的测试用例

# class TestCase():
#     a='TMD,甩锅给我，老子不测了，跳过'
#     @pytest.mark.skipif(condition=2>1,reason="开发请假了，先跳过")     
#     def test_case02(self):
#         print("这是测试用例02")
#     @pytest.mark.skipif(condition=a !='',reason="胡乱甩锅，不爱测，跳过")    # 满足指定条件，跳过
#     def test_case03(self):
#         print("这是测试用例03")

# 3. 自定义 @pytest.mark.skip(reason="")标签
# myskip = pytest.mark.skip(reason="我就试试，其实这里不写也行")   # 自定义跳过标签
# myskip = pytest.mark.skipif(condition=1==1,reason="试试 skipif") 
# @myskip    # 使用自定义标签  这条案例会被跳过
# def test_case01():
#     print("这是测试用例01")



# class TestCase():
#     @myskip    # 在类的内部使用标签，这个也会被跳过
#     def test_case02(self):
#         print("这是测试用例02")

#     def test_case03(self):
#         print("这是测试用例03")


# 4.在函数内部使用 pytest.skip()方法跳过测试函数
    
# def test_case01():
#     pytest.skip("skip方法跳过测试用例")
#     print("这是测试用例01")

# class TestCase():
#     def test_case02(self):
#         pytest.skip("skip方法跳过测试用例")
#         print("这是测试用例02")
#     def test_case03(self):
#         print("这是测试用例03")

# 5.跳过测试类
# 在测试类上使用 @pytest.mark.skip()
# def test_case01():
#     print("这是测试用例01")
# @pytest.mark.skip('这个类下的测试用例都不用执行，我说的')
# @pytest.mark.skipif(condition=1==1,reason='条件满足，这个类下的测试用例都不用执行，我说的')
# class TestCase():
#     def test_case02(self):
#         print("这是测试用例02")
#     def test_case03(self):
#         print("这是测试用例03")

# 6.跳过测试模块
# pytestmark=pytest.mark.skip('这个模块下的测试用例都不用执行，我说的')  # 使用skip跳过整个模块（整个py文件下的所有用例）
# pytestmark=pytest.mark.skipif(condition=1==1,reason='条件满足，这个模块下的测试用例都不用执行，我说的')  # 使用skipif跳过整个模块（整个py文件下的所有用例）
# def test_case01():
#     print("这是测试用例01")

# class TestCase():
#     def test_case02(self):
#         print("这是测试用例02")
#     def test_case03(self):
#         print("这是测试用例03")


# 7.pytest.importorskip()模块导入失败时跳过

docutils = pytest.importorskip('docutils',minversion='1.0.3')  # 引入docutils模块失败时，跳过该模块
def test_case01():
    print("这是测试用例01")

class TestCase():
    def test_case02(self):
        print("这是测试用例02")
    def test_case03(self):
        print("这是测试用例03")