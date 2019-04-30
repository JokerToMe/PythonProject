# 装饰器定义：用来装饰其他函数的函数，表现形式为，把一个函数作为参数传入，经过代码修饰后，返回一个在原有函数基础上添加新功能的函数
# 一种特殊的闭包
# 装饰器变型过程
# 场景：在一个函数执行前加一段打印语句

import functools

# 只适用于func1的装饰器
def func1():
    print('shine is a gentleman')

def outer1():
    print('****************')
    func1()

outer1()

# 变形，适用于不带参数的任意函数，把函数作为参数传递进去
def outer2(func):
    print('****************')
    func()

outer2(func1)

# 再次变形，让outer函数返回一个函数
def outer3(func):
    def inner():
        print('****************')
        func()
    return inner

outer3(func1)()

# 再次变形，让inner返回一个函数
def outer4(func):
    def inner():
        print('****************')
        return func
    return inner

outer3(func1)()

# 可以传递参数的装饰器
def outer5(func):
    def inner(arg):
        print('****************')
        return func(arg)
    return inner

def func2(arg):
    print('%s is a gentleman' % arg)

f = outer5(func2)
f('test')

# 再次变形，可以装饰任意函数的万能装饰器
def outerCommon(func):
    def inner(*args,**kwargs):
        # pass
        print('****************')
        return func(*args,**kwargs)
    return inner

f = outerCommon(func2)
f('test')

# 调用变形
@outerCommon
def func3(arg):
    print('%s is very nice' % arg)

func3('nick')

# 偏函数：给函数的某些参数设置默认值
# 示例
# 第一个参数为函数名，第二个参数为要指定的参数的默认值
int2 = functools.partial(int,base=2)
print(int2('1010'))
