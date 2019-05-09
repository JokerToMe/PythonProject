# 线程调度（难点）,使线程按照一定的顺序来执行
import threading,time

# 概念
# 计算密集型（例如，计算圆周率，高清视频解码）：CPU进行大量的运算，应使用较少数量的进程或线程，这样可以避免频繁切换，导致CPU效率降低
# IO密集型（例如：网络、磁盘的IO任务）：CPU占用较少，任务越多，CPU效率越高

# 线程条件变量
cond = threading.Condition()

# 需求，按0-9顺序打印
def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.notify()
            cond.wait()

if __name__ == '__main__':
    t1 = threading.Thread(target=run1)
    t1.start()
    t2 = threading.Thread(target=run2)
    t2.start()

