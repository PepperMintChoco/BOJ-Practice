'''
2420 - 사파리월드
두 도메인의 유명도 N과 M을 입력받았을 때, N과 M의 차이를 출력해야 하는 문제

파이썬 내장함수인 abs()는 절댓값을 반환해주기 때문에 이를 활용하여 풀 수 있다.
'''

import sys

a, b = map(int, sys.stdin.readline().split())

print(abs(a-b))
