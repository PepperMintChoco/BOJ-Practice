'''
11948 - 과목선택

1~4째 줄에 물리, 화학, 생물, 지구과학 점수 중 3개를 선택하고
5~6째 줄에 역사, 지리 점수 중 2개를 선택했을 때
나올 수 있는 가장 높은 점수를 출력해야 하는 문제
'''
import sys

s = []
t = []

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
f = int(sys.stdin.readline())

s.append(a)
s.append(b)
s.append(c)
s.append(d)
t.append(e)
t.append(f)

s.sort()
t.sort()

print(s[1]+s[2]+s[3]+t[1])
