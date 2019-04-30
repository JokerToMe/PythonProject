class Person(object):

    def __init__(self,name,age,hobby,height):
        # 在属性前加（__），变成私有属性，等同于_Person__name
        self.__name = name
        self.__age= age
        # 特殊属性
        self.__hobby__ = hobby
        # 可以直接访问，但应该视为私有属性
        self._height = height

    # 可以对数据做数据过滤
    def setName(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            self.__name = 'default'

    def getName(self):
        return self.__name

p = Person('Shine',18,'money',173)
# 在外部无法访问
# print(p.__name)

# 给程序动态添加属性
# p.hobby = 'money'
# print(p.hobby)

# 修改私有属性的值
# p.setName(18)
# print(p.getName())

# 不能访问__name的原因是，Python解释器把__name变成了_Person__name，不建议这么做
print(p._Person__name)

# 特殊属性可以访问，一般不采取自定义
print(p.__hobby__)

# 可以访问，但应该当做私有属性不去直接访问
print(p._height)



