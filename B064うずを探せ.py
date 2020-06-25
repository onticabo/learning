# coding: utf-8

def move(x, y):
    step = {'U':[0, -1], 'D':[0, 1], 'L':[-1, 0], 'R':[1, 0], } #方向ごと増分

    arrow = wind_map[y][x]  # 方向を取得
    wind_map[y][x] = 'N'    # 通過済みのマーク

    if arrow == 'N':        # 通過済み座標なら無効
        x, y = -1, -1
    else:
        x += step[arrow][0] # 次の座標を求める
        y += step[arrow][1]

    return([x, y])          # 新しい座標を返す

h, w = map(int, input().split())    # マップの大きさ読み込み
wind_map = [list(input()) for _ in range(h)]    # マップ読み込み

x, y, count = 0, 0, 0               # 初期座標と渦カウント用

for i in range(h):
    for j in range(w):
        x, y = j, i
        root = []
        while 0 <= x < w and 0 <= y < h:    # 座標がマップの範囲内
            root.append([x, y])             # 通過座標の履歴を残す
            x, y = move(x, y)
            if [x, y] in root:  # すでに通った座標なら渦
                count += 1
                break

print(count)          