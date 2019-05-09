# 在一个进程内部干多件事情
# 每一个线程都共享一个进程的资源
# 线程是最小的执行单元，可与进程的概念做对比
# 线程的调度完全有操作系统分配，程序自己不能决定什么时候执行，执行多长时间

# _thread 低级模块，接近底层
# threading 高级模块，对_thread进行了封装
# 任何进程默认都会启动一个线程，作为主线程，主线程可以启动新的子线程

import threading,time

def run(name):
    print('Child thread %s start %s' % (name,threading.current_thread().name))
    time.sleep(3)
    print('Child thread %s end' % name)

if __name__ == '__main__':
    print('Main thread start %s' % threading.current_thread().name)
    t = threading.Thread(target=run,name='sunck',args=('hello',))
    t.start()
    t.join()
    print('Main thread end')
