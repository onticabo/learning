# coding: utf-8

day_pay, night_pay, midnight_pay = map(int, input().split())

DAY_START = 9
NIGHT_START = 17
MIDNIGHT_START = 22

days = int(input())
total = 0
for i in range(days):
    start, end = map(int, input().split())
    if end < DAY_START:
        total += (end - start) * midnight_pay
    elif end < NIGHT_START:
        if start < DAY_START:
            total += (DAY_START - start) * midnight_pay + (end - DAY_START) * day_pay
        else:
            total += (end - start) * day_pay
    elif end < MIDNIGHT_START:
        if start < DAY_START:
            total += (DAY_START - start) * midnight_pay + (NIGHT_START - DAY_START) * day_pay + (end - NIGHT_START) * night_pay
        elif start < NIGHT_START:
            total += (NIGHT_START - start) * day_pay + (end - NIGHT_START) * night_pay
        else:
            total += (end - start) * night_pay
    else:
        if start < DAY_START:
            total += (DAY_START - start) * midnight_pay + (NIGHT_START - DAY_START) * day_pay \
            + (MIDNIGHT_START - NIGHT_START) * night_pay + (end - MIDNIGHT_START) * midnight_pay
        elif start < NIGHT_START:
            total += (NIGHT_START - start) * day_pay + (MIDNIGHT_START - NIGHT_START) * night_pay \
            + (end - MIDNIGHT_START) * midnight_pay
        elif start < MIDNIGHT_START:
            total += (MIDNIGHT_START - start) * night_pay + (end - MIDNIGHT_START) * midnight_pay
        else:
            total += (end - start) * midnight_pay

print(total)