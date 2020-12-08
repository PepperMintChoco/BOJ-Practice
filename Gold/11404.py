'''
11404 - 플로이드

플로이드 와샬 알고리즘의 기본 문제이다.
처음 제출했을 때 WA가 떴는데, 반례를 찾아보니 입력이
1 4 10
1 4 5
이런 식으로도 들어올 수 있다는 것을 알았다.

a에서 b로 가는 기존의 비용보다 더 작은 비용이 입력으로 들어오면
갱신해주는 방법으로 코드를 다시 작성하여 제출하니 AC가 떴다.
'''

import sys

inf = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == inf:
            graph[i][j] = 0
    print(*graph[i][1:])
