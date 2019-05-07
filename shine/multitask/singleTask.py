from time import sleep

def run():
    while True:
        print('run............')
        sleep(1)

if __name__ == '__main__':
    while True:
        print('shine law')
        sleep(1)
    # 不会执行到run方法，main方法执行结束后才开始
    run()