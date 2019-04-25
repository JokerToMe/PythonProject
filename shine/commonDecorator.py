# 可以装饰任何函数
def outer(func):
    def inner(*args,**kwargs):
        # 添加修改的功能
        print('*************')
        return func(*args,**kwargs)
    return inner
# 参数的个数理论上是无限的，但最好不要超过6~7个
@outer
def say(name,age):
    print('%s is %d years old' % (name,age))
say('Shine',age=18)