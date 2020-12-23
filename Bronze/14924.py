'''
14924 - 폰 노이만과 파리
'''

import sys

s, t, d = map(int, sys.stdin.readline().split())

print(d // (2*s) * t)
