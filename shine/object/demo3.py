# 析构函数：__del()__释放对象时自动调用

class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self):
        print('My name is %s,%d years old' % (self.name,self.age))
        print(self.__class__)

    # 在内部创建对象
    def createInstance(self):
        p = self.__class__('inner',0)

    def __del__(self):
        print('我是析构函数')

p = Person('Shine',18)
p.say()
# 手动释放对象
del p
# 访问p的属性时会报错
# p1 = Person('Nick',18)
# p1.say()

def func():
    p = Person('func',1)
    print('函数结束时释放对象')

func()