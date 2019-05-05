import urllib.request

# 如果网页长时间未响应，系统判断超时，无法爬取
for i in range(100):
    try:
        response = urllib.request.urlopen('http://www.baidu.com',timeout=0.2)
        data = response.read().decode('utf-8')
        print(len(data))
    except:
        print('请求超时，爬取下一个地址')