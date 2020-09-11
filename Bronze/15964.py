'''
15964 - 이상한 기호
기호 ＠를 A＠B = (A+B)×(A-B)라고 정의할 때,
A, B를 입력받고 A＠B의 값을 출력해야 하는 문제
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print((a+b)*(a-b))
