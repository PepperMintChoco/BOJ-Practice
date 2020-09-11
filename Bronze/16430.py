'''
16430 - 제리와 톰
치즈 1kg를 제리가 A/B만큼 훔쳐갔을 때, 남은 치즈의 무게를 출력해야 하는 문제
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print(b-a, b)
