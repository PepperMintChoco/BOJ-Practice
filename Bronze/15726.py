'''
15726 - 이칙연산
세 수가 연속으로 주어졌을 때 한 번의 곱셈 기호와 나눗셈 기호를 넣어서
만들 수 있는 가장 큰 값을 출력해야 하는 문제
'''

import sys

a, b, c = map(int, sys.stdin.readline().split())

print(max(int(a*b/c), int(a/b*c)))
