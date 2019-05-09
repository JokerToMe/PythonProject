# 函数执行是通过栈来处理的
# 与线程相比，协程的效率极高，因为只有一个线程，也不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态
# Python对协程的支持是通过generator实现的

def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

# 协程的最简单风格，控制函数的阶段执行,节约线程或者进程的切换
# 返回值是一个生成器
m = run()
print(next(m))
print(next(m))
print(next(m))
