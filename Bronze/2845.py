'''
2845 - 파티가 끝나고 난 뒤
첫째 줄에 1m^2당 사람의 수 L, 파티가 열렸던 곳의 넓이 P를 입력받고
둘째 줄에 각 기사에 실려있는 참가자 수 5개를 입력받은 뒤
상근이가 계산한 참가자 수와 각 기사에 적혀있는 참가자 수의 차이를 출력해야 하는 문제

둘째 줄에 입력받은 숫자들과 L*P 값의 차이를 각각 출력하면 된다.
'''

import sys

l, p = map(int, sys.stdin.readline().split())

m = l * p

s = list(map(int, sys.stdin.readline().split()))

print(s[0] - m, s[1] - m, s[2] - m, s[3] - m, s[4] - m)
