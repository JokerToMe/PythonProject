import urllib.request
import re
import ssl

def skirtCrawler(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    # print(data)
    # with open(toPath,'wb') as f:
    #     f.write(data)
    pat = r'<div style="position: relative">\n<img (src|original)="(.*?)/>\n</div>'
    reImage = re.compile(pat,re.S)
    imageList = reImage.findall(data.decode('utf-8'))
    print(len(imageList))
    for i,image in enumerate(imageList):
        # 写入文件路径
        toPath = str(i+1) + '.jpg'
        # 把图片下载到本地存储
        urli = 'https:'+image[1]
        print(urli)
        # urllib.error.HTTPError: HTTP Error 405: Not Allowed
        # reqi = urllib.request.Request(urli,headers=headers)
        # responsei = urllib.request.urlopen(reqi)
        # with open(toPath,'wb') as f:
        #     f.write(responsei.read())
        urllib.request.urlretrieve(urli,toPath)

url = 'https://search.yhd.com/c0-0/k%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599/'
toPath = r'skirt.html'
skirtCrawler(url)