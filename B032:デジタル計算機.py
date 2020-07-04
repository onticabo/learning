# coding: utf-8
from my_input import input

class Soroban:
    size = len('*|=|****') # soroban size
    tama = ['*|=|****', '*|=*|***', '*|=**|**', '*|=***|*', '*|=****|', 
            '|*=|****', '|*=*|***', '|*=**|**', '|*=***|*', '|*=****|']
    dic_tama = dict(zip(tama, range(10)))
    dic_deci = dict(zip(range(10), tama))

    def __init__(self, digit, pattern):
        self.digit = digit
        self.set_by_pattern(pattern)
    def __add__(self, other):
        total = self.decimal + other.decimal
        total_soroban = Soroban(self.digit, self.pattern)
        total_soroban.set_by_decimal(total)
        return total_soroban

    def set_by_pattern(self, pattern):
        self.pattern = pattern
        self.decimal = self.pattern2decimal()
    def pattern2decimal(self):
        t_pattern = self.transepose(self.pattern)
        str_deci = ''
        for line in t_pattern:
            str_deci += str(Soroban.dic_tama[''.join(line)])
        return int(str_deci)
    def set_by_decimal(self, decimal):
        self.decimal = decimal
        str_deci = str(self.decimal).zfill(self.digit)
        t_pattern = [Soroban.dic_deci[int(c)] for c in str_deci]
        self.pattern = self.transepose(t_pattern)
    def show(self):
        for line in self.pattern:    
            print(''.join(line))

    def make_matrix(self, x, y, init='?'):
        return [[init] * x for _ in range(y)]
    def transepose(self, matrix):
        x, y = len(matrix[0]), len(matrix)
        t_matrix = self.make_matrix(y, x)
        for i in range(y):
            for j in range(x):
                t_matrix[j][i] = matrix[i][j]
        return t_matrix

digit = int(input())

soroban_a = Soroban(digit, [input() for _ in range(Soroban.size)])
soroban_b = Soroban(digit, [input() for _ in range(Soroban.size)])

total = soroban_a + soroban_b
total.show()

