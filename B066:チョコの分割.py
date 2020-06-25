# coding: utf-8

h, w = map(int, input().split())

output_line = []
for i in range(h):
    sugar_content = list(map(int, input().split()))
    half = sum(sugar_content) / 2
    letter = 'A'
    line = ''
    for j in range(w):
        line += letter
        if sum(sugar_content[:j+1]) == half:
           letter = 'B'
    output_line.append(line)

if 'A' * w in output_line:
    print('No')
else:
    print('Yes')
    for line in output_line:
        print(line)