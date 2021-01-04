# coding: utf-8
from my_input import input
import pprint
import re

def parse_log(log):
    address = '[0-9]{,3}.[0-9]{,3}.[0-9]{,3}.[0-9]{,3}'
    postCode = re.match(address, log)
    print(postCode.group())

segment = map(int, input().split())
n = int(input())
log = []
for _ in range(n):
    input_line = input()
    parse_log(input_line)
    log.append(input_line)ire

