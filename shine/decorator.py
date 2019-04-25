# 简单的装饰器
# 概念：装饰器是一个闭包，把一个函数当做参数，返回一个替代版的函数，本质上就是一个返回函数的函数
def fun1():
    print('hello,python')
def outer():
    print('**************')
    fun1()
# 在不修改fun1的情况下，通过outer函数增加代码来装饰fun1函数，所以称为装饰器
outer()
# outer函数中的fun1函数是写死的，所以outer函数只能作为fun1的装饰器，于是需要进行变形
def outer1(fun):
    print('**************')
    fun()
outer1(fun1)
# 再次变形
def outer2(fun):
    def inner():
        print('**************')
        fun()
    inner()
outer2(fun1)
# inner为装饰后的结果，最终作为返回值返回
def outer3(fun):
    def inner():
        print('**************')
        fun()
    return inner
# f为fun1装饰器的加强版本
f = outer3(fun1)
f()
# 函数在作为变量或者返回值的时候不写括号，只在调用的时候才加括号
