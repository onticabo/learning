# coding: utf-8

students, problems = map(int, input().split())
raw_score = 100//problems

for i in range(students):
    day, count = map(int, input().split())
    score = raw_score * count
    if day >= 10:
        score = 0
    elif day >= 1:
        score = int(score * 0.8)
    rank = 'DDDDDDCBAAA'
    print(rank[score//10])