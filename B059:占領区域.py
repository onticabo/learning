# coding: utf-8
# from my_input import input

class Map:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.square = [Square(x, y) for x in range(w) for y in range(h)]
    def show(self):
        for i in range(h):
            print(''.join([sqr.occupied for sqr in self.square if sqr.y == i]))

class Square:
    def __init__(self, x, y, occupied='?'):
        self.x = x
        self.y = y
        self.occupied = occupied
    def distance(self, country):
        return abs(self.x - country.x) + abs(self.y - country.y)
    def compete(self, country_list, max_distance):
        min_distance = max_distance
        for country in country_list: 
            distance = self.distance(country)
            if distance < min_distance:
                square.occupied = country.name
                min_distance = distance
            elif distance == min_distance:
                square.occupied = '?'

class Country:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


h, w, n = map(int, input().split())
map = Map(h, w)
country_list = []
for _ in range(n):
    name, x, y = input().split()
    country_list.append(Country(name, int(x)-1, int(y)-1))

for square in map.square:
    max_distance = map.h + map.w
    square.compete(country_list, max_distance)

map.show()