'''
17256 - 달달함이 넘쳐흘러
a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)이고
a.x, a.y, a.z가 첫째 줄, c.x, c.y, c.z가 둘째 줄에 주어질 때
b.x, b.y, b.z를 출력해야 하는 문제
'''

import sys

ax, ay, az = map(int, sys.stdin.readline().split())
cx, cy, cz = map(int, sys.stdin.readline().split())

print(cx - az, cy // ay, cz - ax)
