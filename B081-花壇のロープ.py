# coding: utf-8
from my_input import input

H, W = map(int, input().split())

garden = []
for _ in range(H):
    garden.append(list(input()))

fence_count = 0
for i in range(H):
    for j in range(W):
        if garden[i][j] == '#':
            fence_count += 4
            if i-1 >=0 and garden[i-1][j] == '#':
                fence_count -= 1
            if i+1 < H and garden[i+1][j] == '#':
                fence_count -= 1
            if j-1 >=0 and garden[i][j-1] == '#':
                fence_count -= 1
            if j+1 < W and garden[i][j+1] == '#':
                fence_count -= 1

print(fence_count)
