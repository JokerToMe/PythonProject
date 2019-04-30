# self代表类的实例，而不是类本身
# self指调用类方法的对象
# self.__class__代表类名

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

p = Person('Shine',18)
p.say()
p1 = Person('Nick',18)
p1.say()