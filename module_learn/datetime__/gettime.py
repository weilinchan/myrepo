#!/usr/bin/python3
# coding: utf-8
"""datetime是Python处理日期和时间的标准库。"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

# todo: 获取当前日期和时间
now = datetime.now()  # 2019-03-10 16:03:08.087306
# print(now)

# todo: 获取指定日期和时间（用指定日期和时间创建datetime）
dt = datetime(2015, 4, 19, 12, 20, 45)  # 2015-04-19 12:20:45
# print(dt)

# todo: datetime转换为timestamp(秒数)
"""计算机时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的.
"""
ts = now.timestamp()  # 1552206137.834067   小数位表示毫秒数
# print(ts)

# todo: timestamp转换为datetime
t = 1552009988.542688
dtf = datetime.fromtimestamp(ts)  # 本地时区: 2019-03-10 17:44:15.807359
# print(dtf)
dtfutc = datetime.utcfromtimestamp(ts)  # UTC标准时区：2019-03-10 09:44:15.807359
# print(dtfutc)

# todo: str转换为datetime
"""用户输入的日期和时间是字符串，要处理日期和时间，必须把str转换为datetime。"""
cday = datetime.strptime('2015-6-1 12:12:59', '%Y-%m-%d %H:%M:%S')  # 2015-06-01 12:12:59
# print(cday)

# todo: datetime转换为str
"""datetime对象，要把它格式化为字符串显示给用户"""
strt = now.strftime('%a, %b %d %H:%M')  # Sun, Mar 10 18:17
# print(strt)

# todo: datetime加减
nextday = now + timedelta(days=1)  # 2019-03-11 18:22:53.247909
# print(nextday)
nexthour = now + timedelta(hours=2)  # 2小时后
nexttime = now + timedelta(hours=2, days=1)

# todo: 本地时间转换为UTC时间
"""datetime类型有一个时区属性tzinfo,但默认为None,无法区分这个datetime到底是哪个时区,除非强行给datetime设置一个时区"""
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区 UTC+8:00
dt_tz = now.replace(tzinfo=tz_utc_8)  # 强制设置为 UTC+8:00  2019-03-10 18:46:25.575690+08:00
# print(dt_tz)

# todo: 时区转换
"""可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
也可以用任何带时区的datetime，转换到其他任意时区,不是必须从UTC+0:00时区转换到其他时区
"""
# 获取UTC时间并强制设置时区为UTC+00:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 2019-03-10 10:57:38.182161+00:00
print(utc_dt)
# 转换为北京时间带时区
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 2019-03-10 18:57:38.182161+08:00
print(bj_dt)
# 转换为东京时间带时区
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))  # 2019-03-10 19:57:38.182161+09:00
print(tokyo_dt)
# 将北京时间转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  # 2019-03-10 19:57:38.182161+09:00
print(tokyo_dt2)
