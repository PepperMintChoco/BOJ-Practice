'''
1279 - TV 크기
TV의 대각선 길이와, 높이 너비의 비율이 주어졌을 때,
실제 높이와 너비의 길이를 출력해야 하는 문제
'''

import sys

a, b, c = map(int, sys.stdin.readline().split())

x = b ** 2 + c ** 2
y = (a ** 2 / (b ** 2 + c ** 2)) ** 0.5

print(int(b * y), int(c * y))
