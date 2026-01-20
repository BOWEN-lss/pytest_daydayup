import pytest
import allure
def test_success():
    print("success")
    assert True

def test_fail():
    print("fail")
    assert False

def test_skip():
    pytest.skip("no reason,just wang to skip")


def test_broken():
    pytest.Exception("有问题了个屁的了")

# 生成aluure测试报告
# 第一步：生成测试报告数据
# 在pytest执行测试的时候，指定 --aluuredir 选项及结果数据保存的路径  
# pytest test_demo_allure.py  --alluredir ./result -v   要先有result这个文件夹
# 这一步完成后会在result文件夹下生成allure测试报告的原始数据（json格式的文件）

# 第二步：生成测试报告的页面   需要在当前路径或者指定路径新建一个文件夹 report  用来存放测试报告
# allure generate ./result -o ./report --clean  # 需要注意的是./result是生成测试报告数据的路径，./report 是生成测试报告页面的路径 --clean表示清理之前生成的测试报告数据D:\python_learn\allure-result

# 第三步：打开测试报告页面
# allure open ./report