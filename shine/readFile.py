"""
步骤：
1.打开文件
函数：
open(path,flag[,encoding][,errors])
path:要打开文件的路径
flag:打开方式
r:以只读的方式打开，文件的描述符放在文件的开头
rb:以二进制方式打开文件用于只读
r+:打开一个文件用于读写
w:打开一个文件只用于写入，如果该文件已存在则会覆盖，如果文件不存在则创建新文件
wb:打开一个文件只用于写二进制
w+:打开一个文件用于读写
a:打开一个文件用于追加，如果文件存在，文件描述符将会放在末尾
a+:打开一个文件用于读写，如果文件存在，文件描述符将会放在末尾
encoding:编码格式
errors:错误处理

2.读取文件
3.关闭文件
"""

path = r'D:\ShineLaw\PythonProject\shine\file1.txt'
# f = open(path,'r',encoding='utf-8',errors='ignore')
# f = open(path,encoding='utf-8')

# 读取文件全部内容，适合读小文件
# str1 = f.read()
# print(str1)

# 读取指定指定长度的字符串
# str1 = f.read(20)
# print('*'+str1+'*')

# 读取整行
# str1 = f.readline()
# print(str1)

# 读取所有行并返回列表
# list1 = f.readlines()
# print(list1)

# 过给定的数字大于0，返回实际size字节的行数，此方法很少使用
# list2 = f.readlines(42)
# print(list2)

# 修改文件描述符的位置
# print('***************')
# f.seek(12)
# str2 = f.read()
# print(str2)
# f.close()

# 一个完整的过程
try:
    f = open(path,'r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()
