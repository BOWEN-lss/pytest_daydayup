# pytets-assume多重断言

import pytest
class TestDemo:
    def test_case1(self):
        print ("开始执行用例1")
        assert False,'用例1第一次断言失败'  
        assert False,'用例1第二次断言失败'

# 运行结果如下：
# collected 1 item

# test_demo22.py::TestDemo::test_case1 开始执行用例1
# FAILED
# 结果中可以看出第一次断言失败后直接抛出AssertionError异常，导致第二次断言不再执行
# 要想让第一次断言失败后继续执行第二次断言，可以使用pytest.assume进行多重断言

    def test_case2(self):
        print ("开始执行用例2")
        pytest.assume(1>2,'用例2第一次断言失败')
        pytest.assume(False,'用例2第二次断言失败')
        pytest.assume(2>1,'用例2第三次断言成功')
        print ("用例2执行完毕")

# 运行结果如下：
# test_demo22.py::TestDemo::test_case1 开始执行用例1
# FAILED
# test_demo22.py::TestDemo::test_case2 开始执行用例2
# 用例2执行完毕
# test_demo22.py:20: AssumptionFailure
#   >>    pytest.assume(1>2,'用例2第一次断言失败')
#   AssertionError: 用例2第一次断言失败
#   assert False

#   test_demo22.py:21: AssumptionFailure
#   >>    pytest.assume(False,'用例2第二次断言失败')
#   AssertionError: 用例2第二次断言失败
#   assert False

#     lambda: runtest_hook(item=item, **kwds),

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ============================================================= short test summary info ==============================================================
# FAILED test_demo22.py::TestDemo::test_case1 - AssertionError: 用例1第一次断言失败                                                   ================ 
# FAILED test_demo22.py::TestDemo::test_case2 - pytest_assume.plugin.FailedAssumption:
# FAILED


# 从结果可以看出，即使第一次断言失败，第二次断言也会被执行
# pytest.assume 允许用例完整执行，但只要存在失败断言，用例最终仍然会被判定为 FAILED