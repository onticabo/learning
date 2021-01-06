# coding: utf-8
from my_input import input

def next_pos(x, y, house, direction):
    return 0
def turn(house, direction):
    return 0

H, W = map(int, input().split())
x, y = map(int, input().split())

edo_map = []
for _ in range(H):
    edo_map.append(list(input()))

while True:
    x, y = next_pos(x, y)
    if not (0 <= x < W and 0 <= y < H):
        break
    cuurent_house = '.' if edo_map[y][x] == '*' else: '*'
