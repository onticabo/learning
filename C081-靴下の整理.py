# coding: utf-8
from my_input import input

n = int(input())

dic = {}
for _ in range(n):
    color, pair = input().split()
    sox = list(dic.get(color, (0,0)))
    if pair == 'L':
        sox[0] += 1
    elif pair == 'R':
        sox[1] += 1
    dic[color] = tuple(sox)

count = 0
for sox in dic.values():
    count += min(sox)

print(count)