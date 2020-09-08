'''
13277 - 큰 수 곱셈
두 정수 A, B를 입력받고 A*B를 출력해야 하는 문제

큰 수를 다루는 문제로, 파이썬으로는 쉽게 해결할 수 있는 문제이다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print(a*b)
