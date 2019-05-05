# 抓取动态请求Ajax的数据

import urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    req = urllib.request.Request(url,headers=headers)
    # 使用ssl创建不用验证的上下文，经测试不用使用此上下文也能抓取https协议的数据
    ctx = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=ctx)
    data = response.read().decode('utf-8')
    # 根据需求返回一个字典
    return json.loads(data)

# https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=recommend&page_limit=20&page_start=0

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=recommend&page_limit=20&page_start=0'
dictData = ajaxCrawler(url)
print(dictData)
print(type(dictData))