'''
11549 - Identifying tea
첫 번째 줄에 T가 주어지고, 두 번째 줄에 5개의 수가 주어지면
5개의 수 중 T와 일치하는 수의 개수를 출력해야 하는 문제

'10797 - 10부제' 문제와 유사하다.
'''

import sys

a = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in s:
    if i == a:
        cnt += 1

print(cnt)
