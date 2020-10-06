'''
5928 - Contest Timing
설명 추가 예정
'''

import sys

d, h, m = map(int, sys.stdin.readline().split())
a = 11 * 60 + 11
b = h * 60 + m

if d < 11 or (d == 11 and a > b):
    print(-1)
elif b >+ a:
    print((d - 11) * 60 * 24 + (b - a))
else:
    print((d - 12) * 60 * 24 + 60 * 24 - (a - b))
