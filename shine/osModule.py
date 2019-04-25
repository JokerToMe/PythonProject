# os：包含了普遍的操作系统的功能
import os

# 获取操作系统类型 nt：windows系统  posix：Linux，Unix或Mac OS X
print(os.name)
# 打印操作系统详细信息，windows不支持
# print(os.uname())
# 获取操作系统中所有的环境变量
print(os.environ)
# 获取指定的环境变量
print(os.environ.get('ANDROID_SDK_HOME'))
# 获取当前目录
print(os.curdir)
# 获取当前文件所在目录的绝对路径
print(os.getcwd())
# 获取当前目录下的文件列表
print(os.listdir())