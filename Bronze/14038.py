'''
14038 - Tournament Selection

W의 개수를 카운트해주고
W의 개수가 5, 6일 경우 1을,
3, 4일 경우 2를,
1, 2일 경우 1을 출력하면 된다.
'''

import sys

s = []

for i in range(6):
    s.append(sys.stdin.readline().rstrip())

cnt = s.count('W')

if cnt == 5 or cnt == 6:
    print(1)
elif cnt == 3 or cnt == 4:
    print(2)
elif cnt == 1 or cnt == 2:
    print(3)
else:
    print(-1)
