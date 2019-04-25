# 编码
path = r'D:\ShineLaw\PythonProject\shine\file3.txt'

# 以二进制的形式写文件
with open(path,'wb') as f:
    f.write('shine law'.encode('utf-8'))

# 以二进制的形式读文件
with open(path,'rb') as f:
    data = f.read()
    print(data)
    print(type(data))
    # 当数据中没有中文的时候，使用gbk的格式解码也不会报错
    newData = data.decode('utf-8')
    print(newData)
    print(type(newData))

