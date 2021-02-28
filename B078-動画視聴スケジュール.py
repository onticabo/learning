from my_input import input

class Program:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration
        self.playing = range(start, start + duration + 1)

class TimeTable:
    def __init__(self, program_list):
        self.program_list = program_list
        self.make_time_table()

    def make_time_table(self):
        self.program_list = sorted(self.program_list, key=lambda x:x.start)
            
N = int(input())

program_list = [Program(s, d) for s, d in [map(int, input().split()) for _ in range(N)]]
table = TimeTable(program_list)

print(table)