'''
18301 - Rats
n1, n2, n12를 입력받고 ⌊(n1+1)(n2+1)/(n12+1)-1⌋를 출력하는 문제 (⌊⌋는 floor function)
'''

import math, sys

n1, n2, n12 = map(int, sys.stdin.readline().split())

print(math.floor(((n1 + 1) * (n2 + 1) / (n12 + 1))-1))
