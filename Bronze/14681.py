'''
14681 - 사분면 고르기
어떤 점의 x좌표와 y좌표가 두 줄에 걸쳐 주어지면
이 점이 위치한 사분면의 번호를 출력해야 하는 문제
'''

import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)
