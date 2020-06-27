# coding: utf-8

def count_bingo(table):
    size = len(table)
    bingo = 0

    for x_line in table:
        bingo += 1 if sum(x_line) == size else 0

    for j in range(n):
        y_line = [table[i][j] for i in range(size)]
        bingo += 1 if sum(y_line) == size else 0

    xy_line = [table[i][i] for i in range(size)]
    bingo += 1 if sum(xy_line) == size else 0
    xy_line = [table[i][n-i-1] for i in range(size)]
    bingo += 1 if sum(xy_line) == size else 0
    
    return(bingo)
    
n, count = map(int, input().split())

num_table = []
for i in range(n):
    num_table.append(list(map(int, input().split())))

mark_table = [[0] * n for _ in range(n)]

for _ in range(count - 1):
    call_n = int(input())
    for i in range(n):
        if call_n in num_table[i]:
            mark_table[i][num_table[i].index(call_n)] = 1
            break

bingo_count = 0
for i in range(n):
    for j in range(n):
        if mark_table[i][j] == 0:
            mark_table[i][j] = 1
            bingo_count = max(bingo_count, count_bingo(mark_table))
            mark_table[i][j] = 0

print(bingo_count)
