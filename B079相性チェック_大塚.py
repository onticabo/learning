# coding: utf-8
def to_number(ch):
    return ord(ch) - 96

def to_chemistry_index(source):
    while 1 < len(source):
        result = []
        for i in range(0, len(source) - 1):
            value = (source[i] + source[i+1]) % 101
            result.append(value)
        source = result
    return source[0]

a, b = input().split()
list_a = list(map(to_number, list(a))) # 2個目のlistは要らなかったかな?
list_b = list(map(to_number, list(b)))
ab = to_chemistry_index(list_a + list_b)
ba = to_chemistry_index(list_b + list_a)
print(ab if ba < ab else ba)
