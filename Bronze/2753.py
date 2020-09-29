'''
2753 - 윤년

연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력해야 하는 문제

연도가 4의 배수이면서 100의 배수가 아닐 때, 또는 400의 배수일 때 윤년이다.
'''

import sys

n = int(sys.stdin.readline())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(1)
else:
    print(0)
