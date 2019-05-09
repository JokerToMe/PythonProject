# 全局变量在线程间是共享，和进程形成对比
# 缺点：容易改乱数据，安全性低

# 原理：num = 1，进行+10操作，变成11，在还未替换原来1的时候，进行了减10操作，变成了-9，-9替换了原来的1，然后才被替换成11，最后结果变成了11
import threading,time

num = 1

def run():
    global num
    for i in range(100000):
        # num被两个线程同时操作的时候会出现问题
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
