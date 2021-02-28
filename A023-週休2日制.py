from my_input import input

def have2holidays(start, end, calendar):
    s = max(start, 0)
    e = min(end, len(calendar))
    return calendar[s:e].count(0) >= 2

N = int(input())
days = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i-6, i+1):
        if have2holidays(j, j+7, days):
            count += 1
            break
print(count)