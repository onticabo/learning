# coding: utf-8
import itertools

def dissatisfaction(sequence, cats):
    dissatisfaction = 0
    for idx, number in enumerate(sequence):
        for i in range(idx+1, len(sequence)):           # 自分より後ろに
            if sequence[i] < number:                    # 自分より前の番号がいたら
                dissatisfaction += cats[sequence[i]][1] # 後ろの猫の不満度を加算
    return dissatisfaction

def eat_time(sequence, cats):
    size = len(sequence)
    time = 0
    for idx, cat in enumerate(sequence):
        time += cats[cat][0] * (size - idx)     # 自分の食べる時間は残りの猫を待たせている
    return(time)

# 猫の数と不満度のリミットを読み込み    
n, border = map(int, input().split())
# 猫の食べる時間と抜かされたときの不満度の上がり方を読み込み
cats = [list(map(int, input().split())) for _ in range(n)]

all_list = itertools.permutations(range(n)) # 猫の並び順をすべて列挙

# 順番ごとの不満度の上がり方と総時間を計算
# 総時間の上限は、食べる時間が最も長い猫が全員分いたと仮定したときの時間
min_time = max([cats[i][0] for i in range(n)]) * sum(range(1,n+1))
for sequence in all_list:
    dissatis = dissatisfaction(list(sequence), cats)
    if dissatis <= border:  # 不満度が許容値のときだけ食べる時間を計算
        min_time = min(min_time, eat_time(list(sequence), cats))
print(min_time)