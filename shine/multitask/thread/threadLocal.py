import threading,time

num = 0
# 让每个线程有独立的存储空间
# 每个线程都可以对local读写，但互不影响
local = threading.local()

def run(x):
    x += 10
    x -= 10

def func():
    # 每个线程都会有local.x，相当于线程的局部变量
    local.x = num
    for i in range(100000):
        run(local.x)
    print('%s--%d' % (threading.current_thread().name,local.x))

if __name__ == '__main__':
    print('Main thread start %s' % threading.current_thread().name)
    t1 = threading.Thread(target=func)
    t2 = threading.Thread(target=func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Main %d' % num)

# 为每一个线程去绑定一个数据库，HTTP请求，或者用户信息等