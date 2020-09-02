'''
5522 - 카드 게임
다섯 줄에 걸쳐 정수를 입력받고, 입력받은 정수들의 총합을 출력해야 하는 문제

입력받은 정수를 리스트 s에 저장하고, 내장함수 sum()을 이용해 리스트의 합을 구하면 된다.
'''

import sys

s = []

for i in range(5):
    s.append(int(sys.stdin.readline()))

print(sum(s))
