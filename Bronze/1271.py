'''
1271 - 엄청난 부자2
n, m 두 정수를 입력받고 n 나누기 m의 몫과 나머지를 한 줄 씩 출력하는 문제

파이썬 내장함수인 divmod()를 사용했다.
divmod(n, m)은 n 나누기 m의 몫과 나머지를 튜플 형태로 반환한다.
'''

import sys

n, m = map(int, sys.stdin.readline().split())

dm = divmod(n, m)

print(dm[0])
print(dm[1])
