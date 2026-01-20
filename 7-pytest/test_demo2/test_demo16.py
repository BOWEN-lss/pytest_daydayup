import pytest
# @pytest.mark.xfail(condition=1>2,reason='不满足条件，用例1执行结果为pass')
# @pytest.mark.xfail(condition=1>0.2,reason='满足条件，这时候的结果为不符合预期的通过xpass')
# @pytest.mark.xfail(condition=1>0.2,reason='满足条件，这时候用例1的结果为符合预期的faild',strict=True)
# def test_xfail():
#     print("用例1执行完毕")


# # 用在类内部的效果也是一样
# class TestDemo():
#     # @pytest.mark.xfail(condition=1>2,reason='不满足条件，用例2执行结果为pass')
#     # @pytest.mark.xfail(condition=1>0.2,reason='满足条件，这时候的结果为不符合预期的通过xpass')
#     @pytest.mark.xfail(condition=1>0.2,reason='满足条件，这时候用例1的结果为符合预期的faild',strict=True)
#     def test_xfail1(self):
#         print("用例2执行完毕")
#         assert False  # 断言为false 使用ini文件后这条用例会被忽略
#     def test_xfail2(self):
#         print("用例3执行完毕")


# 使用ini文件  使所有预期失败，但是测试结果不为faild的用例 执行结果标记为faild

@pytest.mark.xfail(condition=21>2,reason='满足条件，这时候用例1的结果为符合预期的faild')
def test_xfail():
    print("用例1执行完毕")

class TestDemo():
    @pytest.mark.xfail(condition=21>2,reason='满足条件，这时候用例2的结果为符合预期的失败xfail，因为我们加了断言')
    def test_xfail1(self):
        print("用例2执行完毕")
        assert False 
    @pytest.mark.xfail(condition=21>2,reason='满足条件，这时候用例3的结果为符合预期的faild')
    def test_xfail2(self):
        print("用例3执行完毕")