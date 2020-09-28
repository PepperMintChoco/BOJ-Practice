'''
2588 - 곱셈
(세 자리수) × (세 자리수) 곱셈을 할 때
그 과정에 관한 문제
'''

import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

for i in range(3):
    a[i], b[i] = int(a[i]), int(b[i])

a_num = 100*a[0] + 10*a[1] + a[2]
b_num = 100*b[0] + 10*b[1] + b[2]

print(a_num * b[2])
print(a_num * b[1])
print(a_num * b[0])
print(a_num * b_num)
