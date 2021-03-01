# coding: utf-8
from my_input import input

class Player:
    c_award = 3
    goal_pos = 0
    def __init__(self, sugoroku, position=0, coin=0, award=0):
        self.sugoroku = sugoroku
        self.position = position
        self.coin = coin
        self.award = award
        Player.goal_pos = len(sugoroku) - 1
    def move(self, roll):
        pos = max(min(self.position + roll, Player.goal_pos), 0)
        self.set_award(pos)
        self.position = pos
    def set_award(self, pos):
        if pos == Player.goal_pos and self.award == 0:
            self.award = Player.c_award
            Player.c_award = max(Player.c_award-1, 0)        
    def get_award(self, roll):
        self.coin += self.award * roll
    def get_coin(self, amount):
        self.coin = max(self.coin + amount, 0)

class Square:
    def __init__(self, extend=0, coin=0):
        self.extend = extend
        self.coin = coin

class Sugoroku:
    def __init__(self, road):
        self.road = road
        self.start = 0
        self.goal = len(road)

n, m, k = map(int, input().split())

road_map = [Square()]       # start
for _ in range(n-2):
    extend, coin = map(int, input().split())
    road_map.append(Square(extend, coin))
road_map.append(Square())   # goal

player = [Player(road_map) for _ in range(m)]

for _ in range(k):
    roll = list(map(int, input().split()))
    for i in range(m):
        p, r = player[i], roll[i]
        p.get_award(r)
        p.move(r) # ダイスの目分進む
        s = road_map[p.position]
        p.get_coin(s.coin)
        p.move(s.extend)
        
get_coin = [p.coin for p in player]
max_coin = max(get_coin)
winner = get_coin.index(max_coin) + 1
print(winner, max_coin)