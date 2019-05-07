from multiprocessing import Pool
import os,time

# 实现文件拷贝
def copyFile(rPath,wPath):
    with open(rPath,'rb') as rf:
        with open(wPath,'wb') as wf:
            wf.write(rf.read())

# rPath = r'file.txt'
# wPath = r'toFile.txt'
# copyFile(rPath,wPath)

if __name__ == '__main__':
    print('开始拷贝文件')
    # 读取path下的所有文件
    path = 'testPackage'
    fileList = os.listdir(path)
    print(fileList)
    start_time = time.time()
    # 启动for循环读取文件
    with Pool(processes=3) as p:
        for f in fileList:
            fName = f.split('.')[0]
            p.apply_async(copyFile, args=(os.path.join(path,fName), os.path.join(path,fName + 'copy.txt')))
        p.close()
        p.join()
    end_time = time.time()
    print('文件拷贝结束耗时：%d' % end_time-start_time)
