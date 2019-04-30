# 一个.py文件就是一个模块

TT = 100

def sayGood():
    print('good')

def sayNice():
    print('nice')

def sayHandsome():
    print('handsome')

print('当做模块使用时会被执行')

# 每一个模块都有一个__name__属性，当等于__main__时，表示自身在执行
if __name__ == '__main__':
    print('作为模块使用时不希望被执行')