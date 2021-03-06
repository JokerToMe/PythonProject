# 使用模块的意义：把相似功能的函数分组，分别放到不同的文件中去，.py文件就是一个模块
# 优点：1.提高代码的可维护性
# 2.提高了代码的复用度
# 3.引用其他模块（内置模块，三方模块，自定义模块）
# 4.避免函数名和变量名的冲突

# 使用标准库中的模块
import sys

print(sys.argv)
# 获取命令行参数的列表
# for i in sys.argv:
#     print(i)
#
# name = sys.argv[1]
# age = sys.argv[2]
# hobby = sys.argv[3]
#
# print(name,age,hobby)

# 自动查找所需模块的路径列表
print(sys.path)

