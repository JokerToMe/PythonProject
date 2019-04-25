timeStr = input()
strs = timeStr.split(':')
h = int(strs[0])
m = int(strs[1])
s = int(strs[2])
s += 1
if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
print('%.2d:%.2d:%.2d' %(h,m,s))