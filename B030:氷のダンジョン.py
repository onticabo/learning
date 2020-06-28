# coding: utf-8
# from my_input import input

def floor(dungeon, x, y):
    return dungeon[y][x]

def move(dungeon, direction, x, y):
    step_dic = {'U':(0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0)}
    stop = False
    while not stop:
        next_x = x + step_dic[direction][0]
        next_y = y + step_dic[direction][1]
        next_floor = floor(dungeon, next_x, next_y)
        if next_floor == '.':       # 土
            stop = True
            x, y = next_x, next_y
        elif next_floor == '#':     # 氷
            x, y = next_x, next_y
        elif next_floor == '*':     # 壁
            stop = True
    return x, y

h, w = map(int, input().split())

dungeon = ['*' * (w + 2)]   # 周りを壁(*)で囲う
for _ in range(h):
    dungeon.append('*' + input() + '*')
dungeon.append(['*' * (w + 2)])

x, y = map(int, input().split())

n = int(input())
for _ in range(n):
    direction = input()
    x, y = move(dungeon, direction, x, y)

print(x, y)