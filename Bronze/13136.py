'''
13136 - Do Not Touch Anything
좌석의 세로 크기, 가로 크기, 한 대의 CCTV가 수용할 수 있는 범위가 주어졌을 때,
모든 좌석을 전부 촬영할 수 있는 CCTV의 최소 개수를 출력해야 하는 문제
'''

import sys

r, c, n = map(int, sys.stdin.readline().split())

if r % n > 0:
    if c % n > 0:
        print((r // n + 1) * (c // n + 1))
    else:
        print((r // n + 1) * (c // n + 0))
else:
    if c % n > 0:
        print((r // n + 0) * (c // n + 1))
    else:
        print((r // n + 0) * (c // n + 0))
