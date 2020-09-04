'''
11283 - 한글 2
한글 한 글자를 입력받고 그것이 몇 번째 글자인지 출력해야 하는 문제

ord() 함수를 사용하면 입력받은 한글의 유니코드값을 알 수 있다.
'가'의 유니코드값이 44032임을 참고해야 한다.
'''

import sys

a = ord(sys.stdin.readline().rstrip())

print(a - 44031)
