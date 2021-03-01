import random

H, W, N = 100, 100, 100
mark = ['.', '#']
print(H, W)
for i in range(H):
    for j in range(W):
        r = random.randint(0, 1)
        print(mark[r], end='')
    print()
print(N)
for _ in range(N):
    print(random.randint(1, N), random.randint(1, N))