# coding: utf-8
from my_input import input

def move(x, y, w, h, dirc, step):
    step_dic = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    x = (x + step_dic[dirc][0] * int(step)) % w
    y = (y + step_dic[dirc][1] * int(step)) % h
    return x, y

w, h, n = map(int, input().split())
x, y = map(int, input().split())
for _ in range(n):
    dirc, step = input().split()
    x, y = move(x, y, w, h, dirc, step)

print(x, y)