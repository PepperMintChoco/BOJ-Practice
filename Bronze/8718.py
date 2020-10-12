'''
8718 - Bałwanek
(이 문제는 구글 번역을 사용하여 해결하였기 때문에 정해가 아닐 수도 있음)
'''

import sys

x, k = map(int, sys.stdin.readline().split())

if 7000 * k <= 1000 * x:
    print(7000 * k)
elif 3500 * k <= 1000 * x:
    print(3500 * k)
elif 1750 * k <= 1000 * x:
    print(1750 * k)
else:
    print(0)
