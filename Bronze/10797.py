'''
10797 - 10부제
날짜와 자동차 번호의 일의 자리 숫자 5개가 주어졌을 때,
10부제를 위반하는 차량의 대수를 출력해야 하는 문제
'''

import sys

day = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in l:
    if i == day:
        cnt += 1

print(cnt)
