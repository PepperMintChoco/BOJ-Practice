'''
5596 - 시험 점수
첫 번째 줄에 민국이의 정보, 수학, 과학, 영어 점수가,
두 번째 줄에 만세의 정보, 수학, 과학, 영어 점수가 주어졌을 때,
총점이 더 큰 쪽의 총점을 출력해아 하는 문제
'''

import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

print(max(sum(a), sum(b)))
