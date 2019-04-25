# 元组一旦初始化便不能修改,若元素为list，则list中的元素可变
# 防止被篡改，提高安全性
tuple2 = (1,2,3,'python')
print(tuple2)
print(type(tuple2))
# 访问元素
print(tuple2[2])
# 定义一个变量的元组
tuple1 = (1,)
print(tuple1)
# 删除元组
del tuple1
# 元组的操作
t2 = (1,2,3)
t3 = (4,5,6)
print(t2 + t3)
# 元组重复
print(t2 * 3)
# 判断元素是否存在
print(1 in t2)
# 元组截取
print(t2[-1:])
# 二位元组,和二位数组类似
t4 = ((1,2),(3,4),(5,6))
print(t4)
# 元组的方法
print(len(t4))
print(max(t4))
# 将列表转为元组
t5 = tuple([1,2,3])
print(t5)