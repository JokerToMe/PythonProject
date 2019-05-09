def producer(c):
    c.send(None)
    for i in range(5):
        print('生产者生产了%d' % i)
        r = c.send(i)
        print('消费者消费了%s' % r)
    c.close()

def consumer():
    data = ''
    while True:
        n = yield data
        if not n:
            return
        print('消费者消费了%d' % n)
        r = '200'

c = consumer()
producer(c)