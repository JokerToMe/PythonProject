# 三个概念
# 1.时间戳：以整型或者浮点型表示时间的一个以秒为单位的时间间隔
# 2.UTC元组：
# year
# month
# day
# hours
# minutes
# seconds
# weekday
# Julia day
# flag 0：正常格式 1：夏令时 -1：自行判断
# 3.格式化字符串

import time

# 返回当前时间的时间戳，浮点数形式
c = time.time()
print(c)
# 将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)
# 获取本地时间元组
tl = time.localtime(c)
print(tl)
# 获取本地时间的时间戳
ltime = time.mktime(tl)
print(ltime)
# 将时间元组转成字符串
lstr = time.asctime(tl)
print(lstr)
# 将时间戳转为字符串
print(time.ctime(ltime))

# tl可以不传，表示转当前时间
print(time.strftime('%Y-%m-%d %H:%M:%S',tl))
# 将时间字符串转为时间元组
print(time.strptime('2019-04-28 15:37:25','%Y-%m-%d %H:%M:%S'))

# 延迟一个时间，整型或者浮点型
time.sleep(1)
# 返回当前程序的cpu执行时间
print(time.process_time())
# time.sleep(2)
# print(time.process_time())