# coding: utf-8

n, g, m = map(int, input().split())

msg_log = [[] for i in range(n)]

group = []
for i in range(g):
    line = list(map(int, input().split()))
    del(line[0])
    group.append(line)

for i in range(m):
    source, flag, target, message = input().split()
    if int(flag) == 0:
        msg_log[int(source)-1].append(message)
        msg_log[int(target)-1].append(message)
    elif int(flag) == 1 and int(source) in group[int(target)-1]:
        for group_member in group[int(target)-1]:
            msg_log[group_member-1].append(message)           

for i in range(n):
    for msg in msg_log[i]:
        print(msg)
    if i < n-1:
        print('--')
