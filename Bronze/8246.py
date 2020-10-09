'''
8246 - Stół
(이 문제는 구글 번역을 사용하여 해결하였기 때문에 정해가 아닐 수도 있음)
'''

import sys

a, b, k = map(int,sys.stdin.readline().split())

print((a//k)*(b//k) - max(0, (a//k-2)) * max(0, (b//k-2)))
