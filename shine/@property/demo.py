class Person(object):

    def __init__(self,name,age):
        # 属性对外暴露
        # 缺点：数据不安全，且没有数据过滤
        # self.name = name
        # self.age = age
        # 使用限制访问，需要自己写set和get方法
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    # 相当于之前的getAge方法
    @property
    def age(self):
        return self.__age
    # 相当于之前的setAge方法
    @age.setter
    def age(self,age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age

    def __str__(self):
        return 'My name is %s,%d years old' % (self.__name,self.__age)

    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self,age):
    #     if age < 0:
    #         self.__age = 0
    #     else:
    #         self.__age = age

# 直接访问私有变量
# 在添加了装饰器@property和@age.setter之后，age可以像访问非限制变量一样访问变量
p = Person('shine',20)
# 相当于执行了setAge方法
p.age = 18
# 相当于执行了getAge方法
print(p.age)

p.name = 'law'
print(p.name)
print(p)
