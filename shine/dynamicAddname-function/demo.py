from types import MethodType

class Person(object):

    __slots__ = ('name','age','speak')


# 动态添加属性和方法体现了动态语言的优点（灵活）
p = Person()
p.name = 'Tom'
print(p.name)

def say(self):
    print('hello,python')
# 变形
# p.speak = say
# p.speak(p)
# 相当于一个偏函数，给say方法固定了一个值p变成speak方法，从而实现动态添加方法的效果
p.speak = MethodType(say,p)
p.speak()

# 思考：如何限制实例属性的添加，只能添加特定的属性
# 解决：在创建累的时候添加一个特殊属性__slot__（本质上是一个元组，防止能够被添加的属性和方法）
# 添加__slot__范围外的属性或者方法会报错
# p.hobby = 'game'