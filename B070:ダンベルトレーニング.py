# coding: utf-8
# from my_input import input

import itertools
import copy

def get_weight_combination(weghit_list):
    ret_combination = []
    for n in range(len(weghit_list)):
        permutation = itertools.permutations(weghit_list, n+1)
        for combination in permutation:
            if sum(combination) == weight:
                ret_combination = combination
    return ret_combination
def remove_used(weghit_list, combination):
    for weight in combination:
        weghit_list.remove(weight)
    return weghit_list

count, adequate = map(int, input().split())
plate = [int(input()) for _ in range(count)]

weight = adequate // 2
left, right = [], []
while weight > 0 and not (left and right):
    tmp_plate = copy.copy(plate)
    left = get_weight_combination(tmp_plate)
    tmp_plate = remove_used(tmp_plate, left)
    right = get_weight_combination(tmp_plate)
    if not (left and right):
        weight -= 1

print(weight*2)
