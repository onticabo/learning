# coding: utf-8
# from my_input import input

days, offs = map(int, input().split())

calendar = [input() for _ in range(days)]

max_consecutive = 0
for i in range(days):
    off_count, consecutive = 0, 0
    for j in range(i, days):
        if calendar[j] == 'work':
            off_count += 1
        if off_count > offs:
            break
        consecutive += 1
    max_consecutive = max(max_consecutive, consecutive)

print(max_consecutive)