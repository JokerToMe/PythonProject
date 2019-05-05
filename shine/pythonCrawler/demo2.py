import urllib.request

urllib.request.urlretrieve(r'http://www.baidu.com',filename=r'file2.html')
# urlretrieve在执行的过程中会产生缓存
# 清除缓存
urllib.request.urlcleanup()