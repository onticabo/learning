from my_input import input

def coin_count(pay):
    coins = [500, 100, 50, 10, 5, 1]
    coin_count = 0
    while pay:
        for coin in coins:
            coin_count += pay // coin
            pay -= pay // coin * coin
    return coin_count

price = int(input())
min_pay = 21

for y500 in range(3):
    for y100 in range(5):
        for y50 in range(2):
            for y10 in range(5):
                for y5 in range(2):
                    for y1 in range(5):
                        pay = y500 * 500 + y100 * 100 + y50 * 50 + y10 * 10 + y5 * 5 + y1 * 1
                        if pay >= price:
                            pay_count = y500 + y100 + y50 + y10 + y5 + y1
                            charge_count = coin_count(pay - price)
                            min_pay = min(pay_count + charge_count, min_pay)

print(min_pay)
