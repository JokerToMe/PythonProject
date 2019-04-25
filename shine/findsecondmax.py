inputNum = []
n = 0
while n < 10:
    val = int(input())
    inputNum.append(val)
    n += 1
print(inputNum)

inputNum.sort()
countMax = inputNum.count(inputNum[-1])
print('第二大的数为',inputNum[-(countMax+1)])