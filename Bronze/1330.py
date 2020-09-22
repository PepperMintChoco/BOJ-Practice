'''
1330 - 두 수 비교하기
두 수 A, B가 주어질 때
A가 B보다 큰 경우에는 '>'를,
A가 B보다 작은 경우에는 '<'를,
A와 B가 같은 경우에는 '=='를 출력해야 하는 문제
'''

import sys

a, b = map(int, sys.stdin.readline().split()) 
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')
