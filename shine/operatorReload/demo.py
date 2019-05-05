# 示例：
print(1 + 2)
print('1' + '2')

class Person(object):

    def __init__(self,num):
        self.num = num

    # 运算符重载
    def __add__(self, other):
        return Person(self.num + other.num)

p1 = Person(1)
p2 = Person(2)
# 等价于 p1.__add__(p2)
pAdd = p1 + p2
print(pAdd.num)