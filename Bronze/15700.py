'''
15700 - 타일 채우기 4

DP 문제인 것처럼 보이나 전혀 DP 문제가 아니다.
n*m 크기의 직사각형에 2*1, 1*2 크기의 타일을 채운다고 하면
최대 n*m//2개를 채울 수 있다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())
print(n * m // 2)
