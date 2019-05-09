def run():
    # 存储作用
    data = ''
    r = yield data
    print(1,r,data)
    r = yield data
    print(2,r,data)
    r = yield data
    print(3,r,data)
    r = yield data

m = run()
# 启动m
print(m.send(None))
print(m.send('a'))

