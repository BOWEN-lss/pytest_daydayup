"""
接口自动化实现图片壁纸爬虫
"""
import requests
import os  # 导入操作系统模块
if not os.path.exists('./picture_download'):  # 判断当前路径下pic文件夹是否存在 （当前路径指的是项目所在的路径）
    os.mkdir('./picture_download')  # 创建pic文件夹
# if not os.path.exists('D:/python_learn/6-requests接口自动化模块/picture_download'):   # 不想用当前路径的话可以用绝对路径指定
#     os.mkdir('D:/python_learn/6-requests接口自动化模块/picture_download')
from lxml import etree  # 导入HTML解析中的etree模块
url  = 'https://pic.netbian.com/4kyouxi'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 QuarkPC/6.1.0.653'
           ,'Referer': 'https://pic.netbian.com/4kyouxi'}
res=requests.get(url,headers=headers,verify=False)  # 忽略证书验证
res.encoding = 'gbk'  # 设置编码格式，防止乱码
page_info=res.text  # 到这一步已经拿到了页面中全部的图片信息

# 解析响应体（页面标签结构）当响应体的格式为HTML时，可以使用HTML解析器对响应体进行解析
html = etree.HTML(page_info)  # 把text格式的page_info转换成HTML对象
li_list = html.xpath('//ul[@class="clearfix"]/li')  # 获取页面元素中所有的li标签
for li in li_list:    # 遍历li标签中所有的元素对象
    full_path = 'https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]  # 获取图片的src属性值+完整路径拼接
    name=li.xpath('./a/b/text()')[0]+'.jpg'  # 获取图片名称且手动拼接图片格式
    res=requests.get(full_path,headers=headers,verify=False).content  # 获取图片的二进制数据  .content就是图片的二进制数据
    with open('./picture_download'+'/'+name,'wb') as f:
        f.write(res)
        print(name+'下载完成')

# 批量下载图片完成，但是大小只有1K，且不可查看，暂时未找到原因


# =========================================
# 高清原图下载尝试--未成功
# =========================================
# import os
# import requests
# from lxml import etree
# import urllib3

# urllib3.disable_warnings()

# # =========================
# # 【★★需要你确认/替换★★】1. 列表页 URL
# # =========================
# LIST_URL = 'https://pic.netbian.com/4kmeinv/'

# # =========================
# # 【★★需要你确认/替换★★】2. 高清原图接口模板
# # =========================
# DOWNPIC_API = 'https://pic.netbian.com/e/extend/downpic.php?id={}'

# # =========================
# # 3. 请求头（可直接用）
# # =========================
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#     'Referer': 'https://pic.netbian.com/'
# }

# # =========================
# # 4. 图片保存目录
# # =========================
# SAVE_DIR = 'images'
# os.makedirs(SAVE_DIR, exist_ok=True)

# # =========================
# # 5. 请求列表页
# # =========================
# res = requests.get(LIST_URL, headers=HEADERS, verify=False)
# res.encoding = 'gbk'   # ⚠️ pic.netbian 是 gbk 编码
# html = etree.HTML(res.text)

# # =========================
# # 【★★需要你确认/替换★★】6. 壁纸详情页链接 XPath
# # =========================
# detail_urls = html.xpath('//ul[@class="clearfix"]/li/a/@href')

# print(f'共解析到 {len(detail_urls)} 个详情页')

# # =========================
# # 7. 遍历详情页
# # =========================
# for detail_url in detail_urls:
#     detail_url = 'https://pic.netbian.com' + detail_url
#     detail_res = requests.get(detail_url, headers=HEADERS, verify=False)
#     detail_res.encoding = 'gbk'
#     detail_html = etree.HTML(detail_res.text)

#     # =========================
#     # 【★★需要你确认/替换★★】8. 图片 ID XPath
#     # =========================
#     img_id_list = detail_html.xpath('//div[@class="downpic"]/a/@data-id')

#     if not img_id_list:
#         print('❌ 未获取到图片 ID，跳过')
#         continue

#     img_id = img_id_list[0]
#     print(f'开始下载 ID={img_id}')

#     # =========================
#     # 9. 请求高清原图接口
#     # =========================
#     down_url = DOWNPIC_API.format(img_id)
#     down_res = requests.get(
#         down_url,
#         headers=HEADERS,
#         verify=False,
#         allow_redirects=True
#     )

#     content_type = down_res.headers.get('Content-Type', '')

#     # =========================
#     # 10. 情况一：直接返回图片（二进制）
#     # =========================
#     if content_type.startswith('image'):
#         img_content = down_res.content

#     # =========================
#     # 11. 情况二：返回 HTML / JS，需要再解析
#     # =========================
#     else:
#         down_html = etree.HTML(down_res.text)
#         img_src_list = down_html.xpath('//img/@src')

#         if not img_src_list:
#             print('❌ 未解析到 img 标签，跳过')
#             continue

#         img_src = img_src_list[0]
#         img_url = img_src if img_src.startswith('http') else 'https://pic.netbian.com' + img_src

#         img_content = requests.get(
#             img_url,
#             headers=HEADERS,
#             verify=False
#         ).content

#     # =========================
#     # 12. 保存图片
#     # =========================
#     file_path = os.path.join(SAVE_DIR, f'{img_id}.jpg')
#     with open(file_path, 'wb') as f:
#         f.write(img_content)

#     print(f'✅ 下载完成：{file_path}')


