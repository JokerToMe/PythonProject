# 重写：将函数重新定义写一遍

# __repr__：给机器调用的，在命令行中输入对象名是调用
# __str__：在调用print方法打印对象时调用
# 注意：在没有str且有repr时，repr = str

class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 重写方法
    def __str__(self):
        return 'My name is %s,%d is years old' % (self.name,self.age)

    def __repr__(self):
        return 'My name is %s,%d is years old' % (self.name, self.age)

p = Person('Shine',26)
# print(p.__str__())等同
print(p)