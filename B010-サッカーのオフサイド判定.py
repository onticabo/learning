# coding: utf-8
from my_input import input

def team_lineup(players, reverse=False):
    if reverse:
        players = list(map(lambda x:-x, players))
    return zip(range(1, 12), players)
def is_offside(x_player, x_passer, x_offside_line):
    return x_passer < x_offside_line < x_player
def get_offside_line(diffence_team):
    return sorted(diffence_team, reverse=True)[1]
def get_opponent(name):
    return 'A' if name == 'B' else 'B'

# main
offence_name, passer = input().split()
team = {}
team['A'] = list(map(int, input().split()))
team['B'] = list(map(int, input().split()))

if offence_name == 'B':
    for t in team:
        t = list(map(lambda x:-x, t))

diffence_name = get_opponent(offence_name)
offence_team = team[offence_name]
diffence_team = team[diffence_name]

x_offside_line = get_offside_line(diffence_team)
x_passer = int(offence_team[int(passer)-1])

offside_players = []
for idx, x_p in enumerate(offence_team):
    if is_offside(x_p, x_passer, x_offside_line):
        offside_players.append(idx+1)

if offside_players:
    for p in offside_players:
        print(p)
else:
    print('None')
