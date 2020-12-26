'''
15059 - Hard choice

각 값들의 차이를 모두 더하면 되는 문
'''

import sys

a = list(map(int, sys.stdin.readline().split()))
r = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(3):
    if a[i] < r[i]:
        res += r[i] - a[i]

print(res)
