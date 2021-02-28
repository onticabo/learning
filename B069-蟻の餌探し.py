from my_input import input

class Cell:
    def __init__(self, x, y, pheromones=False, food=False):
        self.x, self.y = x, y
        self.pheromones = pheromones
        self.food = food

class Cage:
    def __init__(self, height, width, cells):
        self.height, self.width = height, width
        self.cells = cells
        self.connect = [True] + [False] * (height * width - 1)
        pass

    def _c2i(self, y, x):
        return y * self.width + x
    def _i2c(self, index):
        return index // self.width, index % self.width

    def set_food(self, y, x):
        self.cells[self._c2i(y-1, x-1)].food = True
    
    def connect_pheromones(self):
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, cell in enumerate(self.cells):
            y, x = self._i2c(i)
            if cell.pheromones:
                for vec in neighbors:
                    yd, xd = vec
                    i_n = self._c2i(y+yd, x+xd)
                    if 0 <= i_n < self.height * self.width and self.cells[i_n].pheromones:
                        self.connect[i_n] = self.connect[i]

    def connected(self, y, x):
        return self.connect[self._c2i(y-1, x-1)]    

    
if __name__ == '__main__':

    H, W = map(int, input().split())

    cells = []        
    for y in range(H):
        line = list(input())
        for x in range(W):
            pheromones = line[x] == '#'
            cells.append(Cell(y, x, pheromones))
    
    cage = Cage(H, W, cells)
    cage.connect_pheromones()

    N = int(input())
    food_pos = []
    for _ in range(N):
        y, x = map(int, input().split())
        food_pos.append((y, x))
        cage.set_food(y, x)

    for y, x in food_pos:
        if not cage.connected(y, x):
            print('NO')
            break
    else:
        print('YES')
