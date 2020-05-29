# coding: utf-8
# Your code here!

def add_stock(query):
    for i in range(len(query)):
        stock_list[i] += int(query[i])
    
def buy_bread(query):
    for i in range(len(query)):
        if stock_list[i] < int(query[i]):
            return -1
    sum = 0
    for i in range(len(query)):
        stock_list[i] -= int(query[i])
        sum += price_list[i] * int(query[i])
    return sum
        
N, Q = map(int, input().split()) # N: variety of bread, Q: number of queries

price_list = []  # price of bread
stock_list = []  # stock of bread

# initialize lists
for i in range(N):
    price, stock = map(int, input().split())
    price_list.append(price)
    stock_list.append(stock)

# process queries
for i in range(Q):
    query = input().split()
    command = query.pop(0)
    if command == "bake":
        add_stock(query)
    elif command == "buy":
        print(buy_bread(query))