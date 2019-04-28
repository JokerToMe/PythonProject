# 深度遍历
import os

def getAllDirDeep(path):
    stack = []
    stack.append(path)
    # 处理栈
    while len(stack) != 0:
        # 从栈里取出数据
        dirPath = stack.pop()
        print('目录',dirPath)
        fileslist = os.listdir(dirPath)
        for fileName in fileslist:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                stack.append(fileAbsPath)
            else:
                print('普通文件',fileName)

getAllDirDeep(r'D:\ShineLaw\PythonProject\shine')