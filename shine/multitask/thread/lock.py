import threading,time

num = 0
# 创建锁对象
l = threading.Lock()

def run():
    global num
    # 加锁
    for i in range(100000):
        # num被两个线程同时操作的时候会出现问题
        # 加锁，阻止了多线程的并发执行，加了锁的代码段，只能单线程执行，其他未加锁的代码段不影响
        # 由于存在多个锁，不同的线程持有不同的锁，并试图获取其他的锁，可能导致死锁，所有线程被挂起，只能靠操作系统强行终止
        # l.acquire()
        # try:
        #     num += 10
        #     num -= 10
        # finally:
        #     # 释放锁，不释放，线程2无法执行
        #     l.release()

        # 简单写法，可以自动加锁和解锁
        with l:
            num += 10
            num -= 10

if __name__ == '__main__':
    print('Main thread start %s' % threading.current_thread().name)
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Main %d' % num)
