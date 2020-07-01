# coding: utf-8
# from my_input import input

def new_life(line, next):
    expand = line[-1] + line + line[0] # 端を拡張
    new_life = ''
    for n in range(1,len(expand)-1):
        key = expand[n-1] + expand[n+1] # 左と右を足してキーにする
        new_life += next[key]   # 新しい文字を取得
    return new_life

initial, rule = input().split()
life_status = initial
next_dic = dict(zip(['--', '-+', '+-', '++'], rule))

history = []                    # 履歴を保存するリスト
while initial not in history:   # 初期配列に戻らないうちは次を調べる
    life_status = new_life(life_status, next_dic)
    if life_status in history:  # 初期配置ではないのに履歴にはあるということは
        print("NO")             # 永久に初期配置には戻らない
        break
    history.append(life_status) # 履歴を保存
else:
    print("YES")                # 初期配置に戻ったのでYES
