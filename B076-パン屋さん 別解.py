# coding: utf-8
from my_input import input

class Bread:
    def __init__(self, price, stock=0):
        self.price = price
        self.stock = stock

    def can_buy(self, amount):
        return self.stock >= amount
    def buy(self, amount):
        self.stock -= amount
        return self.price * amount
    def bake(self, amount):
        self.stock += amount
        
n, q = map(int, input().split())

# initialize bread lists
bread = []
for _ in range(n):
    price, stock = map(int, input().split())
    bread.append(Bread(price, stock))
# process queries
for _ in range(q):
    query, *amount = input().split()
    amount = [int(i) for i in amount]
    if query == 'bake':
        for i in range(n):
            bread[i].bake(amount[i])
    elif query == 'buy':
        if False in [bread[i].can_buy(amount[i]) for i in range(n)]:
            print(-1)
        else:
            print(sum([bread[i].buy(amount[i]) for i in range(n)]))
