'''
10707 - 수도요금
수도회사 X, Y에서는 다음과 같은 수도요금 규정이 있다고 한다
- X사 : 1리터당 A
- Y사 : 기본요금 B(단, 사용량이 C리터 이하라면 요금은 기본요금만 청구됨)
        사용량이 C리터를 넘었을 경우 기본요금 B에 1리터 당 D만큼 추가됨
한 달간 쓰는 수도의 양이 P리터라고 할 때, P의 최솟값을 구해야 하는 문제

첫 번째 줄에는 X사의 1리터당 요금 A,
두 번째 줄에는 Y사의 기본요금 B,
세 번째 줄에는 Y사의 요금이 기본요금이 되는 사용량의 상한 C,
네 번째 줄에는 Y사의 1리터 당 추가요금 D,
다섯 번째 줄에는 집에서 사용하는 한 달간 수도의 양 P가 입력된다
'''

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
p = int(sys.stdin.readline())
x = p * a

if p > c: 
    y = b + ((p - c) * d)
else:
    y = b

if x > y:
    print(y)
else:
    print(x)
