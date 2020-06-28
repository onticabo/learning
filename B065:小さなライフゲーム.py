# coding: utf-8
# from my_input import input

def new_life(line, rule):
    next_dic = dict(zip(['--', '-+', '+-', '++'], rule))
    expand = line[-1] + line + line[0]
    new_life = ''
    for n in range(1,len(expand)-1):
        key = expand[n-1] + expand[n+1]
        new_life += next_dic[key]
    return new_life

initial, rule = input().split()

life_status = initial
history = []
while initial not in history:
    life_status = new_life(life_status, rule)
    if life_status in history:
        print("NO")
        break
    history.append(life_status)
else:
    print("YES")
