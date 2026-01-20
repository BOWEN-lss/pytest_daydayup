# 文件的简单写入
# path = 'D:/xuelang_learn/test2.txt'   # 路径下没有这个文件时，这样写会自动创建这个文件
# # 1.打开文件
# f = open(path,'w',encoding='utf-8')
# # 2，写入内容
# f.write('随便写点啥把')
# # 3.关闭文件
# f.close()


# 使用with写入文件
with open('D:/xuelang_learn/test2.txt','w',encoding='utf-8') as f:
    f.write('随便写点啥')
    