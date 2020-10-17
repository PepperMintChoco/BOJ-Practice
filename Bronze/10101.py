'''
10101 - 삼각형 외우기
세 변의 길이를 입력하면 어떤 삼각형인지 출력해야 하는 문제
'''

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c == 180: # 삼각형일 경우
    if a == 60 and b == 60 and c == 60: # 정삼각형일 경우
        print('Equilateral')
    elif a == b or a == c or b == c: # 이등변삼각형일 경우
        print('Isosceles')
    else: # 그 외의 경우
        print('Scalene')
else: # 삼각형이 될 수 없을 경우
    print('Error')
