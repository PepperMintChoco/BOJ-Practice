'''
1550 - 16진수
16진수 수를 입력하면 10진수로 변환해 출력하는 문제

int('0x{}'.format(16진수 수), 16) 꼴의 함수를 사용해 풀 수 있다.
'''

import sys

a = input()

b = int('0x{}'.format(a), 16)
print(b)
