# coding: utf-8

def uranai(first, second):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # [chr(i) for i in range(ord('a'),ord('a')+26)] とも書ける
    name = first + second
    numbers = []
    for c in name:
        numbers.append(alphabet.index(c) + 1)
    # 1行で [alphabet.index(c) + 1 for c in name] とも書ける
    while len(numbers) > 1:
        tmp_numbers = []
        for i in range(len(numbers)-1):
            tmp_numbers.append((numbers[i] + numbers[i+1]) % 101)
        numbers = tmp_numbers
    return numbers[0]
    
male, female = input().split()

result1 = uranai(male, female)
result2 = uranai(female, male)

result = result1 if result1 > result2 else result2
print(result)
