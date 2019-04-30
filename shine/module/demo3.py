# from ... import ... 从模块中引入一个指定的部分

from law import sayGood,sayNice

# 会覆盖模块中引入的方法
def sayGood():
    print('*****************')

sayGood()
sayNice()