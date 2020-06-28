# coding: utf-8
# from my_input import input

def flip(color):
    return 'b' if color == 'w' else 'w'

def isSandwiched(line, pos):
    color = line[pos]
    left, right = line[:pos], line[pos+1:]
    reverse = flip(color)
    if reverse in left and reverse in right:
        return True
    else:
        return False

n = int(input())
line = list(input())

reverse_flag = True
while reverse_flag:
    reverse_flag = False
    tmp_line = []
    for i in range(n):
        if isSandwiched(line, i):
            tmp_line.append(flip(line[i]))
            reverse_flag = True
        else:
            tmp_line.append(line[i])
    line = tmp_line
print(line.count('b'))