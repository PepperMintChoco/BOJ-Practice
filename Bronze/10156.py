'''
10156 - 과자
과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M이 주어졌을 때,
금액이 부족하다면 부족한 금액을 출력해야 하는 문제
'''

import sys

k, n, m = map(int, sys.stdin.readline().split())

if k * n > m:
    print(k * n - m)
else:
    print(0)
