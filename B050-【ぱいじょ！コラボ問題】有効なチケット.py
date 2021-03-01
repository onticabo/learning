# coding: utf-8

number = int(input())
keyword = input()

for i in range(number):
    input_line = input()
    message = 'invalid'
    for j in range(len(input_line) - len(keyword) + 1):
        word_end = j + len(keyword)
        parts = input_line[j:word_end]
        if parts == keyword:
            message = 'valid'
            break
        enhanced = input_line[j:word_end + 1]
        for k in range(len(enhanced)):
            parts = enhanced[0:k] + enhanced[k+1:]
            if parts == keyword:
                message = 'valid'
                break
    print(message)