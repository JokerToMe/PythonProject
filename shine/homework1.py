# 求水仙花数
num = 100
while num < 1000:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    # abc分别为个十百位数
    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1
# 判断一个数是否是质数
inputNum = int(input())
if inputNum == 2:
    print("是质数")
else:
    n = 2
    while n < inputNum:
        if inputNum % n == 0:
            print("不是质数")
            break
        n += 1
    if n == inputNum:
        print("是质数")

