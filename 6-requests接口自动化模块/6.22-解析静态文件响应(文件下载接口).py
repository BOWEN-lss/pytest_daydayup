"""
解析静态文件响应(文件下载接口) 当看到响应体信息中的content-type为text/plain时，说明该接口就是文件下载类的接口
静态资源文件是通过res.content属性获取的，通过open()函数写入文件
二进制的形式返回给客户端的，将二进制内容写入文本即可达到下载文件的效果

"""
import requests
url = 'http://httpbin.org/robots.txt'
response = requests.get(url)
#  print(response.status_code) # 输出响应状态码

# 获取响应内容
content = response.content
print(content)   # 输出响应内容  b'User-agent: *\nDisallow: /deny\n' 说明响应内容是二进制内容

# 将二进制内容写入文件
with open('6.22-robots.txt', 'wb') as f:   #在当前路径下新建 6.22-robots.txt 文件并把content获取到的二进制内容写入文件中 open 打开文件,如果要打开的文件不存在会自动创建  wb表示以二进制写入   
    f.write(content) # 写入文件