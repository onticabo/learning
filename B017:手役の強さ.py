# coding: utf-8
from my_input import input

def hand_rank(hand):
    c_times = {}
    for c in hand:
        c_times[c] = c_times.get(c, 0) + 1
    idx_hand_rank = len(c_times)
    if idx_hand_rank == 2:
        idx_hand_rank = min(c_times.values())
    return idx_hand_rank

raw_hand = list(input())
hand_candidate = []
if '*' in raw_hand:
    raw_hand.remove('*')
    for i in range(len(raw_hand)):
        hand_candidate.append(raw_hand + [raw_hand[i]])
else:
    hand_candidate.append(raw_hand)

hand_name = ['FourCard', 'ThreeCard', 'TwoPair', 'OnePair', 'NoPair']
rank = len(hand_name)
for hand in hand_candidate:
    rank = min(rank, hand_rank(hand))

print(hand_name[rank])