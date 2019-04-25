# 断言可以迅速找出异常，但极少使用
def func(num,div):
    assert (div != 0),'div不能为0'
    print(num/div)

func(10,0)