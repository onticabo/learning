# coding: utf-8

size, limit = map(int, input().split())
count = int(input())

right_list = list(range(1, size + 1)) * (count // size + 1)
log = list(map(int, input().split()))

point, ng_point = 0, 0
for i in range(count):
    if right_list[i] == log[i]:
        point += 1000
    else:
        ng_point += 1
        if ng_point >= limit:
            point = -1
            break
print(point)