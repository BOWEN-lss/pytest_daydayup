"""
pytest模块介绍和安装
"""
# 模块介绍
"""
pytest模块是一个用于测试的模块,非常容易上手，入门简单，文档丰富，有很多实例可以参考
能够支持简单的单元测试和复杂的功能测试
支持参数化
支持跳过某些案例或者对预期失败的案例进行打标
支持重复执行失败的案例
支持运行有unittest编写的案例
支持很多第三方插件且支持自定义插件 
方便和持续集成工具集成

pytest模块安装:

常用 pip 命令速查表（接口自动化 / Python 日常必备）

一、安装与卸载 
pip install requests # 安装 requests 
pip install pytest==8.3.2 # 安装指定版本 
pip uninstall pytest # 卸载 pytest

二、查看 
pip list # 查看已安装包 
pip show pytest # 查看指定包详情 
pip list | findstr pytest   # Windows 下查看某个包版本

三、升级 
python -m pip install –upgrade pip # 升级 
pip pip list –outdated # 查看可升级的包

四、依赖管理 
pip freeze # 导出依赖 
pip freeze > requirements.txt # 生成requirements.txt 
pip install -r requirements.txt # 按文件安装依赖

五、环境定位（非常重要） 
pip –-version  # 查看pip版本和路径


六、镜像相关 
pip install pytest -i
https://pypi.tuna.tsinghua.edu.cn/simple pip config set global.index-url
https://pypi.tuna.tsinghua.edu.cn/simple

七、离线安装 
想到python的三方库官方网站pypi.org下载对应whl文件
pip install xxx.whl pip install –no-index –find-links=.requests

"""
