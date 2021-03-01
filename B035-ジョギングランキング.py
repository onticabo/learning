# coding: utf-8
from my_input import input

def sort_record(record):
    record = dict(sorted(record.items(), key=lambda x: x[0]))
    record = dict(sorted(record.items(), key=lambda x: x[1], reverse=True))
    return record

n, run_count, rank = map(int, input().split())

prev_record = {}
last_record = {}
for _ in range(n):
    name, mileage = input().split()
    prev_record[name] = int(mileage)
    last_record[name] = 0
prev_record = sort_record(prev_record)

for _ in range(run_count):
    date, name, mileage = input().split()
    last_record[name] = last_record.get(name, 0) + int(mileage)
last_record = sort_record(last_record)

for idx, item in enumerate(last_record.items()):
    name, length = item[0], item[1]
    prev_rank = list(prev_record.keys()).index(name)
    comment = 'same'
    if idx < prev_rank:
        comment = 'up'
        if prev_rank >= rank:
            comment = 'new'
    elif prev_rank < idx:
        comment = 'down'
    if rank > idx:
        print(name, length, comment)
    else:
        break


