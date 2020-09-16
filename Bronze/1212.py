'''
1212 - 8진수 2진수
8진수가 주어졌을 때, 2진수로 변환해 출력해야 하는 문제

a에서 8진수의 형태로 입력을 받고,
2진수로 변한한 뒤 str형으로 바꾸고
replace 함수를 이용해 b의 0b를 없앤 뒤 출력하면 된다.
'''

import sys

a = int(sys.stdin.readline(), 8)

b = str(bin(a))

print(b.replace('0b', ''))
