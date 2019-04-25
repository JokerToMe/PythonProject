# 函数就是对功能的封装
# 1.简化代码结构，增加代码复用
# 2.如果想修改某些功能，只需修改对应的函数即可

"""
格式：
def 函数名(参数列表):
    语句
    return 表达式
"""

# 值传递：传递的不可变类型，string tuple number
def fun1(num):
    num = 1

temp = 0
fun1(temp)
print(temp)

# 引用传递
def fun2(l):
    l[0] = 1

list1 = [0,2,3]
fun2(list1)
print(list1)

# 关键字参数
def fun3(str,age):
    print(str,age)

fun3(str='shine',age=18)

# 默认参数
def fun4(str,age=18):
    print(str,age)

fun4('shine')

# 不定长参数：加了*的参数会接收所有未命名的变量参数，参数实质为一个tuple
def func5(*args):
    print(type(args))
    for arg in args:
        print(arg)

func5('shine','law')

def sum(*attr):
    sum = ''
    for a in attr:
        print(a)

sum(1,2,'sum')

# 不定长关键字参数
def func6(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print('%s:%s' %(k,v))

func6(x='1',y='2')