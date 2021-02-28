from my_input import input

class Cell:
    def __init__(self, y, x, z=0):
        self.y, self.x, self.z = y, x, z

class Diorama:
    def __init__(self, height, width, cells):
        self.height = height
        self.width = width
        self.cells = cells
    
    def coordinate2index(self, y, x):
        if 0 <= y < self.height and 0 <= x < self.width:
            return y * self.width + x
        return -1

    def draw(self):
        for y in range(self.height):
            line = []
            for x in range(self.width):
                position = self.coordinate2index(y, x)
                line.append(str(self.cells[position].z))
            print(' '.join(line))

    def drop(self, y, x):
        current_height = self.get_height(y, x)

        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # n e s w
        for yd, xd in neighbors:
            neighbors_height = self.get_height(y + yd, x + xd)
            if neighbors_height < current_height:
                self.drop(y + yd, x + xd)
                break
        else:
            self.stack(y, x)

    def stack(self, y, x):
        position = self.coordinate2index(y, x)
        if position >= 0:
            self.cells[position].z += 1

    def get_height(self, y, x):
        position = self.coordinate2index(y, x)
        if position >= 0:
            return self.cells[position].z
        return 500000


if __name__ == '__main__':

    H, W, N = map(int, input().split())
    
    cells = [Cell(y, x, 0) for y in range(H) for x in range(W)]
    diorama = Diorama(H, W, cells)
    
    for _ in range(N):
        x, y = map(int, input().split())
        diorama.drop(y-1, x-1)
    
    diorama.draw()