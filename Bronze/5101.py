'''
5101 - Sequences
어떤 수열이 있을 때,
첫째 줄에 첫항, 공비, n번째항이 주어지면
n의 값을 출력해야 하는 문제
만약 n이 존재하지 않는다면, X를 출력해야 한다
입력의 마지막에는 0 0 0이 주어진다

첫항이 a, 공차가 d, n번째항이 an일 때, a + n*d = an
즉 구해야하는 n의 값은 (an - a) / d 이다.
(an - a) / d가 나누어떨어지지 않는다면 n이 존재할 수 없으므로 X를 출력한다.
(an - a) / d가 나누어떨어지더라도, (an - a)가 음수가 되면 안되므로 X를 출력한다.
그 외의 경우에는 (floor((an - a) / d) + 1)을 출력한다.
문제에서 다루는 수의 범위가 그리 크지 않으므로 int()형 변환을 사용한다.
마지막에 1을 더하는 이유는 첫항이 a(0)이 아닌 a(1)이기 때문이다.

이 문제는 단순 반복문으로 구현하여도 보너스 시간이 적용되어 맞힐 수 있었다.
'''

import sys

while True:
    a, d, an = map(int, sys.stdin.readline().split())
    if a == 0 and d == 0 and an == 0:
        break
    else:
        s = (an - a) / d
        if s - int(s) > 0:
            print('X')
        elif an - a < 0:
            print('X')
        else:
            print(int(s) + 1)
            
