from lawProcess import LawProcess

if __name__ == '__main__':
    print('父进程启动')
    lp = LawProcess('test')
    # 自动调用run方法
    lp.start()
    # 等待子进程结束才执行父进程代码
    lp.join()
    print('父进程结束')