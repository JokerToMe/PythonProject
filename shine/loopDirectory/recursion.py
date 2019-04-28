import os

def getAllDir(path,sp=''):
    filelist = os.listdir(path)
    # print(filelist)
    sp += '   '
    for fileName in filelist:
        abusolutePath = os.path.join(path,fileName)
        if os.path.isdir(abusolutePath):
            print(sp,'目录',fileName)
            getAllDir(abusolutePath,sp)
        else:
            print(sp,'普通文件',fileName)

getAllDir(r'D:\ShineLaw\PythonProject\shine')