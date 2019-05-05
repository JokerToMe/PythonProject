# 爬取糗事百科数据

import urllib.request
import re

def qiushiCrawler(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    print(type(data))
    # with open(r'qiushi.html','w') as f:
    #     f.write(data)
    # 通过正则表达式处理页面，.匹配出换行以外的任意字符，由于字符串中存在换行，第一行匹配失败后会从下一行开始匹配，故匹配失败，加上re.S后，.也可以匹配换行
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    reJoke = re.compile(pat,re.S)
    divList = reJoke.findall(data)
    # print(divList)
    print(len(divList))
    finalList = []
    for div in divList:
        dict = {}
        # 用户名
        reName = re.compile(r'<h2>(.*?)</h2>',re.S)
        dict['userName'] = reName.findall(div)[0]
        # 段子
        reDuan = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)
        dict['duanzi'] = reDuan.findall(div)[0]
        finalList.append(dict)
    print(finalList)

url = 'https://www.qiushibaike.com/text/page/2/'
info = qiushiCrawler(url)