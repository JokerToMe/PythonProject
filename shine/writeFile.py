path = r'D:\ShineLaw\PythonProject\shine\file2.txt'

with open(path,'w') as f:
    # 将文件写入缓冲区
    f.write('hello,python')
    # 刷新缓冲区，把内部缓冲区的数据立刻写入文件，而不是被动的自动等待缓冲区刷新才写入
    # 缓冲区刷新的三种情况：
    # 1.手动刷新
    # 2.程序结束，缓冲区刷新
    # 3.缓冲区写满了，自动刷新
    # 使用with的时候不需要调用f.flush()方法也能刷新
    # f.flush()

# 追加数据
with open(path,'a') as f:
    f.write('\nhello,world')
