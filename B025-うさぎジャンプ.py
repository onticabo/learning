# coding: utf-8
from my_input import input

def next_position(pos, ring):
    return pos + 1 if pos + 1 < len(ring) else 0

def next_vacant(pos, ring):
    tmp_position = next_position(pos, ring)
    while ring[tmp_position] != 0:
        tmp_position = next_position(tmp_position, ring)
    return tmp_position

## main

bosh_count, rabbits, turns = map(int, input().split())
bosh = [0] * bosh_count

for i in range(1, rabbits + 1):
    bosh[int(input()) - 1] = i

for _ in range(turns):
    for i in range(1, rabbits + 1):
        current_pos = bosh.index(i)
        next_pos = next_vacant(current_pos, bosh)
        bosh[current_pos] = 0
        bosh[next_pos] = i

for i in range(1, rabbits + 1):
    print(bosh.index(i) + 1)

