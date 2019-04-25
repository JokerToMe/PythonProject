# 偏函数
import functools
# 示例
print(int('1010',base=2))
# 当需要大量的调用base=2的int方法时，需要做一下简化
# 偏函数（对参数默认值的控制）
def int2(str,base=2):
    return int(str,base)
print(int2('1011'))
# 把参数固定，返回一个新的函数
int3 = functools.partial(int,base=3)