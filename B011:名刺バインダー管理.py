# coding: utf-8

p, n = map(int, input().split())
pockets = p * 2
number = n - 1

sheets = number // pockets
pos_on_sheet = number % pockets
reverse_pos = pockets - pos_on_sheet
position = sheets * pockets + reverse_pos

print(position)
