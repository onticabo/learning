# coding: utf-8

day_pay, night_pay, midnight_pay = map(int, input().split())

paytable = [midnight_pay for i in range(9)] + [day_pay for i in range(8)] \
+ [night_pay for i in range(5)] + [midnight_pay for i in range(1)]

days = int(input())
total = 0
for i in range(days):
    start, end = map(int, input().split())
    for time in range(23):
        if start <= time and time < end:
            total += paytable[time]
print(total)