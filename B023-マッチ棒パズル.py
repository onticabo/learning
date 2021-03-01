# coding: utf-8
from my_input import input
def show_output_list(output_list):
    if output_list:
        for num in sorted(output_list):
            print(num)
    else:
        print('None')

strnum = input()
move_inner = {'0':['6', '9'], '1':[], '2':['3'], '3':['2', '5'], '4':[],
              '5':['3', '5'], '6':['0', '9'], '7':[], '8':[], '9':['0', '6']}
can_add     = {'0':['8'], '1':['7'], '2':[], '3':['9'], '4':[],
              '5':['6', '9'], '6':['8'], '7':[], '8':[], '9':[]}
can_sub     = {'0':[], '1':[], '2':[], '3':[], '4':[],
              '5':[], '6':['5'], '7':['1'], '8':['0', '6'], '9':['3', '5']}
output_list = []

for i in range(len(strnum)):
    changeable = move_inner[strnum[i]]
    for c in changeable:
        newstr = strnum[:i] + c + strnum[i+1:]
        output_list.append(newstr)



def addable(c):
    return len(can_add[c]) != 0
def subable(c):
    return len(can_sub[c]) != 0
a = []
s = []
for i in range(len(strnum)):
    if addable(strnum[i]):
        a.append(i)
    if subable(strnum[i]):
        s.append(i)
combo = []
for i in a:
    for j in s:
        if i != j:
            combo.append((i, j))
#output_list = []
for a, s in combo:
    astr = can_add[strnum[a]]
    sstr = can_sub[strnum[s]]
    for ad in astr:
        for su in sstr:
            if a < s:
                newstr = strnum[:a] + ad + strnum[a+1:s] + su + strnum[s+1:]
            elif s < a:
                newstr = strnum[:s] + su + strnum[s+1:a] + ad + strnum[a+1:]
                output_list.append(newstr)

show_output_list(output_list)

