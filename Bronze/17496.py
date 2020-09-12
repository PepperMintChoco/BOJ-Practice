'''
17496 - 스타후르츠
N: 여름의 일 수
T: 스타후르츠 씨앗이 자라는데 걸리는 일 수
C: 스타후르츠를 심을 수 있는 칸 수
P: 스타후르츠의 개당 가격
스타후츠츠를 팔아서 벌 수 있는 최대 수익을 출력해야 하는 문제
'''

import sys

n, t, c, p = map(int, sys.stdin.readline().split())

print((n-1) // t * c * p)
