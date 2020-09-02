'''
2338 - 긴자리 계산
두 수 a, b를 입력받고 a+b, a-b, a*b의 결과를 한 줄 씩 출력하는 문제

파이썬 언어는 Big integer를 지원해주므로 별도의 코드 없이 쉽게 해결할 수 있다.
'''

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

print(a+b)
print(a-b)
print(a*b)
