with open('input.txt') as f:
    input_data = f.readlines()

input_idx = -1
def input():
    global input_idx
    input_idx += 1
    return input_data[input_idx].strip()