'''
11943 - 파일 옮기기
첫 번째 바구니에는 사과 A개와 오렌지 B개가,
두 번째 바구니에는 사과 C개와 오렌지 D개가 있다고 할 때
사과와 오렌지를 옮기는 최소 횟수를 출력해야 하는 문제

A+D와 C+B를 계산하고 둘 중 작은 값을 출력하면 된다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

if a+d < b+c:
    print(a+d)
else:
    print(b+c)

