'''
1712 - 손익분기점
A가 고정비용, B가 가변비용, C가 책정가격일 때
최초로 이익이 발생하는 판매량(손익분기점)을 출력해야 하는 문제
단, 손익분기점이 존재하지 않는다면 -1을 출력해야 한다.
'''

import sys

a, b, c = map(int, sys.stdin.readline().split())

bep = 0

if c <= b:
    bep = -1
else:
    bep = a // (c-b) + 1

print(bep)
