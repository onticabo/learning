# coding: utf-8

def MDtoDate(month, day):
    return(('0' + month)[-2:] + ('0' + day)[-2:])

def draw_card(a, b, m, w, x, y, z):
    w1 = (a[0] * w + b[0]) % m[0]
    x1 = (a[1] * x + b[1]) % m[1]
    y1 = (a[2] * y + b[2]) % m[2]
    z1 = (a[3] * z + b[3]) % m[3]
    return w1, x1, y1, z1
    
def isLuckyDay(m, d, w, x, y, z):
    date = MDtoDate(m, d)
    cards = [str(i % 10) for i in [w, x, y, z]]
    for c in date:
        if c in cards:
            cards.remove(c)
        else:
            return False
    return True
    
month, day = input().split()

a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = list(map(int, input().split()))

w, x, y, z = 0, 0, 0, 0

count = 0
while not isLuckyDay(month, day, w, x, y, z):
    w, x, y, z = draw_card(a, b, m, w, x, y, z)
    count += 1
    
print(count)