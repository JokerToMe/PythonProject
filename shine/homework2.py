# 分解质因数
inputNum = int(input())
n = 2
while n < inputNum:
    if inputNum % n == 0:
        inputNum //= n
        print(n)
        n = 2
    n += 1
print(n)