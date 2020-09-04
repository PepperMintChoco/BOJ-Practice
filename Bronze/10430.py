'''
10430 - 나머지

a, b, c를 입력하고
((a+b) % c), (((a%c) + (b%c)) % c), ((a*b) % c), (((a%c) * (b%c)) % c)를 출력해야 하는 문제
'''

import sys

a, b, c= map(int, sys.stdin.readline().split())
print((a+b) % c)
print(((a%c) + (b%c)) % c)
print((a*b) % c)
print(((a%c) * (b%c)) % c)
