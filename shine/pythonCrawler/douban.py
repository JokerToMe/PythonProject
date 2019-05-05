# urllib爬取网页

import urllib.request

# 向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
urlBaidu = r'http://www.baidu.com'
# 编码
url1 = urllib.request.quote(urlBaidu)
# 解码
url2 = urllib.request.unquote(url1)
response = urllib.request.urlopen(url2)
# 读取文件的全部内容
# data = response.read()
# print(data)
# print(type(data))

# 读取一行
# data = response.readline()

# 推荐使用这种读取方式
# 读取文件的全部内容，把读取到的数据复制给一个列表变量
data = response.readlines()
# print(data)
# print(type(data))
# print(len(data))
# print(type(data[100]))

# 将爬取到的网页写入文件
# with open('file.html','wb') as f:
#     f.write(data)

# response常用属性
# 返回当前环境的有关信息
print(response.info())
# 返回状态码 500以上：服务器问题  400以上：访问出错 300以上：缓存相关 200以上：成功
print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
#     # 开始处理网页信息
#     pass
# 正在爬取的url地址
print(response.geturl())
url = r'https://www.baidu.com/s?wd=%E8%B1%86%E7%93%A3&rsv_spt=1&rsv_iqid=0xf210c540000d5970&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100'
# url解码
newUrl = urllib.request.unquote(url)
print(newUrl)
# url编码
print(urllib.request.quote(newUrl))

