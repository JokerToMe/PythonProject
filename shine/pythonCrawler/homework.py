import urllib.request
import re

def skirtCrawler(url,toPath):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    # print(data)
    # with open(toPath,'wb') as f:
    #     f.write(data)
    pat = r'<div style="position: relative">\n(.*?)\n</div>'
    reImage = re.compile(pat,re.S)
    imageList = reImage.findall(data.decode('utf-8'))
    print(len(imageList))
    for i in imageList:
        print(i)

url = 'https://search.yhd.com/c0-0/k%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599/'
toPath = r'skirt.html'
skirtCrawler(url,toPath)