# class Test_demo():
#     def test_login_case01(self):
#         """正确的用户名和密码"""
#         print("输入的用户名：admin")
#         print("正确的密码：123456")
#         print("点击登录")
    
#     def test_login_case02(self):
#         """正确的用户名和错误的密码"""
#         print("正确的用户名：admin")
#         print("错误的密码：123456789")
#         print("点击登录")
#         print("登录失败")

#     def test_login_case03(self):
#         """错误的用户名和正确的密码"""
#         print("错误的用户名：adn")
#         print("正确的密码：123456")
#         print("点击登录")
#         print("登录失败")
# 生成测试报告大小只有2kb，从本地用浏览器打开后报告为空  但是用 allure open./report 命令打开后显示正常   不太理解


# 在基础测试报告上增加自定义内容
# 一、step  --增加测试步骤  用来给测试报告上的用力增加步骤描述
# 语法：
# 方式一：写在函数上方    @allure.step("测试步骤描述")
import allure
@allure.step("输入用户名")
def input_username(username):
    print(f'输入的用户名：{username}')

@allure.step("输入密码")
def input_password(password):
    print(f'输入的密码：{password}')

@allure.feature("登录模块")   # 添加模块描述后可以在allure测试报告 behaviors(功能)  下显示
class Test_demo():
    @allure.story("登录成功")   # 添加功能描述后可以在allure测试报告 behaviors(功能)  下的测试用例中显示
    @allure.link("https://api.example.com/auth", name="官方文档")  
    @allure.issue("http://www.baidu.com", name="登录页面偶尔出现空白")  # 把url地址换成提交bug所用的工具的链接，如禅道，jira等
    @allure.testcase("https://api.example.com/auth", name="登录功能测试用例")  # 这三个装饰器添加后可以在allure测试报告 behaviors(功能)  下的测试用例详细信息中显示

    def test_login_case01(self):
        """正确的用户名和密码"""
        input_username('admin')
        input_password('123456')
        print("点击登录")
    @allure.description("这是测试用例2的描述信息")   # 添加描述信息后可以在allure测试报告 behaviors(功能)  下的测试用例详细信息-description 中显示  图表中也会显示
    @allure.story("正确的用户名和错误的密码")
    def test_login_case02(self):
        """正确的用户名和错误的密码"""
        # 方式二：写在函数内部   with allure.step("测试步骤描述")
        with allure.step("输入用户名"):
            print("正确的用户名：admin")
        with allure.step("输入密码"):
            print("错误的密码：123456789")
        print("点击登录")
        print("登录失败")
    @allure.severity('critical')  # 设置缺陷等级  在测试报告中的用例详情中会详细展示
    @allure.story("错误的用户名和正确的密码")
    def test_login_case03(self):
        """错误的用户名和正确的密码"""
        print("错误的用户名：adn")
        print("正确的密码：123456")
        print("点击登录")
        print("登录失败")
    
    def test_login_case04(self):
        """错误的用户名和错误的密码"""
        print("错误的用户名：adn")
        print("正确的密码：1236")
        print("点击登录")
        allure.attach("这是测试用例4的附加信息", "附加信息", allure.attachment_type.TEXT)   # 添加附加文本信息
        allure.attach.file(source='./pic.png', name="图片展示", attachment_type=allure.attachment_type.PNG)  # 添加图片信息
        allure.attach(body='html展示', name="html信息", attachment_type=allure.attachment_type.HTML) # 添加html信息
    
# 重新生成测试报告后在 测试套--测试信息--执行--测试步骤中就会多出自定义的步骤描述

# 二、feature  测试用例特性（给主要功能模块/类，增加描述信息，写在类方法上方）

# 三、story  测试用例功能（给功能模块，增加描述信息，写在方法上方）

# 四、link/issue/testcase  链接测试用例 
# 语法：
# @allure.link("http://www.baidu.com", name="百度")    一般用来指向 文档 URL、官网地址
# @allure.issue("http://www.baidu.com", name="百度")   用来指向测试问题 URL
# @allure.testcase("http://www.baidu.com", name="百度")  用来指向测试用例 URL

# 五、description  给测试用例增加描述 语法：@allure.description("这是测试用例的描述信息")  写在函数上方

# 六、severity  测试用例的严重程度  语法：@allure.severity(allure.severity_level.CRITICAL) 或者 @allure.severity("critical")  第二种常用  写在函数上方
# 分为以下五个等级
# BLOCKER 阻断缺陷，最高优先级，会影响整个系统或导致系统无法正常工作，必须立即修复才能继续测试
# CRITICAL 严重/临界缺陷，高优先级，主要功能失效，严重影响用户体验，需要尽快修复
# NORMAL 一般缺陷，中等优先级，功能存在缺陷但不影响核心使用，标准的功能测试用例通常使用此缺陷
# MINOR 次要缺陷，低优先级，用户界面小问题或轻微功能瑕疵，对系统整体影响较小
# TRIVIAL 轻微缺陷，最低优先级，很小的问题，如拼写错误、样式调整等，通常不需要紧急修复
# 不指定级别默认为normal

# 七、attach  添加附加信息，通常是一些测试数据信息  在测试函数内部使用
# 语法：
# allure.attach(body, name, attachment_type, extension)
# allure.attach.file(source, name, attachment_type,extension)

# 参数：
# body：要写入文件的原始内容
# name：文件名
# attachment_type：文件类型
# extension：文件扩展名

# 测试用例中添加文本、图片、html信息





