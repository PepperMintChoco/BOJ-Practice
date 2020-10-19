'''
10179 - 쿠폰
첫 번째 줄에 테스트케이스 T가 주어지면
T줄에 걸쳐 가격을 입력받고
20% 할인된 가격을 소수점 셋째 자리에서 반올림하여 출력해야 하는 문제
'''

import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = float(sys.stdin.readline())
    print('$%.2f'%round(0.8*a, 2))
