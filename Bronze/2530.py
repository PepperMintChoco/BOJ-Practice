'''
2530 - 인공지능 시계
현재 시각과 요리하는 데 필요한 시간이 주어졌을 때,
요리가 종료되는 시각을 출력해야 하는 문제
'''

import sys

h, m, s = map(int, sys.stdin.readline().split()) # 현재 시각
n = int(sys.stdin.readline()) # 요리하는 데 필요한 시간

s += (n % 60)
n = (n // 60)

if s >= 60:
    s -= 60
    m += 1

m += (n % 60)
n = (n // 60)

if m >= 60:
    m -= 60
    h += 1

h += n % 24

if h >= 24:
    h -= 24

print(h, m, s)
