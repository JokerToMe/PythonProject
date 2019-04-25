# 数据持久性模块
import pickle

path = r'D:\ShineLaw\PythonProject\shine\file3.txt'
list1 = [1,2,3,4,'hello']
with open(path,'wb') as f:
    pickle.dump(list1,f)
with open(path,'rb') as f:
    print(f.read())
    # 重置文件描述符
    f.seek(0)
    print(pickle.load(f))