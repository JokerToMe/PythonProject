from multiprocessing import Pool
import os,time,random

def run(name):
    print('子进程%d启动 %d' %(name,os.getpid()))
    start_time = time.time()
    time.sleep(random.randint(3))
    end_time = time.time()
    print('子进程%d结束 %d，耗时%d' %(name,os.getpid(),end_time-start_time))

if __name__ == '__main__':
    print('父进程启动 %d' % os.getpid())
    # 创建多个进程
    # 进程池
    # 表示可以同时执行的进程数量
    # Pool默认大小是cpu核心数
    p = Pool()
    for i in range(10):
        # 创建进程放入进程池统一管理
        p.apply_async(run,args=(i,))
    p.close()
    # 在调用join方法之前必须调用close方法，会等待进程池中的所有子进程结束完毕才执行父进程
    p.join()
    print('父进程结束 %d' % os.getpid())

