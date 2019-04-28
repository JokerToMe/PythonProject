# 基于datetime进行了封装，提供了更多方法，接口更直观，更容易调用

# 模块中的类：
# datetime：时间和日期
# timedelta：计算时间间隔
# tzinfo：时区相关
# time：时间
# date：日期

# datetime和date之间可以通过字符串相互转化

from datetime import datetime

# 获取当前时间
d1 = datetime.now()
print(d1)
# 获取指定时间
d2 = datetime(1993,9,23,1,1,1,12356)
print(d2)
# 将时间转为字符串
d3 = d1.strftime('%Y-%m-%d %X')
print(d3)
print(type(d3))
# 将格式化字符串转为datetime类型,后面传入的格式必须与字符串时间格式一致
d4 = datetime.strptime(d3,'%Y-%m-%d %X')
print(d4)
# datetime类型可以做减法，求时间间隔
d5 = d1 - d2
print(d5)
print(type(d5))
print(d5.days)
# 间隔天数除外的秒数
print(d5.seconds)