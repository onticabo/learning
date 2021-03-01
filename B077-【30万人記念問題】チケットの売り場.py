# coding: utf-8
# from my_input import input

class Counter:
    def __init__(self, process_time):
        self.process_time = process_time
        self.wait_time = 0
    def pass_time(self):
        self.wait_time -= 1
        if self.wait_time <= 0:
            self.wait_time = 0
            self.n = 0
    def vacant(self):
        return self.wait_time <= 0
    def accept(self, n):
        self.wait_time = self.process_time
        self.n = n

counter_num, line_num = map(int, input().split())

counters = []
for i in range(counter_num):
    counters.append(Counter(int(input())))
counters = sorted(counters, key=lambda c: c.process_time)

time = 0
line = list(range(1, line_num+1))
while line or False in [counter.vacant() for counter in counters]:
    for counter in counters:
        counter.pass_time()
        if counter.vacant() and line:
            n = line.pop(0)
            counter.accept(n)
    time += 1
print(time-1)
