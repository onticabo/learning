# coding: utf-8

days, buy, sell = map(int, input().split())

money = 0
stock = 0
count = 0

for i in range(days):
    price = int(input())
    if price <= buy:
        money -= price
        stock += price
        count += 1
    elif price >= sell:
        money += price * count
        stock = 0
        count = 0

money += price * count
print(money)
