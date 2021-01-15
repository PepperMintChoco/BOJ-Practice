'''
1753 - 최단경로

다익스트라 알고리즘 기본 문제이다.
'''

import heapq, sys

inf = int(1e9)

n, m = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

visited = [False]*(n+1)

distance = [inf]*(n+1)

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:      
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])
