# coding: utf-8
from my_input import input

class Player:
    def __init__(self, x=0):
        self.x = x
class Team:
    def __init__(self, players):
        self.players = players
    def getposition(self, number):
        return self.players[number-1].x
    def getlastline(self):
        return sorted(self.players, key=lambda p:p.x, reverse=True)[1].x
class Game:
    def __init__(self, teams):
        self.offence = teams[0]
        self.diffence = teams[1]
    def sidechange(self):
        tmp = self.offence
        self.offence = list(map(lambda x:-x, self.diffence))
        self.diffence = list(map(lambda x:-x, self.tmp))
    def getoffsideline(self):
        return self.diffence.getlastline()
    def offsideplayers(self, passer):
        passer_x = self.offence.getposition(passer)
        offside_x = self.getoffsideline()
        offside = []
        for idx, player in enumerate(self.offence.players):
            if passer_x < offside_x < player.x:
                offside.append(idx + 1)
        if not offside:
            offside,append('None')
        return offside

# main
offence, passer = input().split()

teams = []
for _ in range(2):
    p_list = list(map(int, input().split()))
    teams.append(Team(list(map(Player, p_list))))
game = Game(teams)

if offence == 'B':
    game.sidechange()

for p in game.offsideplayers(int(passer)):
    print(p)