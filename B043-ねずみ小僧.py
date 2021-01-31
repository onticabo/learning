# coding: utf-8
from my_input import input

class City:
    def __init__(self, map, height, width):
        self.map = map
        self.height = height
        self.width = width
    def show_map(self):
        for line in self.map:
            print(''.join(line))
    def resident(self, y, x):   # その住居の住民の種類を返す
        return self.map[y][x]
    def flip(self, y, x):       # 住民が庶民なら富豪に富豪なら庶民にする
        self.map[y][x] = '*' if self.map[y][x] == '.' else '.'
    def in_city(self, y, x):    # 座標が町の中かどうか
        return (0 <= y < self.height) and (0 <= x < self.width)

class Walker:
    def __init__(self, y, x):
        self.y, self.x = y, x
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # それぞれの方角に動くときの増分
        self.ref_direction = 0  # 初期値は北(=0)
    def move(self):
        self.y += self.direction[self.ref_direction][0] # 向いてる方角に対応した増分を足す
        self.x += self.direction[self.ref_direction][1]
    def turn_right(self):
        self.ref_direction = (self.ref_direction + 1) % 4   # 右を向いたら右にインデックスをずらす
    def turn_left(self):
        self.ref_direction = (self.ref_direction - 1) % 4   # 左を向いたら左にインデックスをずらす
    def get_pos(self):
        return self.y, self.x

## main
H, W = map(int, input().split())
h0, w0 = map(int, input().split())

edo_map = [list(input()) for _ in range(H)]
edo = City(edo_map, H, W)

mouse_kid = Walker(h0 - 1, w0 - 1)  # 内部では0開始

while True:
    y, x = mouse_kid.get_pos()
    if not edo.in_city(y, x):
        break   # 町の外に出たら終了
    if edo.resident(y, x) == '.':
        mouse_kid.turn_right()  # 庶民の家なら右に回る
    else:
        mouse_kid.turn_left()   # 富豪の家なら左に回る
    edo.flip(y, x)      # 庶民と富豪を入れ替える
    mouse_kid.move()    # 向いた方向に移動

edo.show_map()  # 町の状態を表示

