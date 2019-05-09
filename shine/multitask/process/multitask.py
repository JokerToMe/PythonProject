# 跨平台版本的多进程模块，提供一个Process类来创建进程
from multiprocessing import Process
from time import sleep
import os

# 子进程需要执行的代码
def run(str1):
    print('子进程启动...')
    while True:
        print('子进程：%d %d' %(os.getpid(),os.getppid()))
        sleep(1)

if __name__ == '__main__':
    print('主进程启动...%d' %(os.getpid()))
    # 创建子进程
    # target：说明进程执行的任务，此时是run方法
    p = Process(target=run,args=('nick',))
    # 启动进程
    p.start()
    while True:
        print('主进程：%d %d' %(os.getpid(),os.getppid()))
        sleep(1)
    # 不会执行到run方法，main方法执行结束后才开始
    # run()





