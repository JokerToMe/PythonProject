import threading,time

def func():
    # 事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            # 阻塞，等待事件的出发
            event.wait()
            # 重置
            event.clear()
            print('sunck is a good man %d' % i)
    t = threading.Thread(target=run)
    t.start()
    return event

e = func()
# 触发时间
for i in range(5):
    time.sleep(2)
    e.set()
