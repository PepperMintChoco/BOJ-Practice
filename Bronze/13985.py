'''
13985 - Equality
a + b = c 꼴로 입력받은 뒤
식이 맞다면 YES를, 틀리면 NO를 출력해야 하는 문제

'''

import sys

s = list(sys.stdin.readline().split())

if int(s[0]) + int(s[2]) == int(s[4]):
    print('YES')
else:
    print('NO')
