'''
1747 - 소수&팰린드롬
N을 입력받았을 때
N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서 가장 작은 수를 출력해야 하는 문제

단순하게 소수를 판별하는 함수와 팰린드롬인지 확인하는 함수 두 개를 작성하고
반복문을 돌려서 찾는 방식으로 문제를 해결하였다.

Python3으로 제출했더니 시간 초과가 떠서 PyPy3으로 제출하였다.
'''

def prime(n):
    if n <= 1:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def palindrome(n):
    st = str(n)
    if st[:] == st[::-1]:
        return True
    else:
        return False

import sys

n = int(sys.stdin.readline())

while True:
    if prime(n) and palindrome(n): # 소수이면서 팰린드롬인가?
        print(n)
        break
    n += 1 # 아닐 경우


