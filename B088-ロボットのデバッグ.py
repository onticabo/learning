from my_input import input

class Robot:
    def __init__(self):
        self.step_dic = [[0,1], [1,0], [0,-1], [-1,0]]
        self.dic_idx = 0

class Map:
    def __init__(self, squares):
        self.pos = [0,0]
        self.squares = squares

class Square:
    def __init__(self, type, unexplored=True):
        self.type = type

H, W = map(int, input().split())
lines = []
for _ in range(H):
    line = list(input())
    for s in line:
        