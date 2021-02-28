#from my_input import input
import itertools

class VHLine:
    def __init__(self, xs, ys, xe, ye):         # 始点と終点の x, y 座標
        self.x0, self.x1 = min(xs, xe), max(xs, xe)
        self.y0, self.y1 = min(ys, ye), max(ys, ye)
        self.horizontal =  self.y0 == self.y1   # y座標が揃っていれば水平
        self.vertical = not self.horizontal     # その逆

    def crossing(l1, l2):
        return l1.horizontal != l2.horizontal   # 方向が異なる

    def intersection(l1, l2):
        if VHLine.crossing(l1, l2):
            v = l1 if l1.vertical else l2
            h = l1 if l1.horizontal else l2
            # 鉛直線のx座標が水平線の始点と終点の間にある yも同様
            if h.x0 <= v.x0 <= h.x1 and v.y0 <= h.y0 <= v.y1: 
                return v.x0, h.y0   # 交点を返す
        return None, None
                
class Square:
    def __init__(self, lines):
        self.lines = lines

    def get_corner(self):
        x0, y0, x1, y1 = 0, 0, 0, 0
        x_list, y_list = [], []
        for pair in itertools.combinations(self.lines, 2):
            if VHLine.crossing(pair[0], pair[1]):
                xi, yi = VHLine.intersection(pair[0], pair[1])
                x_list.append(xi)
                y_list.append(yi)
        if x_list and y_list and None not in x_list + y_list: # 直交しているのに交わらない線がある
            x0, y0, x1, y1 = min(x_list), min(y_list), max(x_list), max(y_list)
        return x0, y0, x1, y1

    def get_area(self):
        x0, y0, x1, y1 = self.get_corner()
        width = x1 - x0
        height = y1 - y0
        return width * height

if __name__ == '__main__':

    N = int(input())
    line_coordinates = [map(int, input().split()) for _ in range(N)]
    lines = [VHLine(xs, ys, xe, ye) for xs, ys, xe, ye in line_coordinates]

    squares = itertools.combinations(lines, 4)
    areas = [Square(square).get_area() for square in squares if Square(square).get_area() > 0]

    print(min(areas))
