"""
递归调用：一个函数，调用了自身，称为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事，递归都能干

"""

# 方式：
# 1.写出临界条件
# 2.找这一次和上一次的关系
# 3.假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

# 输入一个数n，计算从1加到n的和

def sumN(n):
    if n == 1:
        return 1
    else:
        return sumN(n-1)+n

print(sumN(100))

# 尾递归
def sumTailN(n,r):
    if n == 1:
        return r
    else:
        return sumTailN(n-1,r+n)

print(sumTailN(100,1))