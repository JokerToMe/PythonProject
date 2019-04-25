s1 = set([1,2,3])
# 重复元素无法添加，无序且没有下标
s1.add(2)
print(s1)
# 插入真个list
s1.update([4,5,6])
print(s1)
# 插入字符串
s1.update('str')
print(s1)
s1.add('str')
print(s1)
# 删除元素
s1.remove('str')
print(s1)
# 遍历获取元素
for i in s1:
    print(i)
for index,data in enumerate(s1):
    print(index,data)

# 求取交集
s2 = set([4,5,6,7])
print(s1 & s2)
# 求取并集
print(s1 | s2)