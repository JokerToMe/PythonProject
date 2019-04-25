# 在不修改源码的基础上完善代码功能
# def say(age):
#     print('Shine is %d years old' % age)

# 此装饰器只实用于参数只有一个且必须为number类型的函数，不通用
def outer(func):
    def inner(age):
        if age <=0:
            age = 0
        func(age)
    return inner
# 通过@符号来替代 say = outer(say) 的写法
@outer
def say(age):
    print('Shine is %d years old' % age)

say(-10)

# f = outer(say)
# f(-9)
