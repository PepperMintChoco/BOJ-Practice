'''
5554 - 심부름 가는 길
이동 시간을 나타내는 초를 한 줄에 하나씩 총 네 줄을 입력받고,
이동 시간의 총합을 구하여 첫 줄에 이동 시간의 분, 둘째 줄에 초를 출력하게 하는 문제

먼저 네 줄에 걸쳐 이동 시간을 입력받고, 이동 시간의 총합을 time에 저장한다.
이때 time을 60으로 나눈 몫과 나머지가 총 이동 시간의 분과 초가 된다.
내장함수 divmod(n, m)는 n 나누기 m의 결과를 튜플(몫, 나머지) 형태로 반환한다. 
'''

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

time = a + b + c + d
res = divmod(time, 60)

print(res[0])
print(res[1])
