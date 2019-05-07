from multiprocessing import Process
from time import sleep

def run():
    print('子进程启动')
    sleep(3)
    print('子进程结束')

if __name__ == '__main__':
    print('父进程启动')
    p = Process(target=run)
    p.start()
    # 需求：等子进程结束后再执行父进程
    # 可以在父进程中开辟多个子进程，父进程调配，子进程执行任务，等所有子进程执行完任务后再结束父进程
    p.join()
    # 父进程的结束不能影响子进程
    print('父进程结束')