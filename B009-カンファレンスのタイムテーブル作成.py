# coding: utf-8
# from my_input import input

def m2h(m):
    hour = m // 60 % 24
    minute = m % 60
    return f'{hour:02}:{minute:02}'
def h2m(h):
    hour, minute = map(int, h.split(':'))
    return hour * 60 + minute

def presentation_time(start_time, duration):
    global rest
    noon = h2m('12:00')
    end_time = start_time + duration
    if not rest and noon < end_time:
        start_time += 60 - 10
        end_time = start_time + duration
        rest = True
    return start_time, end_time
    
n = int(input())

start_time = h2m('10:00')

rest = False
for _ in range(n):
    name, duration = input().split()
    start_time, end_time = presentation_time(start_time, int(duration))
    print(f'{m2h(start_time)} - {m2h(end_time)} {name}')
    start_time = end_time + 10
