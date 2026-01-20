# csv 文件的读写
# csv 文件的读取
# 1.创建一个csv文件 （已创建好file.csv)
# import csv
# with open('file.csv') as f:   # 打开文件，并创建一个csv写入对象
# # 2.获取csv读取器  (读取csv文件的第一行)
#     csv_reader = csv.reader(f)
#     headera = next(csv_reader)
#     print(headera)
# # 3.使用for 循环逐行遍历读取csv文件除了第一行以外的所有行
#     for line in csv_reader:
#         print(line)


###########################################
# csv 文件的写入
import csv
l1=[['1','2','3'],['4','5','6'],['7','8','9']]
l2=[['11','12','13'],['14','15','16'],['17','18','19']]
l3=[['21','22','23'],['24','25','26'],['27','28','29']]
# 1.打开文件 newline 这个参数如果不写的话，写入的csv文件会多出一行空行，写完后指定为空则不会有空行
with open('file8.csv','w',newline='') as f:
# 2.写入文件内容
    csv_writer = csv.writer(f,delimiter='*')  # delimiter 的作用是设置分隔符
    for line in l2:
        csv_writer.writerow(line)    # writerow 的作用是逐行写入数据
# -----------------------------------------------------------------------------
# 以上代码只能写进一行数据，如果想把l1,l2,l3的数据全部写入csv文件，则需要使用 writerows 方法

# 1.打开文件 newline 这个参数如果不写的话，写入的csv文件会多出一行空行，写完后指定为空则不会有空行
with open('file8.csv','w',newline='') as f:
# 2.写入文件内容
    csv_writer = csv.writer(f,delimiter='*')  # delimiter 的作用是设置分隔符
    for line in l2+l1+l3:
        csv_writer.writerow(line)    # writerow 的作用是逐行写入数据