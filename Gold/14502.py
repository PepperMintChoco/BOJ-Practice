'''
14502 - 연구소
지도의 세로 크기 N과 가로 크기 M이 주어지고
N개에 줄에 지도의 모양이 주어졌을 때(0: 빈 공간, 1: 벽, 2: 바이러스),
얻을 수 있는 안전 영역의 최대 크기를 출력해야 하는 문제

1. 먼저 조건에 따라 N과 M, 지도를 입력받는다.
지도는 배열 lab에 2차원 배열 형태로 저장한다.

2. lab 안에서 바이러스의 위치를 탐색하고
배열 virus에 바이러스의 위치를 튜플 형태로 저장한다.

3. wall()에서 빈칸(0) 세 개를 벽(1)으로 바꾼다.
바꾼 뒤 virus_bfs() 함수를 호출한다.

4. 시뮬레이션을 돌릴 지도(lab2)에 기존 지도(lab)를 deepcopy 한다.
방문 여부를 확인할 배열 visit도 visit2에 복사한다.

5. deque와 넓이 우선 탐색 알고리즘을 활용하여
바이러스(2)와 상하좌우로 인접한 빈칸(0)을 바이러스(2)로 바꾼다.

6. 넓이 우선 탐색이 끝난 지도(lab2)는 바이러스가 퍼진 뒤의 모습이 된다.
이 지도를 check() 함수에 전달한다.

7. check() 함수에서는 지도 내의 0의 개수를 센 뒤 배열 res에 저장한다.

8. 벽을 세우고 바이러스를 퍼뜨리는 모든 경우의 수를 simulate했을 때,
안전 영역의 최대 크기는 max(res)가 된다.


deepcopy를 사용해서 그런지 실행 시간이 꽤 오래 걸렸다.
Python3으로 제출하면 TLE가 날 것이 뻔해서 Pypy3으로 제출했다.

N, M의 값도 작은 데다가 알고리즘 분류에 브루트 포스가 있길래
벽을 세우는 과정은 브루트 포스로 구현했다.
그러나 combinations을 사용하거나 dfs를 돌리면
실행 시간이 조금 단축되지 않을까 싶다.
'''

import sys
from collections import deque
from copy import deepcopy

lab = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
virus = []
res = []

n, m = map(int, sys.stdin.readline().split())

visit = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i, j))

def check(lab_check):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if lab_check[i][j] == 0:
                cnt += 1
    res.append(cnt)

def virus_bfs():
    q = deque()
    lab2 = deepcopy(lab)
    visit2 = deepcopy(visit)
    for (a, b) in virus:
        q.append((a, b))
        while q:
            x, y = q.popleft()
            for i in range(4):
                move_x = x + dx[i]
                move_y = y + dy[i]
                if (move_x < 0 or move_x >= n or move_y < 0 or move_y >= m):
                    continue
                else:
                    if (lab2[move_x][move_y] == 0) and (visit2[move_x][move_y] != 1):
                        visit2[move_x][move_y] = 1
                        q.append((move_x, move_y))
                        lab2[move_x][move_y] = 2
    check(lab2)

def wall(wall_cnt):
    if wall_cnt == 3:
        virus_bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(wall_cnt+1)
                lab[i][j] = 0

def main():
    wall(0)
    print(max(res))

if __name__ == "__main__":
    main()
