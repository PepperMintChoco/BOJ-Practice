'''
3046 - R2
어떤 두 수 중 하나를 R1, 나머지를 R2, 평균을 S라고 할 때,
첫째 줄에 R1과 S를 입력받고, R2를 출력해야 하는 문제

S = (R1+R2)/2 이므로 R2 = 2*S-R1 임을 알 수 있다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print(2*b - a)
