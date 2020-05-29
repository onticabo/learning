# coding: utf-8

number = int(input())

hands_count = { 'paper':0, 'rock':0, 'scissors':0 }
win_or_lose = { 'paper':'rock', 'rock':'scissors', 'scissors':'paper'}

for i in range(number):
    hands_count[input()] += 1

remain_count = 0
remain_hand = ''

for key, value in hands_count.items():
    if value == 0:
        remain_hand = key
        remain_count += 1

if remain_count == 1:
    print(win_or_lose[remain_hand])
else:
    print('draw')
