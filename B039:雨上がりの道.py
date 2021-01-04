# coding: utf-8
from my_input import input

def connect(pos1, pos2, pond_list):
    x11, y11, x12, y12 = pond_list[pos1]
    x21, y21, x22, y22 = pond_list[pos2]
    if x11 < x12 < x21 < x22 or y11 < y12 < y21 < y22 or \
        x21 < x22 < x11 < x12 or y21 < y22 < y11 < y12:
        return False
    else:
        return True

pond = int(input())
position = int(input())

pond_list = []
for idx in range(pond):
    pond_list.append(list(map(int, input().split())))
root = [position-1]
c_root = []
while root != c_root:
    c_root = set(root)
    for pos in root:
        for i in range(pond):
            if connect(pos, i, pond_list) and i not in root :
                root.append(i)
    root = set(root)

for pos in root:
    print(pos+1)