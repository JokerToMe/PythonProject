# 广度遍历
import os,collections

def getAlldirRange(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        dir = queue.popleft()
        print('目录',dir)
        fileList = os.listdir(dir)
        for fileName in fileList:
            absPath = os.path.join(dir,fileName)
            if os.path.isdir(absPath):
                queue.append(absPath)
            else:
                print('普通文件',fileName)


getAlldirRange(r'D:\ShineLaw\PythonProject\shine')