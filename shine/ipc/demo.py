from multiprocessing import Process,Queue
import os,time

def write(q):
    print('启动写进程%d' % os.getpid())
    for char in ['A','B','C','D']:
        q.put(char)
        time.sleep(1)

def read(q):
    print('启动读进程%d' % os.getpid())
    while True:
        value = q.get(True)
        print('vaule=%s' % value)

if __name__ == '__main__':
    # 在父进程中创建队列，由不同的子进程去操作队列中的数据
    q = Queue()
    # 创建写进程
    wp = Process(target=write,args=(q,))
    # 创建读进程
    rp = Process(target=read,args=(q,))

    wp.start()
    rp.start()

    wp.join()
    # rp进程是一个死循环，必须强行结束
    rp.terminate()

    print('父进程结束')