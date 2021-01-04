# coding: utf-8
from my_input import input

n, m = map(int, input().split())

count = 0
max_count = 0
incombo = True
for _ in range(m):
    score, play = input().split()
    if score == play:
        count += 1
    elif '#' in score:
        plain = score.replace('#', '+')
        if plain == play and incombo:
            count += 1
        else:
            incombo = False
            count = 0
    else:
        incombo = True
        count = 0
    max_count = max(max_count, count)

print(max_count)
