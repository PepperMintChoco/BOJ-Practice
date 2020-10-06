'''
6764 - Sounds fishy!
물고기의 높이가 네 줄에 걸쳐 주어질 때,
높이가 모두 같으면 'Fish At Constant Depth'를,
증가하는 수열을 이루면 'Fish Rising'를,
감소하는 수열을 이루면 'Fish Diving'를,
그 외에는 'No Fish'를 출력해야 하는 문제
'''

import sys

s = []

for i in range(4):
    s.append(int(sys.stdin.readline()))

if s[0] == s[1] == s[2] == s[3]:
    print('Fish At Constant Depth')
elif s[0] < s[1] < s[2] < s[3]:
    print('Fish Rising')
elif s[0] > s[1] > s[2] > s[3]:
    print('Fish Diving')
else:
    print('No Fish')
