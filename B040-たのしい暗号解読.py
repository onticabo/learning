# coding: utf-8
# from my_input import input

decode_time, table = input().split()
code = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz '
table += ' '

for _ in range(int(decode_time)):
    decoded = ''
    for c in code:
        decoded += alphabet[table.index(c)]
    code = decoded

print(code)