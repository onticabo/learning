# coding: utf-8

length = int(input())
usagi_speed, interval, rest = map(int, input().split())

kame_time = int(input()) * length
rest_count = length//interval if length%interval != 0 else length//interval - 1
usagi_time = length * usagi_speed + rest * rest_count

if usagi_time < kame_time:
    print("USAGI")
elif usagi_time > kame_time:
    print("KAME")
else:
    print("DRAW")