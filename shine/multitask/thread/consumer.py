# 生产者和消费者问题

import threading,queue,time,random

# 生产者
def producer(i,q):
    while True:
        num = random.randint(0,10000)
        q.put(num)
        print('生产者%d生产了数据%d' % (i,num))
        time.sleep(3)
    # 任务完成
    q.task_done()

# 消费者
def consumer(i,q):
    while True:
        num = q.get()
        if num is None:
            break
        print('消费者%d消费了数据%d' % (i, num))
        time.sleep(2)
    # 任务完成
    q.task_done()

if __name__ == '__main__':
    # 创建消息队列
    q = queue.Queue()
    # 启动生产者
    for i in range(4):
        threading.Thread(target=producer,args=(i,q)).start()
    # 启动消费者
    for i in range(3):
        threading.Thread(target=consumer,args=(i,q)).start()

