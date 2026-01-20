def demo ():
    print(__name__)
# demo()   # 在本模块调用自定义函数时，__name__等于__main__

# 但是如果本自定义模块在其他模块中被调用时，__name__等于当前文件的模块名
if __name__ == '__main__':
    demo()