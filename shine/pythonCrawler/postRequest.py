# 特点：把参数进行打包，单独传输
# 优点：承载数据量大，安全（对服务器数据进行修改时建议使用POST）
# 缺点：速度慢

import urllib.request
# 对参数进行打包
import urllib.parse

url = 'http://www.baidu.com'
data = {
    'username': 'sunck',
    'password': '666'
}
headers = {
    'Accept':'application/json, text/plain, */*',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Content-Type':'text/html;charset=utf-8'
}
# 对要发送的数据进行打包，切记对调用urlencode方法之后一定要编码
postData = urllib.parse.urlencode(data).encode('utf-8')
# 创建请求体
req = urllib.request.Request(url,postData,headers)
# 请求
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))


