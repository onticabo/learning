from my_input import input

class Task:
    def __init__(self, priority, duration, start, end):
        self.priority = priority
        self.remain = duration
        self.start = start
        self.end = end
    def can_do(self, current):
        return self.start <= current <= self.end
    def complete(self):
        return self.remain == 0

N = int(input())
input_line = [list(map(int, input().split())) for _ in range(N)]
tasks = [Task(p, d, s, e) for p, (d, s, e) in enumerate(input_line)]

dummy = Task(1000, 1000, 0, 1000)
current = dummy
for time in range(1000):
    for task in tasks:
        if task.can_do(time) and task.priority < current.priority:
            current = task
    if current.can_do(time):
        current.remain -= 1
        if current.complete():
            tasks.remove(current)
            current = dummy
            if not tasks:
                break
if tasks:
    print('NO')
else:
    print('YES')