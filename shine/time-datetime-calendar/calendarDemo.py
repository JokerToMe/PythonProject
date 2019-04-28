# 日历模块

import calendar

# 返回指定某年某月的日历
print(calendar.month(2019,5))
# 返回一年的日历
print(calendar.calendar(2019))
# 判断闰年
print(calendar.isleap(2000))
# 见运行结果
print(calendar.monthrange(2019,5))
# 见运行结果
print(calendar.monthcalendar(2019,5))

