'''
5575 - 타임 카드
첫 번째 줄에는 A 씨의 출근 시간과 퇴근 시간,
두 번째 줄에는 B 씨의 출근 시간과 퇴근 시간,
세 번째 줄에는 C 씨의 출근 시간과 퇴근 시간이 주어졌을 때
첫 번째 줄에 A 씨의 근무 시간,
두 번째 줄에 B 씨의 근무 시간,
세 번째 줄에 C 씨의 근무 시간을 출력해야 하는 문제
'''

import sys

for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
    s2 -= s1
    if s2 < 0:
        s2 += 60
        m2 -= 1
    m2 -= m1
    if m2 < 0:
        m2 += 60
        h2 -= 1
    h2 -= h1

    print(h2, m2, s2)
