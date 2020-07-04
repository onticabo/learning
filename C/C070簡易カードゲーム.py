# coding: utf-8
number = int(input())

hands_table = { 1:'Four Card', 3:'One Pair', 4:'No Pair'}
for _ in range(number):
    hand = input()
    variety = {}
    for card in hand:
        variety[card] = 1 if card not in variety else variety[card] + 1
        # variety[card] = variety.get(card, 0) + 1 <-こう書くほうがカッコイイ
    if len(variety) == 2:
        if 2 in variety.values():
            print('Two Pair')
        else:
            print('Three Card')
    else:
        print(hands_table[len(variety)])
