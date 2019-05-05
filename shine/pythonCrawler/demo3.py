# 模拟浏览器访问
import urllib.request
import random

url = 'http://www.baidu.com'

# 模拟请求头，反爬虫
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# 设置一个请求体
# req = urllib.request.Request(url,headers=headers)
# 发起请求
# response = urllib.request.urlopen(req)
# data = response.read().decode('utf-8')
# print(data)

agentList = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
]
# 通过随机User-Agent来防止封锁ip
agentStr = random.choice(agentList)

# req = urllib.request.Request(url)
# req.add_header('User-Agent',agentStr)
# 设置完整的请求头
headers = {
    'Accept':'application/json, text/plain, */*',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': agentStr,
    'Content-Type':'text/html;charset=utf-8'
}
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)