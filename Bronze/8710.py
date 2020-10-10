'''
8710 - Koszykarz
(이 문제는 구글 번역을 사용하여 해결하였기 때문에 정해가 아닐 수도 있음)
'''

import sys

k, w, m = map(int, sys.stdin.readline().split())

n = w - k

if n % m == 0:
    print(n // m)
else:
    print(n // m + 1)
