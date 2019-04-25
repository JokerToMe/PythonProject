# 求两个数的最大公约数和最小公倍数
print('请输入第一个整数：')
inputNum = int(input())
print('请输入第二个整数：')
inputNum2 = int(input())
if inputNum < inputNum2:
    n = inputNum
else:
    n = inputNum2

while n > 1:
    if inputNum % n == 0 & inputNum2 % n == 0:
        print('最大公约数为：',n)
        break
    else:
        n -= 1

if n == 1:
    print('没有最大公约数')

print('最小公倍数为：',inputNum * inputNum2 // n)