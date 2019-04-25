# 当程序遇到问题时不让程序结束，而越过错误，继续向下执行
# 应用场景：爬虫时测试账号登录，如出现异常继续执行
"""
格式：try:
        语句1
    except 错误码 as e:
        捕获错误后的执行语句1
    except 错误码 as e:
        捕获错误后的执行语句2
    ....
    except 错误码 as e:
        捕获错误后的执行语句n
    else:
        没有捕获到错误执行的语句
注：else语句可有可无
1.语句1出现错误，程序会从上到下逐一匹配错误码，匹配成功后执行对应的语句
2.出现错误却没有匹配到到对应的错误码，错误将会被提交到上一层的try语句，或者程序的最上层
3.没有出现错误，执行else分支后的语句
"""

try:
    # print(num)
    print(3/0)
except ZeroDivisionError as e:
    print('除0错误')
except NameError as e:
    print('没有该参数')
else:
    print('程序没有错误')

print('程序继续执行了')

# 使用except而不使用任何错误类型
try:
    print(arg)
except:
    print('程序出现异常')

# 使用except捕获多种错误
try:
    print(arg)
except (NameError,ZeroDivisionError):
    print('出现了NameError或者ZeroDivisionError的异常')

# 特殊
# 1.所有的异常都继承自基类BaseException
# 异常从上往下依次匹配，匹配成功后不再继续匹配
try:
    print(5/0)
except BaseException as e:
    print('异常1')
except ZeroDivisionError as e:
    print('异常2')

# 2.跨越多层调用，外层函数依然能捕获到内层函数的异常
# 实例
def func1(num):
    print(1/num)

def func2(num):
    func1(num)

def main():
    func2(0)

try:
    main()
except ZeroDivisionError as e:
    print('**********')