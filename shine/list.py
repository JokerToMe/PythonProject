# 列表中元素可以是不同类型
list1 = [1,2,3,"hello",True]
print(list1)
# 列表元素的访问
# 取值，替换
print(list1[1])
list1[1] = "new"
print(list1)
ages = [22,33,58,78]
index = 0
sum = 0
while index < len(ages):
    sum += ages[index]
    index += 1
print(sum/len(ages))
print(list1+ages)
# 列表重复添加
print(list1*3)
# 判断元素是否在列表中
print(3 in list1)
print("world" in list1)
# 列表截取
print(list1[1:3])
print(list1[1:])
print(list1[:3])
# 列表方法
list1.append(6)
print(list1)
# 在末尾添加一个新的元素,追加数组请用+
list1.append([2,3,4])
print(list1)
# 追加多个元素
list1.extend([2,3,4])
print(list1)
# 在某个位置插入元素
list1.insert(1,"index=1")
print(list1)
# 删除指定下标元素，默认最后一个元素
list1.pop()
print(list1)
list1.pop(2)
print(list1)
# 移除指定内容的元素(如果有多个，只移除第一个)
list1.remove(3)
print(list1)
# 清除列表中所有的数据
# list1.clear()
# print(list1)
# 查某个值的下标
print(list1.index(3))
# 圈定一个范围去查找
print(list1.index(1,2,5))
# 列表长度
print(len(list1))
# 求最大数
print(max([1,2,3,4]))
print(min([1,2,3,4]))
# 统计元素的个数
print([1,2,2,3].count(2))
# 结合remove和count方法删除值相同的所有元素
list2 = [1,2,2,3,4,5,2]
count = list2.count(2)
n = 0
while n < count:
    list2.remove(2)
    n += 1
print(list2)
# 倒序
list2.reverse()
print(list2)
list2.sort()
# 升序
print(list2)
# 浅拷贝
list3 = list2
list3[1] = 2
print(list2)
print(list3)
# list2和list3地址相同
print(id(list2))
print(id(list3))
# 深拷贝
list4 = list2.copy()
list4[2] = 3
print(list3)
print(id(list4))
# 将元组转换成数组
print(list((1,2,3,4)))