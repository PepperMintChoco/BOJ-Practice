'''
8723
(이 문제는 구글 번역을 사용하여 해결하였기 때문에 정해가 아닐 수도 있음)
세 변의 길이가 주어질 때
직각삼각형이면 1, 정삼각형이면 2, 그 외의 삼각형이거나 삼각형이 만들어질 수 없는 경우 0을 출력해야 하는 문제
'''

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print('1')
elif a == b == c:
    print('2')
else:
    print('0')
