# 可迭代对象(Iterable)：可以作用于for循环的对象,可以用isinstance方法判断是否为可迭代对象
# 可以作用于for循环的数据类型：
# 集合数据类型：list set dict tuple string
# generator：包括生成器和带yield的generator function

from collections.abc import Iterable,Iterator

print(isinstance([1,2],Iterable))
print(isinstance({1,2},Iterable))
print(isinstance((1,2),Iterable))
print(isinstance('abc',Iterable))
print(isinstance({0:'1',1:'2'},Iterable))
print(isinstance([x for x in range(5)],Iterable))
print(isinstance(1,Iterable))

# 迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出一个StopIteration错误，表示无法继续返回下一个值
# 定义：可以被next()函数调用并不断返回下一个值的对象成为迭代器（Iterator）

print(isinstance([1,2],Iterator))
print(isinstance({1,2},Iterator))
print(isinstance((1,2),Iterator))
print(isinstance('abc',Iterator))
print(isinstance({0:'1',1:'2'},Iterator))
print(isinstance([x for x in range(5)],Iterator))
print(isinstance((x for x in range(5)),Iterator))

l = [1,2,3,4,34]
i = (x for x in l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# 超出调用报错
# print(next(i))

# list->Iterator
i1 = iter(l)
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))

print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter(''),Iterator))



