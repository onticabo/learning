from my_input import input

class Segments:
    def __init__(self, lit):
        self.lit = lit
    def is_correct_number(self):
        joined_lit = ''.join(self.lit)
        correct_numbers = [ '1111110',  # 0
                            '0110000',  # 1
                            '1101101',  # 2
                            '1111001',  # 3
                            '0110011',  # 4
                            '1011011',  # 5
                            '1011111',  # 6
                            '1110010',  # 7
                            '1111111',  # 8
                            '1111011',  # 9
                            ]
        return joined_lit in correct_numbers
    def swap_lit(self, n1, n2):
        self.lit[n1], self.lit[n2] = self.lit[n2], self.lit[n1]
    def rotate(self):
        self.swap_lit(0, 3)
        self.swap_lit(1, 4)
        self.swap_lit(2, 5)
        return self
    def reflect(self):
        self.swap_lit(1, 5)
        self.swap_lit(2, 4)
        return self
    def show(self):
        print(' ' + '_' if self.lit[0] == '1' else ' ' + ' ')
        print(('|' if self.lit[5] == '1' else ' ') + ('_' if self.lit[6] == '1' else ' ') + ('|' if self.lit[1] == '1' else ' '))
        print(('|' if self.lit[4] == '1' else ' ') + ('_' if self.lit[3] == '1' else ' ') + ('|' if self.lit[2] == '1' else ' '))
        print()
    


def judge_correct_numbers(num1, num2):
    print('Yes' if num1.is_correct_number() and num2.is_correct_number() else 'No') 

## main
digit1 = list(input().split())
stay, ref, rot = Segments(digit1), Segments(digit1), Segments(digit1)
print(id(stay), id(ref), id(rot))
stay.show()
ref.reflect().show()
rot.rotate().show()
print(id(stay), id(ref), id(rot))
