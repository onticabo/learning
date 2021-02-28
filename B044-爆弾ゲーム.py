#from my_input import input

class Area:
    def __init__(self, map):
        self.map = map
    def show_map(self):
        for line in self.map:
            print(''.join(line))
    def square(self, y, x):
        return self.map[y][x]
    def burn(self, y, x):
        if self.map[y][x] != '#':
            if self.map[y][x] == 'X':   # 敵だったら焼く
                self.map[y][x] = 'B' 
            return True
        return False
    def count_enemies(self):
        return sum([v.count('X') for v in self.map])

## main
H, W = map(int, input().split())

area_map = [list(input()) for _ in range(H)]
area = Area(area_map)

for i in range(H):
    for j in range(W):
        square = area.square(i, j)
        if square in '0123456789':
            power = int(square)
            for diff in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                for k in range(1, power + 1):
                    if not area.burn((i + diff[0] * k), (j + diff[1] * k)):
                        break

print('YES' if area.count_enemies() == 0 else 'NO')