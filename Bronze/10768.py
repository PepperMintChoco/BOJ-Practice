'''
10768 - 특별한 날
날짜(월, 일)를 입력받고, 이 날짜가 2월 18일인지, 전인지, 후인지를 출력해야 하는 문제
'''

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if a == 2:
    if b > 18:
        print('After')
    elif b < 18:
        print('Before')
    elif b == 18:
        print('Special')
elif a > 2:
    print('After')
elif a < 2:
    print('Before')
