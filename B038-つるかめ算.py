feet, head, crane, turtle = map(int, input().split())

matched = [0, 0]
for i in range(1, head):
    tmp_feet = i * crane + (head - i) * turtle
    if tmp_feet == feet:
        if matched != [0, 0]:
            matched = [0, 0]
            break
        else:
            matched = [i, head - i]
if matched != [0, 0]:
    print(matched[0], matched[1])
else:
    print('miss')