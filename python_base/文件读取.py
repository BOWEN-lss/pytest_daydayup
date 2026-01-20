# 打开文件
# f = open('test.txt','r+',encoding='utf-8')
# txt=f.readline(8)
# print(txt)
# f.close()

# with open('test.txt','r+',encoding='utf-8') as f:
#     print(f.readlines()[2:5])    # 取指定行数

# for 循环读取
with open('test.txt','r+',encoding='utf-8') as f:
    for line in f:
        print(line.strip())
