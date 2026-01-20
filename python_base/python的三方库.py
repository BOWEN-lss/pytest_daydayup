"""
python安装第三方模块（三方库）
需要注意的是，在使用pip命令之前需要配置环境变量，把python安装路径下的scripts添加到环境变量中
常用命令
pip --version   # 查看pip版本
pip list    # 查看已安装的三方库列表
python -m pip install --upgrade pip # 升级pip
easy_install --upgrade pip # 升级pip

1.在线安装三方库
1.1.使用pip安装
pip install requests
安装指定版本
pip install requests==1.0.4
1.2.使用pip3安装
pip3 install requests

1.3.使用conda安装
conda install requests

1.4.使用pipenv安装
pipenv install requests

1.5.使用pipenv install -r requirements.txt安装多个三方库
pipenv install -r requirements.txt

1.6.使用pipenv install -e .安装本地三方库
pipenv install -e .

1.7.使用pipenv install -e .[dev]安装本地三方库和开发环境三方库

1.8 使用国内镜像安装
pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

2.升级三方库
pip install --upgrade requests

3.卸载三方库
pip uninstall requests

-----------------------------
离线安装三方库    离线包下载地址  https：//pypi.org/
分为.whl格式和.tar.gz格式
.whl格式安装方法：
1.将.whl文件放入python安装路径下的scirpt路径下
2.打开cmd窗口，cd 到script路径下
3.执行命令 pip install [文件名]
pip install requests-2.25.1-py2.py3-none-any.whl


.tar.gz格式安装方法:
1.下载并解压.tar.gz压缩包
2.cmd窗口，cd 到解压缩的位置
3.执行命令  python setup.py.install


--------------------------------

python项目依赖包整体迁移 （当我们需要把A电脑上的项目整体迁移到B电脑上时）
1.在原项目下生成requirements.txt文件  命令是 pip freeze >requirements.txt
2.依据requirements.txt文件下载离线包   命令是 pip download -r requirements.txt
离线包下载好后用U盘复制到B电脑的三方库安装位置，cmd命令cd 到这个路径下
3.在B电脑上安装所有离线包:
pip install --no-index --find-links=./ requirements.txt 
"""