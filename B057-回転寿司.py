# coding: utf-8
# from my_input import input

def round_ring(ring):
    return [ring[-1]] + ring[:-1]

def eat(sushi_ring, eating_map, n):
    if eating_map[n] > 0:
        eating_map[n] -= 1
    elif sushi_ring[n] == 1:
        eating_map[n] = 10 - 1
        sushi_ring[n] = 0
        
    return sushi_ring, eating_map

round_time, customer_num, sushi_num = map(int, input().split())
customer_pos    = list(map(int, input().split()))
sushi_pos       = list(map(int, input().split()))

customer_ring   = [1 if i in customer_pos else 0 for i in range(round_time)]
sushi_ring      = [1 if i in sushi_pos else 0 for i in range(round_time)]

eating_map = [0] * round_time

time = 0
while sum(sushi_ring) > 0 or sum(eating_map) > 0:
    for n in customer_pos:
        sushi_ring, eating_map = eat(sushi_ring, eating_map, n) 
    sushi_ring = round_ring(sushi_ring)
    time += 1

print(time)