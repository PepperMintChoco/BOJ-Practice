'''
2261 - 가장 가까운 두 점

모든 경우의 수를 셀 경우 시간 초과가 나므로 분할 정복 기법을 활용해야 한다.

먼저 입력받은 좌표들을 x좌표 기준으로 정렬한 뒤
좌우를 나누는 기준선 middle을 정한다(middle은 n/2번째 점과 n/2+1번째 점 x좌표의 평균).
이 기준선과 가장 가까운 점까지의 거리를 찾아 distance에 저장한다.
이 범위(좌우 거리 distance 이내)에 있는 점을 cd_in_range에 저장하고
cd_in_range의 좌표들을 y좌표 기준으로 정렬한다.
그리고 각 점과의 거리를 계산해서 min_distance를 갱신해주고,
y좌표 차이가 distance를 초과하면 비교 작업을 중단한다.
(가로 길이 2*d, 세로 길이 d인 직사각형 내에 서로 간 거리가 최소 d가 되도롤 점을 배치한다고 했을 때
최대 7개까지 들어갈 수 있다는 사실에 의하면, 비교 과정은 7번을 넘지 않는다고 한다.)

추가로 중복되는 점이 있을 경우 가장 가까운 두 점은 그 두 점이 된다(거리 0)
따라서 set -> list로 중복을 제거해주는 과정에서 배열에 크기 변화가 생겼다면 바로 0을 출력한다.
'''

import sys

def return_dist(cd1, cd2):
    return (cd1[0] - cd2[0])**2 + (cd1[1] - cd2[1])**2

def closest_pair(cd, n):
    if n == 2: # base case
        return return_dist(cd[0], cd[1])
    elif n == 3: # base case
        return min(return_dist(cd[0], cd[1]), return_dist(cd[1], cd[2]), return_dist(cd[0], cd[2]))
    # 분할 정복 기법을 활용해 x좌표 기준 최소 거리를 distance에 저장
    distance = min(closest_pair(cd[(n//2):], n//2), closest_pair(cd[:(n//2)], n//2))

    middle = (cd[n//2][0]+cd[n//2-1][0]) // 2
    cd_in_range = [] 
    for i in cd: # 두 점의 x좌표 거리가 distance보다 클 경우 제외
        if (middle-i[0])**2 <= distance:
            cd_in_range.append(i)

    cd_in_range = sorted(cd_in_range, key = lambda x: x[1])

    if len(cd_in_range) == 1:
        return distance
    else:
        min_distance = distance
        for i in range(len(cd_in_range)-1):
            for j in range(i+1, len(cd_in_range)):
                # 두 점의 y좌표 거리가 distance보다 클 경우 제외
                if (cd_in_range[i][1]-cd_in_range[j][1])**2 > distance:
                    break
                # 두 점이 middle보다 왼쪽에 있는 경우 제외
                elif cd_in_range[i][0] < middle and cd_in_range[j][0] < middle:
                    continue
                # 두 점이 middle보다 오른쪽에 있는 경우 제외
                elif cd_in_range[i][0] > middle and cd_in_range[j][0] > middle:
                    continue
                min_distance = min(min_distance, return_dist(cd_in_range[i], cd_in_range[j]))
    return min_distance

n = int(sys.stdin.readline())

coordinate = []

for i in range(n):
    coordinate.append(tuple(map(int, sys.stdin.readline().split())))

coordinate = list(set(map(tuple, coordinate))) # 중복 제거

if len(coordinate) != n: # 중복된 점이 있을 경우
    print(0)
else:
    coordinate.sort()
    print(closest_pair(coordinate, n))
