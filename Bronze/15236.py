'''
15236 - Dominos
'''

import sys

def intsum(n):
    s = 0
    for i in range(n+2):
        s += i
    return s

a = int(sys.stdin.readline())
print(a * intsum(a))
