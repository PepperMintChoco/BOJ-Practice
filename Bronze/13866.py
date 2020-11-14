'''
13866 - 팀 나누기
4명의 레벨이 주어지고 두 명씩 팀을 구성한다고 할 때,
두 팀의 레벨 차이의 최솟값을 출력해야 하는 문제

1등-4등, 2등-3등 으로 팀을 구성하면 레벨 차이가 최소가 된다.
'''

import sys

s = list(map(int, sys.stdin.readline().rstrip().split()))

s.sort()

print(abs((s[0]+s[3]) - (s[1]+s[2])))
