'''
11282 - 한글
n이 주어졌을 때, UTF-8로 인코딩했을 때의 n번째 한글을 출력해야 하는 문제

'가'의 UTF-8값이 44032임을 이용하면 된다.
파이썬의 내장 함수 chr()를 활용하여 문제를 해결했다.
'''

import sys

n = int(sys.stdin.readline())

print(chr(44031 + n))
