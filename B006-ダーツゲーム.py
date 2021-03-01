# coding: utf-8
from my_input import input

import math

oy, speed, angle_d = map(int, input().split())
d_x, d_y, r = map(int, input().split())
G = 9.8
angle_r = math.radians(angle_d)
vx = speed * math.cos(angle_r)
vy = speed * math.sin(angle_r)
t = d_x / vx
y = oy + vy * t - G * t ** 2 / 2
diff = y - d_y
if -r <= diff <= r:
    print('Hit', round(diff, 1))
else:
    print('Miss')