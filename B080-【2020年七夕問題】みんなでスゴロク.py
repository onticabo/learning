# coding: utf-8
from my_input import input

n, m, k = map(int, input().split())
masu = [[0, 0]]
for _ in range(1, n-1):
    masu.append(list(map(int, input().split())))
masu += [[0, 0]]

player = [[0, 0, 0] for _ in range(m)]
winner = []
winner_coin = 0
award = 3
for _ in range(k):
    roll = list(map(int, input().split()))
    for i in range(m):
        pos = player[i][0] + roll[i]
        player[i][1] += player[i][2] * roll[i]
        if pos >= n:
            player[i][2] += award
            award = max(award, 0)
            pos = n - 1
        player[i][1] = max(player[i][1]+masu[pos][1], 0)
        pos = pos + masu[pos][0]
        if pos >= n:
            player[i][2] += award
            award = max(award, 0)
            pos = n - 1
        elif pos <= 0:
            pos == 0
        player[i][0] = pos
        if winner and winner_coin < player[i][1]:
            winner.append(i)
            winner_coin = player[i][1]

print(*winner, winner_coin)