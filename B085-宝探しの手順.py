from my_input import input

def my_sign(x):
    return (x > 0) - (x < 0)

def get_frequency_sequence(seq, max=10000):
    sequance = []
    for item in seq:
        for sign in [1, -1]:
            num = item * sign
            sequance.append(num)
        if abs(num) > max:
            break
    return sequance

def get_route_length(seq, item):
    total = 0
    value = 0
    for i in range(1, len(seq)):
        total += abs(seq[i-1] - seq[i])
        if abs(seq[i]) >= abs(item) and my_sign(seq[i]) == my_sign(item):
            value = total - abs(seq[i] -item)
            break
    return value

item = int(input())

## method 1
targets = get_frequency_sequence(list(range(10000)))

print(get_route_length(targets, item), end=' ')

## method 2
seq = [0] + [2 ** i for i in range(10000) if 2 ** i < 10000]
targets = get_frequency_sequence(seq)

print(get_route_length(targets, item))
