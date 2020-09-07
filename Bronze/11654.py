'''
11654 - 아스키 코드
알파벳 소문자, 대문자 또는 숫자 0-9를 입력받고 주어진 글자의 아스키 코드 값을 출력해야 하는 문제
'''

import sys

a = sys.stdin.readline().rstrip()

print(ord(a))
