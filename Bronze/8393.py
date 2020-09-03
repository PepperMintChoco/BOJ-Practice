'''
8393 - 합
n을 입력받으면 1부터 n까지의 합을 출력해야 하는 문제

n의 최대치가 그리 크지 않기 때문에, 단순 반복문을 사용하였다.
1부터 n까지의 합은 [(n*(n+1)) / 2]라는 일반항을 사용해서 구할 수도 있다.
'''

import sys

res = 0

n = int(sys.stdin.readline())

for i in range(n+1):
    res += i

print(res)
