'''
14264
정육각형의 한 점에서 다른 세 점으로 대각선을 그으면 4개의 삼각형이 생긴다
정육각형의 한 변의 길이가 주어지면 가장 작은 삼각형의 넓이를 출력해야 하는 문제

삼각비를 활용하여 풀면 된다.
'''

import sys
from math import *

l = int(sys.stdin.readline())

print((l*l*sin(radians(120)))/2)
