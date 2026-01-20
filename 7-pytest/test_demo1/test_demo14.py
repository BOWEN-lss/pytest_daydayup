# parametrize 与其他mark一起使用

import pytest
a='跳过'
@pytest.mark.parametrize("x,y",[('test1',123456),
                               pytest.param('test1',123456,marks=pytest.mark.xfail),
                               pytest.param('test1',123456,marks=pytest.mark.xfail),
                               pytest.param('test2',123456,marks=pytest.mark.skip('跳过')),
                               pytest.param('test3',123456,marks=pytest.mark.skipif(a=='跳过',reason='有条件的跳过'))])

def  test_one(x,y):
    assert x=='test1'
    assert y==123456

# 执行结果如下：
# test_demo14.py::test_one[test1-123456_0] PASSED   第一个用例通过
# test_demo14.py::test_one[test1-123456_1] XPASS    XPASS = "意外通过"，期望测试失败（xfail），但实际测试通过了
# test_demo14.py::test_one[test1-123456_2] XPASS    XPASS = "意外通过"，期望测试失败（xfail），但实际测试通过了
# test_demo14.py::test_one[test2-123456] SKIPPED (跳过)  使用了 pytest.mark.skip('跳过') 直接跳过测试
# test_demo14.py::test_one[test3-123456] SKIPPED (有条件的跳过)  满足条件 跳过测试