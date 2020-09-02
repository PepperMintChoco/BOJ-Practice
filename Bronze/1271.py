'''
1271 - 엄청난 부자2
n, m 두 정수를 입력받고 n 나누기 m의 몫과 나머지를 한 줄 씩 출력하는 문제
'''

import sys

n, m = map(int, sys.stdin.readline().split())

print(n // m)

print(n % m)
