from my_input import input

class Vender:
    def __init__(self, coins):
        self.coins = coins
    def buy(self, price, coins):
        charge_price = coins.price() - price
        return self.coins.payout(charge_price)

class Coins:
    def __init__(self, v_500, v_100, v_50, v_10):
        self.v_500 = v_500
        self.v_100 = v_100
        self.v_50 = v_50
        self.v_10 = v_10
    def __add__(self, other):
        self.v_500 += other.v_500
        self.v_100 += other.v_100
        self.v_50 += other.v_50
        self.v_10 += other.v_10
    def price(self):
        return self.v_500 * 500 + self.v_100 * 100 + self.v_50 * 50 + self.v_10 * 10
    def show(self):
        print(self.v_500, self.v_100, self.v_50, self.v_10)
    def payout(self, price):
        if price > self.price():
            return None
        p_100 = price // 100
        if p_100 > self.v_100:
            return None
        price -= p_100 * 100
        p_50 = price // 50
        if p_50 > self.v_50:
            p_50 = self.v_50
        price -= p_50 * 50
        p_10 = price // 10
        price -= p_10 * 10
        if price != 0:
            return None
        self.v_100 -= p_100
        self.v_50 -= p_50
        self.v_10 -= p_10
        if self.v_10 < 0:
            return None
        return Coins(0, p_100, p_50, p_10)

v_500, v_100, v_50, v_10 = map(int, input().split())
vender = Vender(Coins(v_500, v_100, v_50, v_10))
N = int(input())

for _ in range(N):
    price, x_500, x_100, x_50, x_10 = map(int, input().split())
    pay = Coins(x_500, x_100, x_50, x_10)
    charge = vender.buy(price, pay)
    if charge:
        charge.show()
    else:
        print('impossible')


            