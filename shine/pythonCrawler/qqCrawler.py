import urllib.request
import os
import re

def writeFileBytes(htmlBytes,toPath):
    with open(toPath,'wb') as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,toPath):
    with open(toPath, 'w') as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read()

def qqCrawler(url):
    data = getHtmlBytes(url)
    writeFileBytes(data,'qqFileBytes.html')

    # 查找所有的qq
    # [1-9]：数字1-9开头，{4,9}位数4到9位 总位数是5-10位
    # pat = r'[1-9]\d{4,9}'
    # reQQ = re.compile(pat)
    # qqList = reQQ.findall(data.decode('utf-8'))
    # # 去重
    # print(list(set(qqList)))
    # print(len(qqList))

    # 查找网址
    pat = r'^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)'
    urlList = re.findall(pat,data.decode('utf-8'))
    print(urlList)


url = r'https://www.douban.com/group/topic/110094603/'
qqCrawler(url)