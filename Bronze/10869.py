'''
10869 - 사칙연산
두 자연수 A, B를 입력받고
A+B, A-B, A*B, A//B, A%B를 출력해야 하는 문제
'''

import sys

a, b = map(int, sys.stdin.readline().split())
print(a+b, a-b, a*b, a//b, a%b, sep = '\n')

