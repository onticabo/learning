# coding: utf-8
from my_input import input

n = int(input())

goto, back = 'go to ', 'use the back button'
history = []
current_pos = 0
for i in range(n):
    command = input()
    if goto in command:
        page = command[len(goto):]
        current_pos = 0
    elif back in command:
        current_pos -= 2
        page = history[current_pos]
    history.append(page)

for page in history:
    print(page)
