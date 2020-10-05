'''
5893 - 17배
입력받은 2진수를 17배한 다음 이진수로 출력해야 하는 문제
'''

import sys

n = int(sys.stdin.readline(), 2) #입력받은 2진수를 n에 10진수로 저장

print(str(bin(n*17)).replace('0b', '')) # 17배 -> 2진수 변환 -> 문자열 변환 -> '0b' 제거 후 출력
