'''
1008 - A/B
A와 B를 입력받고 A/B를 출력해야 하는 문제

상대오차가 10^(-9) 이하이면 정답이므로, 별도의 모듈이나 함수 없이도 풀 수 있다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print(a/b)
