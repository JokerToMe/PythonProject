class Person(object):

    # 构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('Shine',26)
print(p.name,p.age)